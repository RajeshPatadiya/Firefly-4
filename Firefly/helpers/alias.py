from Firefly import logging
from Firefly.const import (ALIAS_FILE)
import json

class Alias(object):
  def __init__(self, alias_file=ALIAS_FILE):
    self._alias_file = alias_file
    self._aliases = {}

    self.read_file()

  def read_file(self):
    with open(self._alias_file) as file:
      self._aliases = json.load(file)

  def export_aliases(self):
    with open(self._alias_file, 'w') as file:
      json.dump(self.aliases, file, indent=4, sort_keys=True)

  def set_alias(self, device_id, alias):
    self.aliases[str(device_id)] = str(alias)

  def get_alias(self, device_id):
    if device_id in self.aliases.keys():
      return self.aliases[device_id]

    return device_id

  def get_device_id(self, alias):
    if alias in self.aliases.values():
      device_id_list = [a for a in self.aliases if self.aliases[a] == alias]
      if len(device_id_list) != 1:
        logging.error('More than one ff_id matching alias')
        return None
      return device_id_list[0]
    if alias in self.aliases.keys():
      logging.debug('Seems like device_id was given, not alias')
      return alias
    logging.error('Unknown error getting ff_id ID.')
    return None

  @property
  def aliases(self):
    return self._aliases