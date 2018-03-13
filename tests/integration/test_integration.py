import unittest

from dateutil.parser import parse

from modules import adownloader


class IntegrationTest(unittest.TestCase):

    def test_full_scenario(self):
        criteria = {
            'dex_date': {'from': parse('11-12-2015')},
            'markets': {'play.google.com'},
        }
        metadata = ['sha256', 'pkg_name', 'apk_size', 'dex_date', 'markets']
        input_file = r'latest_first50.csv'
        base_url = 'https://androzoo.uni.lu/api/download?apikey={0}&sha256={01}'
        api_key = '***REMOVED***'
        apk_number = 5

        adownloader.run(input_file, base_url, api_key,
                        apk_number, criteria, metadata, out_dir='azoo_dataset')


if __name__ == '__main__':
    unittest.main()
