import logging.config
import os
import shutil
import unittest

from click.testing import CliRunner

import cli


class IntegrationTest(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
        self.expected_out_dir_contents = ['com.auctionmobility.auctions.vinpresariowineauctions.apk', 'com.ncbhk.mortgage.android.hk.apk', 'com.netpulse.mobile.creekbridgefitness.apk', 'com.smartsound.skeeperheart.apk', 'com.zabuzalabs.balloonbowarrow_football.apk', 'metadata.csv']

    def test_from_cli(self):
        out_dir = 'out'
        if os.path.exists(out_dir):
            shutil.rmtree(out_dir)
        os.mkdir(out_dir)

        runner = CliRunner()
        runner.invoke(cli.run, ['-n', '5', '-d', '2015-12-11:', '-m', 'play.google.com', '-o', out_dir, '-sd', '1'], catch_exceptions=False)
        out_dir_contents = os.listdir(out_dir)
        self.assertEqual(out_dir_contents, self.expected_out_dir_contents)


if __name__ == '__main__':
    unittest.main()
