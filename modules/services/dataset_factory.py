import logging

from modules.entities.apk import Apk
from modules.entities.dataset import Dataset
from modules.services.apk_evaluator import ApkEvaluator


class DatasetFactory:
    def __init__(self, source, criteria, evaluator=ApkEvaluator()):
        self.source = source
        self.apk_evaluator = evaluator
        self.apk_evaluator.criteria = criteria

    def create_dataset(self, criteria):
        logging.info(f'CREATE INITIAL DATASET BY CRITERIA: {criteria}')

        dataset = Dataset()
        for apk in self.source:
            logging.debug(f'EVALUATE {apk.pkg_name}')
            if self.apk_evaluator.satisfies(apk):
                logging.debug(f'{str(apk)} SATISFIES CRITERIA' )
                dataset.add(apk)
        logging.info(f'DATASET HAS BEEN CREATED. {len(dataset)} APKS SATISFY CRITERIA')

        return dataset
