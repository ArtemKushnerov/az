from pathlib import Path

import os

from modules.exceptions import AbsentUserConfigException, NotDefinedConfigValue


class UserConfig:
    API_KEY_CONFIG_NAME = 'key'
    INPUT_FILE_CONFIG_NAME = 'input_file'

    def __init__(self):
        self.key, self.input_file = self.read_user_config()
        if not self.key:
            raise NotDefinedConfigValue('Api key is not defined')
        if not self.input_file:
            raise NotDefinedConfigValue('Input file is not defined')

    def read_user_config(self):
        api_key, input_file = None, None
        user_config = self.get_user_config()
        if not os.path.exists(user_config):
            raise AbsentUserConfigException()
        with open(user_config) as config:
            for line in config:
                key, value = line.split('=')
                if key == self.API_KEY_CONFIG_NAME:
                    api_key = value.strip()
                elif key == self.INPUT_FILE_CONFIG_NAME:
                    input_file = value.strip()
            return api_key, input_file

    @staticmethod
    def get_user_config():
        if os.path.exists('.az'):
            return '.az'
        home_dir = Path.home()
        return os.path.join(home_dir, '.az')
