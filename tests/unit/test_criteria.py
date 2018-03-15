import unittest

from dateutil.parser import parse

from modules.entities.criteria import Criteria


class CriteriaTest(unittest.TestCase):

    def test_initializes_from_dictionary(self):
        criteria_dict = {
            'dex_date': {'from': '2015-11-12', 'to': '2015-11-15'},
            'apk_size': {'from': '5', 'to': '8'},
            'markets': {'play.google.com', 'chinese.market'},
            'pkg_name': {'name1', 'name2'},
            'vt_detection': {'from': '3', 'to': '5'},
        }
        actual_criteria = Criteria.init_from_dict(criteria_dict)
        expected_criteria = Criteria(dex_date_from='2015-11-12', dex_date_to='2015-11-15', apk_size_from=5, apk_size_to=8, markets={'play.google.com', 'chinese.market'},
                                     pkg_name={'name1', 'name2'}, vt_detection_from=3, vt_detection_to=5)
        self.assertEqual(expected_criteria, actual_criteria)

    def test_not_crashes_if_partial_config(self):
        criteria_dict = {
            'apk_size': {'from': '5', 'to': '8'},
            'markets': {'play.google.com', 'chinese.market'},
        }
        actual_criteria = Criteria.init_from_dict(criteria_dict)
        expected_criteria = Criteria(apk_size_from=5, apk_size_to=8, markets={'play.google.com', 'chinese.market'})
        self.assertEqual(expected_criteria, actual_criteria)

        criteria_dict = {
            'apk_size': {'from': '5'},
        }
        actual_criteria = Criteria.init_from_dict(criteria_dict)
        expected_criteria = Criteria(apk_size_from=5)
        self.assertEqual(expected_criteria, actual_criteria)


if __name__ == '__main__':
    unittest.main()
