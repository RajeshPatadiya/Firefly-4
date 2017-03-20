from Firefly.const import (STATE_ON, STATE_OFF, PRESENT, NOT_PRESENT)


def metaDimmer(min=0, max=100, command=True, request=False, primary=False):
  meta = {
    'command': command,
    'request': request,
    'primary': primary,
    'context': 'Change dimmer level.',
    'type':    'number',
    'options': {
      'min': min,
      'max': max
    }
  }
  return meta


def metaSwitch(command=True, request=True, primary=False):
  meta = {
    'command': command,
    'request': request,
    'primary': primary,
    'context': 'Change dimmer level.',
    'type':    'boolean',
    'options': {
      "On":  STATE_ON,
      "Off": STATE_OFF
    }
  }
  return meta

def metaPresence(command=True, request=True, primary=False):
  meta = {
    'command': command,
    'request': request,
    'primary': primary,
    'context': 'Set the presence of a device.',
    'type':    'boolean',
    'options': {
      "Present":  PRESENT,
      "Not Present": NOT_PRESENT
    }
  }
  return meta