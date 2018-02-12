from modules.entities import Metadata, Source
from modules.services import DatasetFactory, RandomPicker, DatasetDownloader, MetadataSaver


def run(input_file, number, criteria, out_dir='azoo_dataset'):
    metadata = Metadata()
    source = Source(input_file)

    dataset = DatasetFactory(source).create_dataset(criteria)
    dataset = RandomPicker().get_random_subset(dataset, number)
    DatasetDownloader(dataset, out_dir).download()
    MetadataSaver(dataset, out_dir).save(metadata)
