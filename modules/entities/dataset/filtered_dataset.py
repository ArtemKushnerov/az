import logging

from modules.entities.entity import Entity
from modules.services.apk_evaluator import ApkEvaluator


class FilteredDataset(Entity):
    def __init__(self, source=None, criteria=None):
        self.source = source
        self.criteria = criteria
        self.apk_evaluator = ApkEvaluator(criteria)
        self.length = 0
        logging.info(f'CREATE DATASET BY CRITERIA: {self.apk_evaluator.criteria}')

    def _key(self):
        return self.criteria

    def __iter__(self):
        return self

    def __next__(self):
        try:
            apk = next(self.source)
            logging.debug(f'EVALUATE {apk.pkg_name}')
            while not self.apk_evaluator.satisfies(apk):
                logging.debug(f'EVALUATE {apk.pkg_name}')
                apk = next(self.source)
            self.length += 1
            return apk
        except StopIteration:
            logging.info(f'DATASET HAS BEEN CREATED. {self.length} APKS SATISFY CRITERIA')
            raise StopIteration
