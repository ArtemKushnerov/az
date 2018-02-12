import logging
import random

from modules.entities import Dataset, Apk
from modules.exceptions import EmptyDatasetException
from dateutil.parser import parse


class ApkEvaluator:
    def __init__(self, ):
        pass

    def satisfies(self, apk, criteria):
        if apk is None:
            return False
        satisfies = True
        if criteria.get('dex_date') is not None:
            requested_date = criteria.get('dex_date')
            satisfies = satisfies and apk.dex_date is not None and parse(requested_date.get('from')) <= apk.dex_date <= parse(requested_date.get('to'))
        if criteria.get('apk_size') is not None:
            satisfies = satisfies and criteria.apk_size.get('from') < apk.apk_size < criteria.apk_size.get('to')
        # if criteria.pkg_name is not None:
        #     satisfies = satisfies and apk.pkg_name in criteria.pkg_name
        # if criteria.vt_detection is not None:
        #     satisfies = satisfies and criteria.vt_detection.get('from') < apk.vt_detection < criteria.vt_detection.get('to')
        # if criteria.markets is not None:
        #     satisfies = satisfies and criteria.markets.intersection(apk.markets)
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
