from configparser import ConfigParser
import os
from pathlib import Path
import constants as const
    
class ConfigController():

    def __init__(self):
        self.config = ConfigParser()
       
    def _check_config_path(self):
        config_file_path = os.path.join(Path(__file__).resolve().parents[0], const.CONFIG_FILE_NAME)
        found_files = self.config.read(config_file_path)
        if not found_files:
            raise ValueError("No config file found.")

    def _validate(self):
        required_values = const.DICT_FOR_VALIDATION

        for section, keys in required_values.items():
            if section not in self.config:
                raise Exception('Missing section %s in the config file' % section)

            for key, values in keys.items():
                if key not in self.config[section] or self.config[section][key] == '':
                    raise Exception(('Missing value for %s under section %s in ' + 'the config file') % (key, section))

                if values:
                    if self.config[section][key] not in values:
                        raise Exception(('Invalid value for %s under section %s in ' + 'the config file') % (key, section))
        