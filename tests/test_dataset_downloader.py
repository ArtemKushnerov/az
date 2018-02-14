import unittest
from unittest import mock

from modules.entities import Dataset, Apk
from modules.services import DatasetDownloader, UrlConstructor


class DatasetDownloaderTest(unittest.TestCase):

    def setUp(self):
        self.apk = Apk(sha256='1234', pkg_name='apk1')
        self.apk2 = Apk(sha256='5678', pkg_name='apk2')
        self.dataset = Dataset(self.apk, self.apk2)
        self.constructor_mock = mock.create_autospec(UrlConstructor)
        self.constructor_mock.construct.side_effect = lambda apk: apk.sha256  # use sha256 of apk as download url, just for a test
        self.dataset_downloader = DatasetDownloader(self.dataset,url_constructor=self.constructor_mock, out_dir='out')

    @mock.patch('urllib.request')
    @mock.patch("modules.services.open")
    @mock.patch("modules.services.shutil")
    @mock.patch("modules.services.os")
    def test_checks_if_out_dir_exists(self, os_mock, mock_shutil, mock_open, mock_request):
        self.dataset_downloader.download()
        os_mock.path.exists.assert_any_call('out')

        os_mock.path.exists.return_value = False
        self.dataset_downloader.download()
        os_mock.path.exists.assert_any_call('out')
        os_mock.makedirs.assert_called_with('out')

    @mock.patch("modules.services.os.makedirs")
    @mock.patch('urllib.request')
    @mock.patch("modules.services.open")
    @mock.patch("modules.services.shutil")
    def test_downloads_apks(self, shutil_mock, open_mock, request_mock, os_mock):
        self.dataset_downloader.download()

        self.assertEqual(self.constructor_mock.construct.call_args_list, [mock.call(self.apk), mock.call(self.apk2)])
        self.constructor_mock.reset_mock()
        self.assertEqual(request_mock.urlopen.call_args_list, [mock.call(self.apk.sha256), mock.call(self.apk2.sha256)])
        self.assertEqual(open_mock.call_args_list, [mock.call(r'out\apk1', 'wb'), mock.call(r'out\apk2', 'wb')])
        self.assertEqual(shutil_mock.copyfileobj.call_count, 2)


if __name__ == '__main__':
    unittest.main()
