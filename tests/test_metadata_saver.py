import unittest

import os

import shutil

from modules.entities.apk import Apk
from modules.entities.dataset import Dataset
from modules.services.metadata_saver import MetadataSaver


class MetadataSeverTest(unittest.TestCase):

    def setUp(self):
        if os.path.exists('out'):
            shutil.rmtree('out')

    def test_saves_metadata(self):
        dataset = Dataset(Apk(pkg_name='apk1', apk_size=8, dex_date='01-01-2001', markets='play'), Apk(pkg_name='apk2', apk_size=13, dex_date='01-03-2001', markets='play|china'))
        MetadataSaver(dataset=dataset, out_dir='out').save(['pkg_name', 'apk_size', 'dex_date'])
        self.assertTrue(os.path.exists(r'out\metadata.csv'))


if __name__ == '__main__':
    unittest.main()
