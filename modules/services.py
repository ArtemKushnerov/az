import logging
import random

from dateutil.parser import parse

from modules.entities import Dataset, Apk
from modules.exceptions import EmptyDatasetException


class ApkEvaluator:
    def __init__(self, ):
        pass

    def satisfies(self, apk, criteria):
        if not apk:
            return False

        satisfies = True

        criteria_dex_date = criteria.get('dex_date')
        if criteria_dex_date:
            satisfies = satisfies and apk.dex_date and parse(criteria_dex_date.get('from')) <= apk.dex_date <= parse(criteria_dex_date.get('to'))

        criteria_apk_size = criteria.get('apk_size')
        if criteria_apk_size:
            satisfies = satisfies and apk.apk_size and criteria_apk_size.get('from') <= apk.apk_size <= criteria_apk_size.get('to')

        criteria_pkg_name = criteria.get('pkg_name')
        if criteria_pkg_name:
            satisfies = satisfies and apk.pkg_name in criteria_pkg_name

        criteria_vt_detection = criteria.get('vt_detection')
        if criteria_vt_detection:
            satisfies = satisfies and apk.vt_detection and criteria_vt_detection.get('from') <= apk.vt_detection <= criteria_vt_detection.get('to')

        criteria_markets = criteria.get('markets')
        if criteria_markets:
            satisfies = satisfies and apk.markets and set(criteria_markets).intersection(set(apk.markets))

        return satisfies


class DatasetFactory:
    def __init__(self, source, evaluator=ApkEvaluator()):
        self.source = source
        self.apk_evaluator = evaluator

    def create_dataset(self, criteria):
        dataset = Dataset()
        for record in self.source:
            apk = Apk(**record)
            if self.apk_evaluator.satisfies(apk, criteria):
                dataset.add(apk)
        return dataset


class RandomPicker:

    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)

    def get_random_subset(self, input_dataset, requested_size):
        if input_dataset.is_empty():
            raise EmptyDatasetException()
        if len(input_dataset) < requested_size:
            logging.warning('Input dataset size less than requested random subset size, returning copy of input dataset')
            return Dataset(*input_dataset.apks)
        unique_random_apks = set()
        subset_size = min(len(input_dataset), requested_size)
        while len(unique_random_apks) != subset_size:
            apk = random.choice(input_dataset.apks)
            unique_random_apks.add(apk)
        return Dataset(*unique_random_apks)


class DatasetDownloader:
    def __init__(self, dataset, out_dir):
        pass

    def download(self):
        pass


class MetadataSaver:
    def __init__(self, dataset, out_dir):
        pass

    def save(self, metadata):
        pass
