import unittest
from unittest import mock

from unittest import TestCase

from modules.adownloader import DatasetFactory, Source
from modules.entities.apk import Apk
from modules.entities.dataset import Dataset
from modules.services.apk_evaluator import ApkEvaluator


class DatasetFactoryTest(TestCase):

    def test_create_dataset_according_to_criteria(self):

        apks = [Apk(pkg_name='apk1'),Apk(pkg_name='apk2'),Apk(pkg_name='apk3')]
        source_mock = mock.create_autospec(Source)
        evaluator_mock = mock.create_autospec(ApkEvaluator)
        factory = DatasetFactory(source_mock, evaluator_mock)
        list()
        expected_dataset = Dataset(Apk(pkg_name='apk1'), Apk(pkg_name='apk3'))
        input_criteria = {}
        evaluator_mock.satisfies.side_effect = lambda apk, criteria: apk.pkg_name in ('apk1', 'apk3') and criteria == input_criteria
        source_mock.__iter__.side_effect = apks.__iter__
        actual_dataset = factory.create_dataset(input_criteria)
        self.assertEqual(expected_dataset, actual_dataset)
        self.assertEqual(evaluator_mock.satisfies.call_count, 3)


if __name__ == '__main__':
    unittest.main()
