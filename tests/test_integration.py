import cProfile
import unittest
from pstats import Stats
from dateutil.parser import parse

from modules import adownloader


class IntegrationTest(unittest.TestCase):
    pass
    # def setUp(self):
    #     """init each test"""
    #     self.pr = cProfile.Profile()
    #     self.pr.enable()
    #     print("\n<<<---")


    # def test(self):
    #     criteria = {
    #         'dex_date': {'from': parse('11-12-2015')},
    #         'markets': {'play.google.com'},
    #     }
    #     metadata = ['sha256', 'pkg_name', 'apk_size', 'dex_date', 'markets']
    #     adownloader.run(r'c:\SaToSS\latest.csv', 'https://androzoo.uni.lu/api/download?apikey={0}&sha256={01}', '***REMOVED***', 5, criteria, metadata, out_dir='azoo_dataset')

    # def tearDown(self):
    #     """finish any test"""
    #     p = Stats(self.pr)
    #     p.strip_dirs()
    #     p.sort_stats('cumtime')
    #     p.print_stats()
    #     print( "\n--->>>")


if __name__ == '__main__':
    unittest.main()