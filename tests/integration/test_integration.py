import logging.config
import os
import shutil
import unittest

from click.testing import CliRunner

import cli
from modules import adownloader
from modules.entities.criteria import Criteria


class IntegrationTest(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
        self.expected_out_dir_contents = ['com.bz.solo.theme.gray.dim.apk', 'com.GoldStudio.TurtleParkour.apk', 'com.kbf.app27730661.apk', 'com.nicescreen.screenlock.ak47HD.apk',
                                          'com.zabuzalabs.balloonbowarrow_football.apk', 'metadata.csv']

    def test_from_cli(self):
        self.out_cli = 'out/cli'
        if os.path.exists(self.out_cli):
            shutil.rmtree(self.out_cli)

        runner = CliRunner()
        runner.invoke(cli.run, ['-n', '5', '-d', '2015-12-11:', '-m', 'play.google.com', '-o', self.out_cli, '-sd', '1'], catch_exceptions=False)
        out_dir_contents = os.listdir(self.out_cli)
        self.assertEqual(out_dir_contents, self.expected_out_dir_contents)

    def test_from_config(self):
        self.out_config = 'out/config'
        if os.path.exists(self.out_config):
            shutil.rmtree(self.out_config)

        config = {
            'dex_date': {'from': '2015-12-11'},
            'markets': {'play.google.com'},
        }
        metadata = ['sha256', 'pkg_name', 'apk_size', 'dex_date', 'markets']
        input_file = 'resources/latest_first50.csv'
        api_key = '98da5f71867dcfd6cd7878435c29a0f94bb8862c63d65439fdb862a93151c831'
        apk_number = 5
        criteria = Criteria.init_from_dict(config)
        adownloader.run(input_file, api_key, apk_number, criteria, metadata, out_dir=self.out_config, seed=1)
        out_dir_contents = os.listdir(self.out_config)
        self.assertEqual(out_dir_contents, self.expected_out_dir_contents)


if __name__ == '__main__':
    unittest.main()
