import unittest

from modules.entities.apk import Apk
from modules.entities.criteria import Criteria
from modules.services.apk_evaluator import ApkEvaluator


class CriteriaTest(unittest.TestCase):

    def test_return_false_for_none(self):
        criteria = Criteria
        self.assertFalse(ApkEvaluator(criteria).satisfies(None))

    def test_dex_date(self):
        evaluator = ApkEvaluator(Criteria(dex_date_from='2016-3-3', dex_date_to='2016-3-5'))
        self.assertTrue(evaluator.satisfies_date(Apk(dex_date='2016-3-3 17:58:23')))
        self.assertTrue(evaluator.satisfies_date(Apk(dex_date='2016-3-4 2:30:00'), ))
        self.assertTrue(evaluator.satisfies_date(Apk(dex_date='2016-3-5 00:00:00')))
        self.assertFalse(evaluator.satisfies_date(Apk(dex_date='2016-3-2 17:58:07')))
        self.assertFalse(evaluator.satisfies_date(Apk(dex_date='2016-3-6 17:58:08')))

        evaluator = ApkEvaluator(Criteria(dex_date_from='2016-3-5', dex_date_to='2016-5-5'))
        self.assertTrue(evaluator.satisfies_date(Apk(dex_date='2016-3-7 17:58:00')))
        self.assertTrue(evaluator.satisfies_date(Apk(dex_date='2016-5-4 17:58:00')))
        self.assertFalse(evaluator.satisfies_date(Apk(dex_date='2016-2-13 17:58:00')))
        self.assertFalse(evaluator.satisfies_date(Apk()))

        evaluator = ApkEvaluator(Criteria(dex_date_from='2016-3-3'))
        self.assertTrue(evaluator.satisfies_date(Apk(dex_date='2016-4-3 17:58:00')))
        self.assertFalse(evaluator.satisfies_date(Apk(dex_date='2016-2-3 17:58:00')))

        evaluator = ApkEvaluator(Criteria(dex_date_to='2016-3-3'))
        self.assertFalse(evaluator.satisfies_date(Apk(dex_date='2016-4-3 17:58:00')))
        self.assertTrue(evaluator.satisfies_date(Apk(dex_date='2016-2-3 17:58:00')))

    def test_apk_size(self):
        evaluator = ApkEvaluator(Criteria(apk_size_from=10, apk_size_to=20))
        self.assertTrue(evaluator.satisfies_size(Apk(apk_size=15)))
        self.assertFalse(evaluator.satisfies_size(Apk(apk_size=5)))
        self.assertTrue(evaluator.satisfies_size(Apk(apk_size=20)))
        self.assertFalse(evaluator.satisfies_size(Apk()))

    def test_pkg_name(self):
        evaluator = ApkEvaluator(Criteria(pkg_name=['name1', 'name2']))
        self.assertTrue(evaluator.satisfies_name(Apk(pkg_name='name1')))
        self.assertTrue(evaluator.satisfies_name(Apk(pkg_name='name2')))
        self.assertFalse(evaluator.satisfies_name(Apk(pkg_name='name3')))
        self.assertFalse(evaluator.satisfies_name(Apk(pkg_name='name4')))
        self.assertFalse(evaluator.satisfies_name(Apk()))

    def test_vt_detection(self):
        evaluator = ApkEvaluator(Criteria(vt_detection_from=7, vt_detection_to=40))
        self.assertTrue(evaluator.satisfies_vt_detection(Apk(vt_detection=8)))
        self.assertTrue(evaluator.satisfies_vt_detection(Apk(vt_detection=12)))
        self.assertFalse(evaluator.satisfies_vt_detection(Apk(vt_detection=5)))
        self.assertFalse(evaluator.satisfies_vt_detection(Apk(vt_detection=100)))
        self.assertFalse(evaluator.satisfies_vt_detection(Apk()))

    def test_markets(self):
        evaluator = ApkEvaluator(Criteria(markets={'google.play.com', 'chinese.market'}))
        self.assertTrue(evaluator.satisfies_markets(Apk(markets='google.play.com')))
        self.assertTrue(evaluator.satisfies_markets(Apk(markets='chinese.market')))
        self.assertTrue(evaluator.satisfies_markets(Apk(markets='google.play.com|chinese.market')))
        self.assertFalse(evaluator.satisfies_markets(Apk(markets='another.chinese.market')))
        self.assertFalse(evaluator.satisfies_markets(Apk(markets='onemore.chinese.market')))
        self.assertFalse(evaluator.satisfies_markets(Apk()))

    def test_sha256(self):
        evaluator = ApkEvaluator(Criteria(sha256={'123', '456'}))
        self.assertTrue(evaluator.satisfies_sha256(Apk(sha256='123')))
        self.assertFalse(evaluator.satisfies_sha256(Apk(sha256='789')))
        self.assertTrue(evaluator.satisfies_sha256(Apk(sha256='456')))
        self.assertFalse(evaluator.satisfies_sha256(Apk(sha256='035')))
        self.assertFalse(evaluator.satisfies_sha256(Apk()))
        
    def test_sha1(self):
        evaluator = ApkEvaluator(Criteria(sha1={'123', '456'}))
        self.assertTrue(evaluator.satisfies_sha1(Apk(sha1='123')))
        self.assertFalse(evaluator.satisfies_sha1(Apk(sha1='789')))
        self.assertTrue(evaluator.satisfies_sha1(Apk(sha1='456')))
        self.assertFalse(evaluator.satisfies_sha1(Apk(sha1='035')))
        self.assertFalse(evaluator.satisfies_sha1(Apk()))
        
    def test_md5(self):
        evaluator = ApkEvaluator(Criteria(md5={'123', '456'}))
        self.assertTrue(evaluator.satisfies_md5(Apk(md5='123')))
        self.assertFalse(evaluator.satisfies_md5(Apk(md5='789')))
        self.assertTrue(evaluator.satisfies_md5(Apk(md5='456')))
        self.assertFalse(evaluator.satisfies_md5(Apk(md5='035')))
        self.assertFalse(evaluator.satisfies_md5(Apk()))

    def test_all(self):
        evaluator = ApkEvaluator(Criteria(dex_date_from='2016-3-3 00:00:01', dex_date_to='2016-3-5 23:59:59',
                                          apk_size_from=1, apk_size_to=4,
                                          pkg_name=['pkg1', 'pkg2'],
                                          vt_detection_from=1, vt_detection_to=5,
                                          markets={'market1', 'market2'},
                                          sha256={'adf', '789'}))
        self.assertTrue(evaluator.satisfies(Apk(dex_date='2016-3-4 17:58:00', apk_size=3, pkg_name='pkg1', vt_detection=3, markets='market1', sha256='adf')))
        self.assertTrue(evaluator.satisfies(Apk(dex_date='2016-3-3 17:58:00', apk_size=4, pkg_name='pkg2', vt_detection=4, markets='market1|market2', sha256='789')))
        self.assertFalse(evaluator.satisfies(Apk(dex_date='2016-3-3 17:58:00', apk_size=4, pkg_name='pkg2', vt_detection=4, markets='market1|market2')))
        self.assertFalse(evaluator.satisfies(Apk(dex_date='2016-3-4 17:58:00', apk_size=5, pkg_name='pkg1', vt_detection=3, markets='market1')))
        self.assertFalse(evaluator.satisfies(Apk(dex_date='2016-3-4 17:58:00', apk_size=3, pkg_name='pkg3', vt_detection=3, markets='market1')))
        self.assertFalse(evaluator.satisfies(Apk(dex_date='2016-3-4 17:58:00', apk_size=3, pkg_name='pkg1', vt_detection=0, markets='market1')))
        self.assertFalse(evaluator.satisfies(Apk(dex_date='2016-3-4 17:58:00', apk_size=3, pkg_name='pkg1', vt_detection=3, markets='market8')))
        self.assertFalse(evaluator.satisfies(Apk(dex_date='2016-3-4 17:58:00', apk_size=3, pkg_name='pkg1', vt_detection=3, markets='market8')))
        self.assertFalse(evaluator.satisfies(Apk()))


if __name__ == '__main__':
    unittest.main()
