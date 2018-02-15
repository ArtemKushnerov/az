from modules.entities import Source
from modules.services import DatasetFactory, RandomPicker, DatasetDownloader, MetadataSaver


def run(input_file, base_url, key, number, criteria, out_dir='azoo_dataset'):
    source = Source(input_file)

    dataset = DatasetFactory(source).create_dataset(criteria)
    random_subset = RandomPicker().get_random_subset(dataset, number)
    DatasetDownloader(random_subset, out_dir, base_url, key).download()

    metadata = ['pkg_name', 'apk_size', 'dex_date']
    MetadataSaver(random_subset, out_dir).save(metadata)
