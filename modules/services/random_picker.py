import logging
import random
import sys

from modules.entities.dataset.dataset import Dataset
from modules.enums import DownloadType


class RandomPicker:
    def __init__(self, seed=None):
        if seed is None:
            seed = random.randrange(sys.maxsize)
        random.seed(seed)
        logging.info(f'RANDOM SEED: {seed}')

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
