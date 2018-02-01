import os
import urllib.request

import logging

import time

import sys

import shutil
from conf import config

if config.concurrency_module == 'dummy':
    from multiprocessing.dummy import Pool
elif config.concurrency_module == 'pool':
    from multiprocessing.pool import Pool


def download_apks(dataset):
    logging.info('DOWNLOADING {0} APKS...'.format(dataset.get_size()))
    if not os.path.exists(config.apk_dir):
        os.makedirs(config.apk_dir)

    start = time.time()
    if config.concurrent_download:
        download_concurrently(dataset)
        end = time.time()
        logging.debug('It took {0} to download {1} apks concurrently using  pool from {2}'
                      ' ({3} pool size)'.format(end - start, dataset.get_size(), config.concurrency_module,
                                                config.pool_size_downloading))
    else:
        download_sequentially(dataset)
        end = time.time()
        logging.debug('It took {0} to download {1} apks sequentially'.format(end - start, dataset.get_size()))


def download_sequentially(dataset):
    for apk in dataset:
        download(apk)


def download_concurrently(dataset):
    with Pool(config.pool_size_downloading) as pool:
        pool.map(download, dataset)


def download(apk):
    try:
        if os.path.exists(apk.path_on_disk):
            logging.debug('{0} is already downloaded'.format(apk.name))
            return
        logging.debug('Downloading {0}... '.format(apk.name))
        with urllib.request.urlopen(apk.url) as response, open(apk.path_on_disk, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
    except:
        logging.error("Unexpected error while downloading {}: {}".format(apk.name, sys.exc_info()[1]))


