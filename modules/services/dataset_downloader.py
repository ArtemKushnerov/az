import asyncio
import logging
import os
import sys

import aiofiles
from aiohttp import ClientSession

from modules.services.url_constructor import UrlConstructor


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

        asyncio.run(self.download_dataset())

    async def download_dataset(self):
        async with ClientSession() as session:
            coros = [self.download_apk(apk, session) for apk in self.dataset]
            await asyncio.wait(coros)

    async def download_apk(self, apk, session):
        apk_save_path = os.path.join(self.out_dir, apk.pkg_name) + '.apk'
        try:
            if os.path.exists(apk_save_path):
                apk_save_path = apk_save_path.replace('.apk', f'{apk.sha1}.apk')
                logging.warning(f'apk with pkg {apk.pkg_name} already exists, saving by {apk_save_path}')
            logging.debug(f'DOWNLOAD {apk.pkg_name}... ')
            apk_url = self.url_constructor.construct(apk)
            response = await session.get(apk_url)
            async with aiofiles.open(apk_save_path, 'wb') as out_file:
                code = response.status
                if code != 200:
                    logging.warning(f'HTTP code for {apk.pkg_name} is {code}')
                await out_file.write(await response.read())
        except:
            logging.error(f'Unexpected error while downloading {apk.pkg_name}: {sys.exc_info()[1]}')
