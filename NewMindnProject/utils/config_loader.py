# utils/config_loader.py

import configparser


class ConfigLoader:
    def __init__(self, config_file='config/config.properties'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_property(self, key):
        for section in self.config.sections():
            if key in self.config[section]:
                return self.config[section][key]
        return None
