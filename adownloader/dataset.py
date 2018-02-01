import os
from collections import defaultdict
from enum import Enum, auto

from conf import config


class Type(Enum):
    MALICIOUS = auto()
    BENIGN = auto()
    MIXED = auto()


class Dataset:
    def __init__(self, dataset_type=Type.MIXED):
        self.apks = set()
        self.higher_than_23_count = 0
        self.api_level_to_apk_num_dict = defaultdict(int)
        self.not_found_platform_permissions = defaultdict(int)
        self.not_found_custom_permissions = defaultdict(int)
        self.dataset_type = dataset_type

        self.results_path = os.path.join(config.results_path, self.get_type(), config.results_file)
        self.save_path = os.path.join(config.results_path, self.get_type(), config.dataset_save_path_file)
        self.not_found_permissions_path = os.path.join(config.results_path, self.get_type(), config.not_found_permissions_file)
        self.api_level_distribution_bar_chart_save_path = os.path.join(
            config.results_path, self.get_type(), config.target_api_level_distribution_file)
        self.estimated_api_level_distribution_bar_chart_save_path = os.path.join(
            config.results_path, self.get_type(), config.estimated_api_level_distribution_file)

    def __iter__(self):
        return iter(self.apks)

    def add(self, apk):
        duplicate = apk in self.apks
        if not duplicate:
            self.apks.add(apk)
        return duplicate

    def get_size(self):
        return len(self.apks)

    def get_api_level_distribution(self):
        if not self.api_level_to_apk_num_dict:
            for apk in self.apks:
                self.api_level_to_apk_num_dict[apk.target_api_level] += 1
        return self.api_level_to_apk_num_dict

    def get_estimated_distribution_for_undefined(self):
        api_level_1_subset = self.get_subset_with_api_level(1)
        distribution = defaultdict(int)
        for apk in api_level_1_subset:
            lowest_api = 1
            highest_api = 25
            for permission in apk.permissions:
                introduced_in = permission.introduced_in
                latest_api_present_in = permission.latest_api_present_in
                if introduced_in > lowest_api:
                    lowest_api = introduced_in
                if latest_api_present_in < highest_api:
                    highest_api = latest_api_present_in
            distribution['{}-{}'.format(lowest_api, highest_api)] += 1
        return distribution

    def get_higher_than_23_count(self):
        api_level_dict = self.get_api_level_distribution()
        for api_level, num_of_apks in api_level_dict.items():
            if api_level >= 23:
                self.higher_than_23_count += num_of_apks
        return self.higher_than_23_count

    def get_benign_subset(self):
        benign = Dataset(dataset_type=Type.BENIGN)
        for apk in self.apks:
            if not apk.is_malware:
                benign.add(apk)
        return benign

    def get_malicious_subset(self):
        malicious = Dataset(dataset_type=Type.MALICIOUS)
        for apk in self.apks:
            if apk.is_malware:
                malicious.add(apk)
        return malicious

    def get_subset_with_api_level(self, api_level):
        subset = Dataset(self.dataset_type)
        for apk in self.apks:
            if apk.target_api_level == api_level:
                subset.add(apk)
        return subset

    def get_runtime_to_installtime_ratio(self):
        uses_runtime_num = 0
        for apk in self.apks:
            if apk.uses_runtime_permissions:
                uses_runtime_num += 1
        return uses_runtime_num, self.get_size() - uses_runtime_num

    def get_type(self):
        return self.dataset_type.name.lower()









