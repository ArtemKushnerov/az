import unittest

from modules.entities import Apk
from modules.services import ApkEvaluator


class CriteriaTest(unittest.TestCase):

    def test_return_false_for_none(self):
        criteria = {}
        self.assertFalse(ApkEvaluator().satisfies(None, criteria))

    def test_dex_date(self):
        criteria = {'dex_date': {'from': '3/3/2016', 'to': '3/5/2016'}}
        self.assertTrue(ApkEvaluator().satisfies(Apk(dex_date='3/3/2016'), criteria))
        self.assertTrue(ApkEvaluator().satisfies(Apk(dex_date='3/4/2016'), criteria))
        self.assertTrue(ApkEvaluator().satisfies(Apk(dex_date='3/5/2016'), criteria))
        self.assertFalse(ApkEvaluator().satisfies(Apk(dex_date='3/2/2016'), criteria))
        self.assertFalse(ApkEvaluator().satisfies(Apk(dex_date='3/6/2016'), criteria))

        criteria = {'dex_date': {'from': '3/5/2016', 'to': '5/5/2016'}}
        self.assertTrue(ApkEvaluator().satisfies(Apk(dex_date='3/7/2016'), criteria))
        self.assertTrue(ApkEvaluator().satisfies(Apk(dex_date='5/4/2016'), criteria))
        self.assertFalse(ApkEvaluator().satisfies(Apk(dex_date='2/13/2016'), criteria))

    def test_apk_size(self):
        criteria = {'apk_size': {'from': 10, 'to': 20}}
        self.assertTrue(ApkEvaluator().satisfies(Apk(apk_size=15), criteria))


if __name__ == '__main__':
    unittest.main()
