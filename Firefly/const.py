

# #### SETTINGS ####
FIREFLY_CONFIG_SECTION = 'FIREFLY'
CONFIG_PORT = 'port'
CONFIG_DEFAULT_PORT = 6002
CONFIG_HOST = 'host'
CONFIG_DEFAULT_HOST = 'localhost'
CONFIG_FILE = 'dev_config/firefly.config'

ALIAS_FILE = 'dev_config/device_alias.json'
DEVICE_FILE = 'dev_config/devices.json'

# #### EVENT TYPES ####
EVENT_TYPE_ANY = 'ANY'
EVENT_TYPE_COMMAND = 'COMMAND'
EVENT_TYPE_UPDATE = 'UPDATE'
EVENT_TYPE_BROADCAST = 'BROADCAST'
EVENT_TYPE_REQUEST = 'REQUEST'

# #### EVENT ACTIONS ####
EVENT_ACTION_ANY = 'ANY'
EVENT_ACTION_ON = 'ON'
EVENT_ACTION_OFF = 'OFF'
EVENT_ACTION_ACTIVE = 'ACTIVE'
EVENT_ACTION_INACTIVE = 'INACTIVE'
EVENT_ACTION_OPEN = 'OPEN'
EVENT_ACTION_CLOSE = 'CLOSE'



EVENT_DAWN = 'dawn'
EVENT_SUNRISE = 'sunrise'
EVENT_NOON = 'noon'
EVENT_SUNSET = 'sunset'
EVENT_DUSK = 'dusk'
DAY_EVENTS = [EVENT_DAWN, EVENT_SUNRISE, EVENT_NOON, EVENT_SUNSET, EVENT_DUSK]

# #### COMMAND ACTIONS ####
COMMAND_NOTIFY = 'NOTIFY'
COMMAND_SPEECH = 'SPEECH'
COMMAND_ROUTINE = 'ROUTINE'

ACTION_OFF = 'OFF'
ACTION_ON = 'ON'

# #### REQUESTS ####
STATE = 'STATE'
LEVEL = 'LEVEL'

STATE_OFF = 'OFF'
STATE_ON = 'ON'


# #### DEVICE TYPES ####
DEVICE_TYPE_SWITCH = 'SWITCH'
DEVICE_TYPE_DIMMER = 'DIMMER'
DEVICE_TYPE_COLOR_LIGHT = 'COLOR_LIGHT'
DEVICE_TYPE_THERMOSAT = 'THERMOSTAT'


SOURCE_LOCATION = 'LOCATION'


