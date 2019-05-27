import unittest
from unittest import mock

from modules.entities.apk import Apk
from modules.entities.dataset.dataset import Dataset
from modules.services.dataset_downloader import DatasetDownloader
from modules.services.url_constructor import UrlConstructor


class DatasetDownloaderTest(unittest.TestCase):

    def setUp(self):
        self.apk = Apk(sha256='1234', pkg_name='apk1')
        self.apk2 = Apk(sha256='5678', pkg_name='apk2')
        self.dataset = Dataset(self.apk, self.apk2)
        self.constructor_mock = mock.create_autospec(UrlConstructor)
        self.constructor_mock.construct.side_effect = lambda apk:' https://'+apk.sha256  # use sha256 of apk as download url, just for a test
        self.dataset_downloader = DatasetDownloader(self.dataset, threads=4, url_constructor=self.constructor_mock, out_dir='out')

    @mock.patch('requests.get')
    @mock.patch("modules.services.dataset_downloader.open")
    @mock.patch("modules.services.dataset_downloader.os")
    def test_checks_if_out_dir_exists(self, os_mock, mock_open, mock_request):
        self.dataset_downloader.download()
        os_mock.path.exists.assert_any_call('out')

        os_mock.path.exists.return_value = False
        self.dataset_downloader.download()
        os_mock.path.exists.assert_any_call('out')
        os_mock.makedirs.assert_called_with('out')

    @mock.patch("modules.services.dataset_downloader.os.makedirs")
    @mock.patch("modules.services.dataset_downloader.open")
    @mock.patch("modules.services.dataset_downloader.requests.get")
    def test_downloads_apks(self, get_mock, open_mock, os_mock):
        self.dataset_downloader.download()
        self.assertTrue(mock.call(self.apk) in self.constructor_mock.construct.call_args_list)
        self.assertTrue(mock.call(self.apk2) in self.constructor_mock.construct.call_args_list)
        self.constructor_mock.reset_mock()
        self.assertEqual(get_mock.call_count, 2)
        self.assertTrue(mock.call(r'out/apk1.apk', 'wb') in open_mock.call_args_list)
        self.assertTrue(mock.call(r'out/apk2.apk', 'wb') in open_mock.call_args_list)


if __name__ == '__main__':
    unittest.main()
