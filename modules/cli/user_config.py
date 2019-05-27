from pathlib import Path

import os

from modules.exceptions import AbsentUserConfigException


class UserConfig:
    CONFIG_FILE_NAME = '.az'
    API_KEY_CONFIG_NAME = 'key'
    INPUT_FILE_CONFIG_NAME = 'input_file'
    SEPARATOR = '='

    def __init__(self, key_arg, in_arg):
        self.key, self.in_file, self._key_local, self._in_local, self._key_global, self._in_global = None, None, None, None, None, None
        self._key_arg = key_arg
        self._in_arg = in_arg
        self._err_msg = ''
        self._read_local_config()
        self._read_global_config()
        self._assign_key()
        self._assign_in_file()

        if self._err_msg:
            raise AbsentUserConfigException(self._err_msg)

    def _read_local_config(self):
        self._key_local, self._in_local = self._read_user_config(self.CONFIG_FILE_NAME)

    def _read_global_config(self):
        home_dir = Path.home()
        global_config = os.path.join(home_dir, self.CONFIG_FILE_NAME)
        self._key_global, self._in_global = self._read_user_config(global_config)

    def _read_user_config(self, path):
        api_key, input_file = None, None
        if os.path.exists(path):
            with open(path) as config:
                for line in config:
                    if self.SEPARATOR in line:
                        key, value = line.split(self.SEPARATOR)
                        if key == self.API_KEY_CONFIG_NAME:
                            api_key = value.strip()
                        elif key == self.INPUT_FILE_CONFIG_NAME:
                            input_file = value.strip()
        return api_key, input_file

    def _assign_key(self):
        self.key = self._key_arg or self._key_local or self._key_global
        if not self.key:
            self._err_msg += "Key is not defined. Please, define  configuration parameter 'key' in local or global config"

    def _assign_in_file(self):
        self.in_file = self._in_arg or self._in_local or self._in_global
        if not self.in_file:
            self._err_msg += 'Input file is not defined.'


