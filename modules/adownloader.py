import logging
import random

from modules.entities import Dataset, Apk, Criteria, Metadata, Source
from modules.exceptions import EmptyDatasetException


class DatasetFactory:
    def __init__(self, source):
        self.source = source

    def create_dataset(self, criteria):
        dataset = Dataset()
        for record in self.source:
            apk = Apk(**record)
            if apk.satisfies(criteria):
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


def run(input_file, number, dex_date=None, apk_size=None, pkg_name=None, vt_detection=None, markets=None, out_dir='azoo_dataset'):
    criteria = Criteria(dex_date, apk_size, pkg_name, vt_detection, markets)
    metadata = Metadata()
    source = Source(input_file)

    dataset = DatasetFactory(source).create_dataset(criteria)
    dataset = RandomPicker().get_random_subset(dataset, number)
    DatasetDownloader(dataset, out_dir).download()
    MetadataSaver(dataset, out_dir).save(metadata)
