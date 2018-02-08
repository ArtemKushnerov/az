from modules.entities import Dataset, Apk, Criteria, Metadata, Source


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
    def get_random_subset(self, dataset, size):
        pass


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
