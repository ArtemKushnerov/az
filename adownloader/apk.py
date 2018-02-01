import os
from datetime import datetime

from conf import config

from Experiment.modules.entities.dataset import Type


class Apk:
    processed_apks = None

    android6_release_date = datetime(2015, 10, 5).date()
    android7_release_date = datetime(2016, 8, 22).date()

    def __init__(self, name, sha256, update_date, vt_detection, markets):
        self.name = name
        self.sha256 = sha256
        self.update_date = update_date
        self.target_api_level = 1
        self.vt_detection = vt_detection
        self.url = 'https://androzoo.uni.lu/api/download?apikey={0}&sha256={01}'.format(config.api_key, sha256)
        self.path_on_disk = config.apk_dir + '/' + name
        self.path_on_disk_decompiled = config.decompiled_apks_dir + '/' + name
        self.is_malware = vt_detection > 0
        self.updated_after_release = update_date > self.android6_release_date
        self.permissions = set()
        self.uses_runtime_permissions = False
        self.markets = markets
        if self.vt_detection > 0:
            self.type = Type.MALICIOUS
        else:
            self.type = Type.BENIGN

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return f'{self.name}, {self.markets}, {self.vt_detection}'

    def is_on_disk(self):
        return os.path.isfile(self.path_on_disk)
