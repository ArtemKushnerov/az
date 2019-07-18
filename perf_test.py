import asyncio
import os
import time
from multiprocessing.dummy import Pool

import aiofiles
import requests
from aiohttp import ClientSession


async def download_dataset_async(urls):
    if not os.path.exists('async'):
        os.makedirs('async')
    async with ClientSession() as session:
        coros = [download_url_async(url, session) for url in urls]
        await asyncio.wait(coros)


async def download_url_async(url, session):
    apk_save_path = os.path.join('async',f'{time.time()}.html')
    response = await session.get(url)
    async with aiofiles.open(apk_save_path, 'wb') as out_file:
        contents = await response.read()
        await out_file.write(contents)


def download_dataset_sync(urls):
    if not os.path.exists('sync'):
        os.makedirs('sync')

    with Pool(4) as pool:
        pool.map(download_url, urls)


def download_url(url):
    apk_save_path = os.path.join('sync', f'{time.time()}.html')
    response = requests.get(url)
    with open(apk_save_path, 'wb') as out_file:
        out_file.write(response.content)


urls = ['http://example.com'] * 1000

start = time.perf_counter()
asyncio.run((download_dataset_async(urls)))
finish = time.perf_counter()
total = finish - start
print(f'Async: {total}')

start = time.perf_counter()
download_dataset_sync(urls)
finish = time.perf_counter()
total = finish - start
print(f'Sync: {total}')
