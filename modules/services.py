import logging
import os
import random
import shutil
import sys
import urllib.request

from dateutil.parser import parse

from modules.entities import Dataset, Apk
from modules.exceptions import EmptyDatasetException


class ApkEvaluator:
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


class UrlConstructor:
    def __init__(self, base_url='', key=''):
        self.base_url = base_url
        self.key = key

    def construct(self, apk):
        return self.base_url.format(self.key, apk.sha256)


class DatasetDownloader:
    def __init__(self, dataset, url_constructor, base_url='', key='', out_dir='azoo_dataset'):
        self.dataset = dataset
        self.out_dir = out_dir
        if not url_constructor:
            url_constructor = UrlConstructor(base_url, key)
        self.url_constructor = url_constructor

    def download(self):
        logging.info(f'DOWNLOADING {len(self.dataset)} APKS...')
        if not os.path.exists(self.out_dir):
            os.makedirs(self.out_dir)

        for apk in self.dataset:
            self.download_apk(apk)

    def download_apk(self, apk):
        apk_save_path = os.path.join(self.out_dir, apk.pkg_name)
        try:
            if os.path.exists(apk_save_path):
                logging.debug(f'{apk.pkg_name} is already downloaded')
                return
            logging.debug(f'Downloading {apk.pkg_name}... ')
            apk_url = self.url_constructor.construct(apk)
            with urllib.request.urlopen(apk_url) as response, open(apk_save_path, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
        except:
            # todo handle exception better
            logging.error(f'Unexpected error while downloading {apk.pkg_name}: {sys.exc_info()[1]}')


class MetadataSaver:
    def __init__(self, dataset, out_dir):
        pass

    def save(self, metadata):
        pass
