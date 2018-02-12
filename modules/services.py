from modules.entities import Dataset, Apk


class ApkEvaluator:
    def __init__(self, ):
        pass

    def satisfies(self, apk, criteria):
        pass


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
