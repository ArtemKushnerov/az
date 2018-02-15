import logging

import sys

from modules.entities import Source
from modules.services import DatasetFactory, RandomPicker, DatasetDownloader, MetadataSaver


def run(input_file, base_url, key, number, criteria, out_dir='azoo_dataset'):
    try:
        source = Source(input_file=input_file)

        dataset = DatasetFactory(source).create_dataset(criteria)
        random_subset = RandomPicker().get_random_subset(dataset, number)
        DatasetDownloader(dataset=random_subset, out_dir=out_dir, base_url=base_url, key=key).download()

        metadata = ['sha256', 'pkg_name', 'apk_size', 'dex_date']
        MetadataSaver(random_subset, out_dir).save(metadata)
    except KeyboardInterrupt as ki:
        logging.info('Keyboard interrupt')
        sys.exit()
