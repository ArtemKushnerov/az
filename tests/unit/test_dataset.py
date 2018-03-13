import unittest

from modules.entities.apk import Apk
from modules.entities.dataset import Dataset


class DatasetTest(unittest.TestCase):

    def setUp(self):
        self.dataset = Dataset(Apk('apk1'), Apk('apk2'), Apk('apk3'), Apk('apk4'), Apk('apk5'))

    def test_equals_reflective(self):
        self.assertEqual(self.dataset, self.dataset)
        self.assertEqual(hash(self.dataset), hash(self.dataset))

    def test_not_equals_null(self):
        self.assertNotEqual(self.dataset, None)

    def test_equals(self):
        self.assertEqual(Dataset(), Dataset())
        dataset2 = Dataset(Apk('apk1'), Apk('apk2'), Apk('apk3'), Apk('apk4'), Apk('apk5'))
        self.assertEqual(self.dataset, dataset2)
        self.assertEqual(hash(self.dataset), hash(dataset2))
        dataset2.add(Apk('apk6'))
        self.assertNotEqual(hash(self.dataset), hash(dataset2))


if __name__ == '__main__':
    unittest.main()
