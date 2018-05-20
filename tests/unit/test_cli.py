import unittest
from unittest import mock

from click.testing import CliRunner

import main


class CliTest(unittest.TestCase):

    @mock.patch("modules.az.run")
    def test_sha256(self, mock_run):
        runner = CliRunner()
        result = runner.invoke(main.run, ['--sha256', '42'], catch_exceptions=False)
        self.assertNotEqual(result.output.strip(), 'Error: no such option: --sha256')

    @mock.patch("modules.az.run")
    def test_sha1(self, mock_run):
        runner = CliRunner()
        result = runner.invoke(main.run, ['--sha1', '42'], catch_exceptions=False)
        self.assertNotEqual(result.output.strip(), 'Error: no such option: --sha1')

    @mock.patch("modules.az.run")
    def test_md5(self, mock_run):
        runner = CliRunner()
        result = runner.invoke(main.run, ['--md5', '42'], catch_exceptions=False)
        self.assertNotEqual(result.output.strip(), 'Error: no such option: --md5')

    @mock.patch("modules.az.run")
    def test_one_hashing_algorithm_is_specified(self, mock_run):
        runner = CliRunner()
        result = runner.invoke(main.run, ['--md5', '42', '--sha256', '8'], catch_exceptions=False)
        self.assertEqual(result.output.strip(), 'Please specify only one hashing algorithm')
        result = runner.invoke(main.run, ['--md5', '42', '--sha1', '8'], catch_exceptions=False)
        self.assertEqual(result.output.strip(), 'Please specify only one hashing algorithm')
        result = runner.invoke(main.run, ['--sha256', '42', '--sha1', '8'], catch_exceptions=False)
        self.assertEqual(result.output.strip(), 'Please specify only one hashing algorithm')
        result = runner.invoke(main.run, ['--sha256', '42', '--sha1', '8', '--md5', '9'], catch_exceptions=False)
        self.assertEqual(result.output.strip(), 'Please specify only one hashing algorithm')
        result = runner.invoke(main.run, ['-n', '5'], catch_exceptions=False)
        self.assertNotEqual(result.output.strip(), 'Please specify only one hashing algorithm')

