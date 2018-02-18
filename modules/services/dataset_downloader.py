import logging

import os
import urllib.request

import shutil

import sys

from modules.services.url_constructor import UrlConstructor


class DatasetDownloader:
    def __init__(self, dataset, url_constructor=None, base_url='', key='', out_dir='azoo_dataset'):
        self.dataset = dataset
        self.out_dir = out_dir
        if not url_constructor:
            url_constructor = UrlConstructor(base_url, key)
        self.url_constructor = url_constructor

    def download(self):
        logging.info(f'DOWNLOADING {len(self.dataset)}')
        if not os.path.exists(self.out_dir):
            os.makedirs(self.out_dir)

        for apk in self.dataset:
            self.download_apk(apk)

    def download_apk(self, apk):
        apk_save_path = os.path.join(self.out_dir, apk.pkg_name) +'.apk'
        try:
            if os.path.exists(apk_save_path):
                apk_save_path = apk_save_path.replace('.apk', f'{apk.sha1}.apk')
                logging.warning(f'apk with pkg {apk.pkg_name} already exists, saving by {apk_save_path}')
            logging.info(f'DOWNLOAD {apk.pkg_name}... ')
            apk_url = self.url_constructor.construct(apk)
            with urllib.request.urlopen(apk_url) as response, open(apk_save_path, 'wb') as out_file:
                code = response.getcode()
                if code != 200:
                    logging.warning(f'HTTP code for {apk.pkg_name} is {code}')
                shutil.copyfileobj(response, out_file)
        except:
            # todo handle exception better
            logging.error(f'Unexpected error while downloading {apk.pkg_name}: {sys.exc_info()[1]}')
