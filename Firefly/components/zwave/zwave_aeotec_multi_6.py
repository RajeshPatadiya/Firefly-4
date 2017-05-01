from Firefly import logging
from Firefly.components.zwave.zwave_device import ZwaveDevice
from Firefly.helpers.device import Device
from Firefly.helpers.events import Event
import asyncio
from openzwave.network import ZWaveNode
from Firefly import logging
from Firefly.const import (STATE, SENSORS, DEVICE_TYPE_MOTION, EVENT_TYPE_BROADCAST, MOTION, MOTION_ACTIVE, MOTION_INACTIVE)



TITLE = 'Aeotec Gen6 MultiSensor'
DEVICE_TYPE = DEVICE_TYPE_MOTION
AUTHOR = 'Zachary Priddy'
COMMANDS = []
REQUESTS = [STATE, MOTION]
INITIAL_VALUES = {'_state': False, '_sensitivity': 3, '_timeout': 300}

def Setup(firefly, package, **kwargs):
  logging.message('Entering %s setup' % TITLE)
  sensor = ZwaveAeotecMulti(firefly, package, **kwargs)
  # TODO: Replace this with a new firefly.add_device() function
  firefly.components[sensor.id] = sensor
  return sensor.id


class ZwaveAeotecMulti(ZwaveDevice):
  def __init__(self, firefly, package, **kwargs):
    init_values = INITIAL_VALUES
    if kwargs.get('initial_values'):
      init_values.update(kwargs.get('initial_values'))
    kwargs['initial_values'] = init_values
    super().__init__(firefly, package, TITLE, AUTHOR, COMMANDS, REQUESTS, DEVICE_TYPE, **kwargs)
    self.__dict__.update(kwargs['initial_values'])

    self.add_request(STATE, self.get_state)
    self.add_request(MOTION, self.get_motion)


  def update_device_config(self, **kwargs):
    # TODO: Pull these out into config values
    # TODO Copy this retry logic to all zwave devices
    """
    Updated the devices to the desired config params. This will be useful to make new default devices configs.

    For example when there is a gen6 multisensor I want it to always report every 5 minutes and timeout to be 30 seconds.
    Args:
      **kwargs ():
    """

    if self._update_try_count >= 5:
      self._config_updated = True
      return

    # TODO: self._sensitivity ??
    #sensitivity = 3 # index 4
    #timeout = 10 # index 8
    sensitivity = self._initial_values.get('_sensitivity', 3)
    timeout = self._initial_values.get('_timeout', 300)
    scale = 1 # index 64
    group1 = 241 # index 101
    interval = 300 #index 111


    self.node.set_config_param(4, sensitivity)
    self.node.set_config_param(3, timeout)
    self.node.set_config_param(8, 30) # broadcast rate sec
    self.node.set_config_param(64, scale, size=1)  # THIS BROKE THINGS
    self.node.set_config_param(101, group1)
    self.node.set_config_param(111, interval)
    self.node.set_config_param(5, 1)


    successful = True
    successful &= self.node.request_config_param(4) == sensitivity
    successful &= self.node.request_config_param(3) == timeout

    self._update_try_count += 1
    self._config_updated = successful

  def update_from_zwave(self, node: ZWaveNode = None, ignore_update=False, **kwargs):
    if node is None:
      return

    super().update_from_zwave(node, **kwargs)

    values = kwargs.get('values')
    if values is  None:
      return
    genre = values.genre
    if genre != 'User':
      return

    #self._state = get_kwargs_value(self._sensors, 'SENSOR', False)
    b = self._raw_values.get('burglar')
    print(b)
    if b:
      self._state = b.get('value') == 8
    else:
      self._state = False

    #self._state = self._raw_values.get('BURGLAR')




  def get_state(self, **kwargs):
    return self.state

  def get_motion(self, **kwargs):
    return MOTION_ACTIVE if self.state else MOTION_INACTIVE


  @property
  def state(self):
    self._state =  self._sensors.get('sensor')
    return self._state
