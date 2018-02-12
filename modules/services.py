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
