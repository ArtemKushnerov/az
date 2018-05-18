import random

from modules.entities.dataset.dataset import Dataset
from modules.enums import DownloadType


class RandomPicker:
    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)

    def get_random_subset(self, input_dataset, requested_size):
        result = []
        for num, apk in enumerate(input_dataset, 1):
            if requested_size is DownloadType.ALL or len(result) < requested_size:
                result.append(apk)
            else:
                s = int(random.random() * num)
                if s < requested_size:
                    result[s] = apk
        return Dataset(*result)
