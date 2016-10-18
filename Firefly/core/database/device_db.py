# -*- coding: utf-8 -*-
# @Author: Zachary Priddy
# @Date:   2016-10-12 23:18:17
# @Last Modified by:   Zachary Priddy
# @Last Modified time: 2016-10-17 22:24:12

import json

import pickle

from core import deviceDB
from sys import modules

from core import ffScheduler

class DeviceViews(object):

  def __init__(self):
    self.deviceViewsList = getDeviceViewsList()
    self.deviceStatusDict = getDeviceStatusDict()

    ffScheduler.runEveryS(2, self.refreshViews, job_id='Device_Refresher')

  def refreshViews(self):
    self.deviceViewsList = getDeviceViewsList()
    self.deviceStatusDict = getDeviceStatusDict()


def getDeviceList(lower=True):
  device_list = {}
  for d in deviceDB.find({},{"config.name":1,"id":1}):
    if d.get('config').get('name') is not None:
      if lower:
        device_list[d.get('config').get('name').lower()] = d.get('id')
      else:
        device_list[d.get('config').get('name')] = d.get('id')
  return device_list

def getDeviceViewsList():
  devices = []
  for d in deviceDB.find({},{'status.views':1, 'id':1}):
    if (d.get('status').get('views')):
      devices.append(d.get('status').get('views'))
  return devices

def getDeviceStatusDict():
  devices = {}
  for d in deviceDB.find({},{'status':1, 'id':1}):
    d_id = d.get('id')
    if (d.get('status')):
      devices[d_id] = d.get('status')
  return devices


def reinstallDevices():
  deviceDB.remove({})
  with open('config/devices.json') as devices:
    allDevices = json.load(devices)
    for name, device in allDevices.iteritems():
      if device.get('module') != "ffZwave":
        package_full_path = device.get('type') + 's.' + device.get('package') + '.' + device.get('module')
        package = __import__(package_full_path, globals={}, locals={}, fromlist=[device.get('package')], level=-1)
        reload(modules[package_full_path])
        dObj = package.Device(device.get('id'), device)
        d = {}
        d['id'] = device.get('id')
        d['ffObject'] = pickle.dumps(dObj)
        d['config'] = device
        d['status'] = {}
        deviceDB.insert(d)
