from Firefly.const import (CONTACT_CLOSED, CONTACT_OPEN, EVENT_ACTION_OFF, EVENT_ACTION_ON, MOTION_ACTIVE,
                           MOTION_INACTIVE, NOT_PRESENT, PRESENT)

def metaDimmer(min=0, max=100, command=True, request=False, primary=False):
  meta = {
    'command': command,
    'request': request,
    'primary': primary,
    'title':   'dimmer',
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
    'title':   'siwtch',
    'context': 'Change switch.',
    'type':    'select',
    'options': {
      "On":  EVENT_ACTION_ON,
      "Off": EVENT_ACTION_OFF
    }
  }
  return meta


def metaPresence(command=True, request=True, primary=False):
  meta = {
    'command': command,
    'request': request,
    'primary': primary,
    'title':   'presence',
    'context': 'Set the presence of a device.',
    'type':    'select',
    'options': {
      "Present":     PRESENT,
      "Not Present": NOT_PRESENT
    }
  }
  return meta


def metaContact(command=False, request=True, primary=False):
  meta = {
    'command': command,
    'request': request,
    'primary': primary,
    'title':   'contact',
    'context': 'Contact state of the device.',
    'type':    'text',
    'options': {
      "Open":   CONTACT_OPEN,
      "Closed": CONTACT_CLOSED
    }
  }
  return meta


def metaMotion(command=False, request=True, primary=False):
  meta = {
    'command': command,
    'request': request,
    'primary': primary,
    'context': 'Motion state of the device.',
    'type':    'text',
    'options': {
      "Active":   MOTION_ACTIVE,
      "Inactive": MOTION_INACTIVE
    }
  }
  return meta
