import unittest

from modules.entities.apk import MarketsSet


class MarketsHolderTest(unittest.TestCase):

    def test_str(self):
        set_str = str(MarketsSet('one|two|three'))
        self.assertTrue(set_str == 'one|two|three' or set_str == 'one|three|two'
                        or set_str == 'three|one|two' or set_str == 'three|two|one'
                        or set_str == 'two|three|one' or set_str == 'two|one|three')


if __name__ == '__main__':
    unittest.main()
