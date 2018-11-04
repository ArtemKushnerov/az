import logging.config
import os
import shutil
import unittest

from click.testing import CliRunner

from modules import main


THIS_DIR = os.path.dirname(os.path.abspath(__file__))

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
        input_file_path = os.path.join(THIS_DIR,'resources/latest_first50.csv')
        runner.invoke(main.run, ['-i', input_file_path, '-n', '5', '-d', '2015-12-11:', '-m', 'play.google.com', '-o', out_dir, '-sd', '1'], catch_exceptions=False)
        out_dir_contents = os.listdir(out_dir)
        self.assertEqual(set(out_dir_contents), set(self.expected_out_dir_contents))


if __name__ == '__main__':
    unittest.main()
