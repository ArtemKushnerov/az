from modules.entities import Metadata, Source
from modules.services import DatasetFactory, RandomPicker, DatasetDownloader, MetadataSaver


def run(input_file, number, criteria, out_dir='azoo_dataset'):
    metadata = Metadata()
    source = Source(input_file)

    dataset = DatasetFactory(source).create_dataset(criteria)
    random_subset = RandomPicker().get_random_subset(dataset, number)
    DatasetDownloader(random_subset, out_dir, base_url, key).download()
    MetadataSaver(random_subset, out_dir).save(metadata)
