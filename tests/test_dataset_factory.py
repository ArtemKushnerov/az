import random
import unittest
from unittest import mock

from unittest import TestCase

from modules.adownloader import DatasetFactory, Source
from modules.entities import Apk, Dataset
from modules.services import ApkEvaluator


class DatasetFactoryTest(TestCase):

    def test_create_dataset_according_to_criteria(self):
        source = Source(records=[{'pkg_name': 'apk1'},
                                 {'pkg_name': 'apk2'},
                                 {'pkg_name': 'apk3'}])
        evaluator_mock = mock.create_autospec(ApkEvaluator)
        factory = DatasetFactory(source, evaluator_mock)

        expected_dataset = Dataset([Apk('apk1'), Apk('apk3')])
        input_criteria = {}
        evaluator_mock.satisfies.side_effect = lambda apk, criteria: apk.pkg_name in ('apk1', 'apk3') and criteria == input_criteria
        actual_dataset = factory.create_dataset(input_criteria)
        self.assertEqual(expected_dataset, actual_dataset)
        self.assertEqual(evaluator_mock.satisfies.call_count, 3)

if __name__ == '__main__':
    unittest.main()
