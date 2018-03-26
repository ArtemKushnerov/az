import unittest
from unittest import mock

from click.testing import CliRunner

import cli

from modules.exceptions import AbsentUserConfigException


class CliTest(unittest.TestCase):

    @mock.patch('cli.os')
    def test_throws_exception_if_user_config_empty(self, os_mock):
        os_mock.path.exists.return_value = False
        runner = CliRunner()
        result = runner.invoke(cli.run, ['-n 5'])
        self.assertTrue(result.exception is not None)
        self.assertTrue(result.exception.__class__ == AbsentUserConfigException)

    def test_validate(self):
        pass
        # todo

if __name__ == '__main':
    unittest.main()
