import shutil
import unittest

import os

from modules import adownloader
from modules.entities.criteria import Criteria


class IntegrationTest(unittest.TestCase):

    def setUp(self):
        if os.path.exists('azoo_dataset'):
            shutil.rmtree('azoo_dataset')

    def test_full_scenario(self):
        config = {
            'dex_date': {'from': '2015-12-11'},
            'markets': {'play.google.com'},
        }
        metadata = ['sha256', 'pkg_name', 'apk_size', 'dex_date', 'markets']
        input_file = r'latest_first50.csv'
        base_url = 'https://androzoo.uni.lu/api/download?apikey={0}&sha256={01}'
        api_key = '***REMOVED***'
        apk_number = 5
        criteria = Criteria.init_from_dict(config)
        adownloader.run(input_file, base_url, api_key,
                        apk_number, criteria, metadata, out_dir='azoo_dataset')


if __name__ == '__main__':
    unittest.main()
