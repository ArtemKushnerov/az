import logging
import os
import sys

import requests

from modules.services.url_constructor import UrlConstructor
from multiprocessing.dummy import Pool


class DatasetDownloader:
    def __init__(self, dataset, threads, url_constructor=None, key='', out_dir='azoo_dataset'):
        self.dataset = dataset
        self.out_dir = out_dir
        if not url_constructor:
            url_constructor = UrlConstructor(key)
        self.url_constructor = url_constructor
        self.threads = threads

    def download(self):
        logging.info(f'DOWNLOADING {len(self.dataset)}, number of threads {self.threads}')
        if not os.path.exists(self.out_dir):
            os.makedirs(self.out_dir)

        with Pool(self.threads) as pool:
            pool.map(self.download_apk, self.dataset)

    def download_apk(self, apk):
        apk_save_path = os.path.join(self.out_dir, apk.pkg_name) + '.apk'
        try:
            if os.path.exists(apk_save_path):
                apk_save_path = apk_save_path.replace('.apk', f'{apk.sha1}.apk')
                logging.warning(f'apk with pkg {apk.pkg_name} already exists, saving by {apk_save_path}')
            logging.debug(f'DOWNLOAD {apk.pkg_name}... ')
            apk_url = self.url_constructor.construct(apk)
            response = requests.get(apk_url)
            with open(apk_save_path, 'wb') as out_file:
                code = response.status_code
                if code != 200:
                    logging.warning(f'HTTP code for {apk.pkg_name} is {code}')
                out_file.write(response.content)
        except:
            logging.error(f'Unexpected error while downloading {apk.pkg_name}: {sys.exc_info()[1]}')
