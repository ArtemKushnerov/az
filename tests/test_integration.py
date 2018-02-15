import cProfile
import unittest
from pstats import Stats

from modules import adownloader


class IntegrationTest(unittest.TestCase):
    def setUp(self):
        """init each test"""
        self.pr = cProfile.Profile()
        self.pr.enable()
        print("\n<<<---")


    def test(self):
        criteria = {
            # mandatory
            'number': 10,
            # optional, comment out those you don't need
            'dex_date': {'from': '01-01-2014', 'to': '01-31-2014'},
            # 'apk_size': {'from': 1, 'to': 4},
            # 'pkg_name': ['pkg1'],
            # 'vt_detection': {'from': 0, 'to': 5},
            'markets': ['play.google.com'],
        }

        adownloader.run(r'resources\first_million.csv', 'https://androzoo.uni.lu/api/download?apikey={0}&sha256={01}', '***REMOVED***', 10, criteria, out_dir='azoo_dataset')

    def tearDown(self):
        """finish any test"""
        p = Stats(self.pr)
        p.strip_dirs()
        p.sort_stats('cumtime')
        p.print_stats()
        print( "\n--->>>")


if __name__ == '__main__':
    unittest.main()