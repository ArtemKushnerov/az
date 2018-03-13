import unittest

from modules.entities.apk import Apk
from modules.services.url_constructor import UrlConstructor


class UrlConstructorTest(unittest.TestCase):

    def test_create_url(self):
        url = UrlConstructor(r'http:\\azoo.com\?key={}&sha={}', key='mykey').construct(Apk(sha256=123))
        self.assertEqual(url, r'http:\\azoo.com\?key=mykey&sha=123')
        url = UrlConstructor(r'http:\\azoo.com\?key={}&sha={}', key='mykey').construct(Apk(sha256=456))
        self.assertEqual(url, r'http:\\azoo.com\?key=mykey&sha=456')


if __name__ == '__main__':
    unittest.main()
