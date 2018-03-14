import logging.config
import sys

from modules.entities.source import Source
from modules.services.dataset_downloader import DatasetDownloader
from modules.services.dataset_factory import DatasetFactory
from modules.services.metadata_saver import MetadataSaver
from modules.services.random_picker import RandomPicker


def run(input_file, base_url, key, number, criteria, metadata, out_dir='azoo_dataset'):
    logging.info(f'START. APKS TO DOWNLOAD: {number}')
    source = None
    try:
        source = Source(input_file=input_file)

        dataset = DatasetFactory(source, criteria).create_dataset()
        random_subset = RandomPicker().get_random_subset(dataset, number)
        DatasetDownloader(dataset=random_subset, out_dir=out_dir, base_url=base_url, key=key).download()

        MetadataSaver(random_subset, out_dir).save(metadata)
    except KeyboardInterrupt:
        logging.info('Keyboard interrupt')
        sys.exit()
    finally:
        if source:
            source.input_file.close()

