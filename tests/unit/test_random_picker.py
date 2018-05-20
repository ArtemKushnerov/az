import unittest

from modules.entities.apk import Apk
from modules.entities.dataset.dataset import Dataset
from modules.az import RandomPicker


class RandomPickerTest(unittest.TestCase):

    def test_returns_whole_dataset_if_dataset_size_less_then_requested_size(self):
        input_dataset = Dataset(Apk('apk1'), Apk('apk2'))
        subset = RandomPicker().get_random_subset(input_dataset, 4)
        self.assertEqual(subset, input_dataset)

    def test_return_dataset_of_size_n(self):
        subset = RandomPicker().get_random_subset(Dataset(Apk('apk1'), Apk('apk2'), Apk('apk3')), 2)
        self.assertEqual(len(subset), 2)
        subset = RandomPicker().get_random_subset(Dataset(Apk('apk1'), Apk('apk2'), Apk('apk3'), Apk('apk4')), 3)
        self.assertEqual(len(subset), 3)

    def test_return_subset_of_dataset(self):
        initial_dataset = Dataset(Apk('apk1'), Apk('apk2'), Apk('apk3'), Apk('apk4'), Apk('apk5'), Apk('apk6'))
        subset = RandomPicker().get_random_subset(initial_dataset, 4)
        self.assertTrue(initial_dataset.contains(subset))
        subset = RandomPicker().get_random_subset(initial_dataset, 2)
        self.assertTrue(initial_dataset.contains(subset))
        self.assertEqual(len(subset), 2)

    def test_return_random_subset(self):
        initial_dataset = Dataset(Apk('apk1'), Apk('apk2'), Apk('apk3'), Apk('apk4'), Apk('apk5'), Apk('apk6'))
        picker = RandomPicker(seed=12)
        random_subset1 = picker.get_random_subset(initial_dataset, 3)
        expected_random_subset1 = Dataset(Apk('apk3'), Apk('apk4'), Apk('apk1'))
        self.assertEqual(random_subset1, expected_random_subset1)
        random_subset2 = picker.get_random_subset(initial_dataset, 3)
        expected_random_subset2 = Dataset(Apk('apk2'), Apk('apk5'), Apk('apk6'))
        self.assertEqual(random_subset2, expected_random_subset2)
        random_subset3 = picker.get_random_subset(initial_dataset, 3)
        expected_random_subset3 = Dataset(Apk('apk1'), Apk('apk4'), Apk('apk3'))
        self.assertEqual(random_subset3, expected_random_subset3)


if __name__ == '__main__':
    unittest.main()