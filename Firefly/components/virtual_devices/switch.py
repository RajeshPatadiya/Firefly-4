from Firefly import logging
from Firefly.helpers.device_types.switch import Switch
from Firefly.const import SWITCH, AUTHOR

TITLE = 'Virtual Switch'

def Setup(firefly, package, **kwargs):
  logging.message('Entering %s setup' % TITLE)
  switch = VirtualSwitch(firefly, package, **kwargs)
  return firefly.install_component(switch)


class VirtualSwitch(Switch):
  def __init__(self, firefly, package, **kwargs):
    super().__init__(firefly, package, TITLE, AUTHOR, **kwargs)

  def set_on(self, **kwargs):
    self.update_values(switch='on')

  def set_off(self, **kwargs):
    self.update_values(switch='off')
