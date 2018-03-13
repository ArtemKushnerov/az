import unittest

from dateutil.parser import parse

from modules.entities.apk import Apk
from modules.services.apk_evaluator import ApkEvaluator


class CriteriaTest(unittest.TestCase):

    def test_return_false_for_none(self):
        criteria = {}
        self.assertFalse(ApkEvaluator().satisfies(None, criteria))

    def test_dex_date(self):
        criteria = {'dex_date': {'from': parse('2016-3-3'), 'to': parse('2016-3-5')}}
        self.assertTrue(ApkEvaluator().satisfies_date(Apk(dex_date='2016-3-3 17:58:23'), criteria))
        self.assertTrue(ApkEvaluator().satisfies_date(Apk(dex_date='2016-3-4 2:30:00'), criteria))
        self.assertTrue(ApkEvaluator().satisfies_date(Apk(dex_date='2016-3-5 00:00:00'), criteria))
        self.assertFalse(ApkEvaluator().satisfies_date(Apk(dex_date='2016-3-2 17:58:07'), criteria))
        self.assertFalse(ApkEvaluator().satisfies_date(Apk(dex_date='2016-3-6 17:58:08'), criteria))

        criteria = {'dex_date': {'from': parse('2016-3-5'), 'to': parse('2016-5-5')}}
        self.assertTrue(ApkEvaluator().satisfies_date(Apk(dex_date='2016-3-7 17:58:00'), criteria))
        self.assertTrue(ApkEvaluator().satisfies_date(Apk(dex_date='2016-5-4 17:58:00'), criteria))
        self.assertFalse(ApkEvaluator().satisfies_date(Apk(dex_date='2016-2-13 17:58:00'), criteria))
        self.assertFalse(ApkEvaluator().satisfies_date(Apk(), criteria))

        criteria = {'dex_date': {'from': parse('2016-3-3')}}
        self.assertTrue(ApkEvaluator().satisfies_date(Apk(dex_date='2016-4-3 17:58:00'), criteria))
        self.assertFalse(ApkEvaluator().satisfies_date(Apk(dex_date='2016-2-3 17:58:00'), criteria))

        criteria = {'dex_date': {'to': parse('2016-3-3')}}
        self.assertFalse(ApkEvaluator().satisfies_date(Apk(dex_date='2016-4-3 17:58:00'), criteria))
        self.assertTrue(ApkEvaluator().satisfies_date(Apk(dex_date='2016-2-3 17:58:00'), criteria))

    def test_apk_size(self):
        criteria = {'apk_size': {'from': 10, 'to': 20}}
        self.assertTrue(ApkEvaluator().satisfies_size(Apk(apk_size=15), criteria))
        self.assertFalse(ApkEvaluator().satisfies_size(Apk(apk_size=5), criteria))
        self.assertTrue(ApkEvaluator().satisfies_size(Apk(apk_size=20), criteria))
        self.assertFalse(ApkEvaluator().satisfies_size(Apk(), criteria))

    def test_pkg_name(self):
        criteria = {'pkg_name': ['name1', 'name2']}
        self.assertTrue(ApkEvaluator().satisfies_name(Apk(pkg_name='name1'), criteria))
        self.assertTrue(ApkEvaluator().satisfies_name(Apk(pkg_name='name2'), criteria))
        self.assertFalse(ApkEvaluator().satisfies_name(Apk(pkg_name='name3'), criteria))
        self.assertFalse(ApkEvaluator().satisfies_name(Apk(pkg_name='name4'), criteria))
        self.assertFalse(ApkEvaluator().satisfies_name(Apk(), criteria))

    def test_vt_detection(self):
        criteria = {'vt_detection': {'from': 7, 'to': 40}}
        self.assertTrue(ApkEvaluator().satisfies_vt_detection(Apk(vt_detection=8), criteria))
        self.assertTrue(ApkEvaluator().satisfies_vt_detection(Apk(vt_detection=12), criteria))
        self.assertFalse(ApkEvaluator().satisfies_vt_detection(Apk(vt_detection=5), criteria))
        self.assertFalse(ApkEvaluator().satisfies_vt_detection(Apk(vt_detection=100), criteria))
        self.assertFalse(ApkEvaluator().satisfies_vt_detection(Apk(), criteria))

    def test_markets(self):
        criteria = {'markets': {'google.play.com', 'chinese.market'}}
        self.assertTrue(ApkEvaluator().satisfies_markets(Apk(markets='google.play.com'), criteria))
        self.assertTrue(ApkEvaluator().satisfies_markets(Apk(markets='chinese.market'), criteria))
        self.assertTrue(ApkEvaluator().satisfies_markets(Apk(markets='google.play.com|chinese.market'), criteria))
        self.assertFalse(ApkEvaluator().satisfies_markets(Apk(markets='another.chinese.market'), criteria))
        self.assertFalse(ApkEvaluator().satisfies_markets(Apk(markets='onemore.chinese.market'), criteria))
        self.assertFalse(ApkEvaluator().satisfies_markets(Apk(), criteria))

    def test_all(self):
        criteria = {'dex_date': {'from': parse('2016-3-3 00:00:01'), 'to': parse(' 2016-3-5 23:59:59')},
                    'apk_size': {'from': 1, 'to': 4},
                    'pkg_name': ['pkg1', 'pkg2'],
                    'vt_detection': {'from': 1, 'to': 5},
                    'markets': {'market1', 'market2'}}
        self.assertTrue(ApkEvaluator().satisfies(Apk(dex_date='2016-3-4 17:58:00', apk_size=3, pkg_name='pkg1', vt_detection=3, markets='market1'), criteria))
        self.assertTrue(ApkEvaluator().satisfies(Apk(dex_date='2016-3-3 17:58:00', apk_size=4, pkg_name='pkg2', vt_detection=4, markets='market1|market2'), criteria))
        self.assertFalse(ApkEvaluator().satisfies(Apk(dex_date='2016-3-4 17:58:00', apk_size=5, pkg_name='pkg1', vt_detection=3, markets='market1'), criteria))
        self.assertFalse(ApkEvaluator().satisfies(Apk(dex_date='2016-3-4 17:58:00', apk_size=3, pkg_name='pkg3', vt_detection=3, markets='market1'), criteria))
        self.assertFalse(ApkEvaluator().satisfies(Apk(dex_date='2016-3-4 17:58:00', apk_size=3, pkg_name='pkg1', vt_detection=0, markets='market1'), criteria))
        self.assertFalse(ApkEvaluator().satisfies(Apk(dex_date='2016-3-4 17:58:00', apk_size=3, pkg_name='pkg1', vt_detection=3, markets='market8'), criteria))
        self.assertFalse(ApkEvaluator().satisfies(Apk(dex_date='2016-3-4 17:58:00', apk_size=3, pkg_name='pkg1', vt_detection=3, markets='market8'), criteria))
        self.assertFalse(ApkEvaluator().satisfies(Apk(), criteria))


if __name__ == '__main__':
    unittest.main()
