import unittest
from unittest import mock

from click.testing import CliRunner

import cli


class CliTest(unittest.TestCase):

    @mock.patch("modules.adownloader.run")
    def test_sha256(self, mock_run):
        runner = CliRunner()
        result = runner.invoke(cli.run, ['--sha256', '42'], catch_exceptions=False)
        self.assertNotEqual(result.output.strip(), 'Error: no such option: --sha256')

    @mock.patch("modules.adownloader.run")
    def test_sha1(self, mock_run):
        runner = CliRunner()
        result = runner.invoke(cli.run, ['--sha1', '42'], catch_exceptions=False)
        self.assertNotEqual(result.output.strip(), 'Error: no such option: --sha1')

    @mock.patch("modules.adownloader.run")
    def test_md5(self, mock_run):
        runner = CliRunner()
        result = runner.invoke(cli.run, ['--md5', '42'], catch_exceptions=False)
        self.assertNotEqual(result.output.strip(), 'Error: no such option: --md5')
