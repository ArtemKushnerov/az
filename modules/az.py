import logging.config
import sys

from modules.entities.dataset.filtered_dataset import FilteredDataset
from modules.entities.source import Source
from modules.services.dataset_downloader import DatasetDownloader
from modules.services.metadata_saver import MetadataSaver
from modules.services.random_picker import RandomPicker


def run(input_file, key, number, criteria, metadata, threads, out_dir='azoo_dataset', seed=None, ):
    logging.info(f'START. APKS TO DOWNLOAD: {str(number)}')
    source = None
    try:
        source = Source(input_file=input_file)

        dataset = FilteredDataset(source, criteria)
        random_subset = RandomPicker(seed=seed).get_random_subset(dataset, number)
        DatasetDownloader(dataset=random_subset, out_dir=out_dir, key=key, threads=threads).download()

        MetadataSaver(random_subset, out_dir).save(metadata)
    except KeyboardInterrupt:
        logging.info('Keyboard interrupt')
        sys.exit()
    finally:
        if source:
            source.input_file.close()

