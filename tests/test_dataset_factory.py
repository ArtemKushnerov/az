import unittest
from unittest import TestCase

from modules.adownloader import DatasetFactory, Criteria, Source, Apk, Dataset


class DatasetFactoryTest(TestCase):

    def test_create_dataset_according_to_criteria(self):
        source = Source(records=[{'apk_size': 1, 'pkg_name': 'apk1', 'dex_date': '4/5/2016'},
                                      {'apk_size': 2, 'pkg_name': 'apk2'},
                                      {'apk_size': 1, 'pkg_name': 'apk3'}])
        factory = DatasetFactory(source)
        apk1 = Apk(pkg_name='apk1', apk_size=2, dex_date='4/5/2016')
        apk2 = Apk(pkg_name='apk2', apk_size=2)
        apk3 = Apk(pkg_name='apk3', apk_size=1)
        expected_dataset = Dataset([apk1, apk3])

        actual_dataset = factory.create_dataset(Criteria(apk_size={'from': 0, 'to': 1.5}))
        self.assertEqual(expected_dataset, actual_dataset)

        actual_dataset = factory.create_dataset(Criteria(apk_size={'from': 1.5, 'to': 2.5}))
        self.assertEqual(Dataset([apk2]), actual_dataset)

        actual_dataset = factory.create_dataset(Criteria(dex_date={'from': '3/5/2016', 'to': '6/5/2016'}))
        self.assertEqual(Dataset([apk1]), actual_dataset)


if __name__ == '__main__':
    unittest.main()
