import unittest

from modules.exceptions import EmptyDatasetException
from modules.adownloader import RandomPicker
from modules.entities import Dataset, Apk


class RandomPickerTest(unittest.TestCase):

    def test_raise_exception_if_input_is_empty(self):
        with self.assertRaises(EmptyDatasetException):
            RandomPicker().get_random_subset(Dataset(), 4)

    def test_logs_if_input_dataset_size_less_then_requested_subset_size(self):
        with self.assertLogs(level='WARNING') as cm:
            input_dataset = Dataset(Apk('apk1'))
            subset = RandomPicker().get_random_subset(input_dataset, 4)
        self.assertTrue('Input dataset size less than requested random subset size, returning copy of input dataset' in cm.output[0])
        self.assertTrue(len(subset), len(input_dataset))

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
        expected_random_subset1 = Dataset(Apk('apk4'), Apk('apk3'), Apk('apk6'))
        self.assertEqual(random_subset1, expected_random_subset1)
        random_subset2 = picker.get_random_subset(initial_dataset, 3)
        expected_random_subset2 = Dataset(Apk('apk3'), Apk('apk5'), Apk('apk6'))
        self.assertEqual(random_subset2, expected_random_subset2)
        random_subset3 = picker.get_random_subset(initial_dataset, 3)
        expected_random_subset3 = Dataset(Apk('apk1'), Apk('apk4'), Apk('apk2'))
        self.assertEqual(random_subset3, expected_random_subset3)

if __name__ == '__main__':
    unittest.main()