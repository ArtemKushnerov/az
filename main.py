import logging.config

import yaml

from modules import adownloader
from config import config

def setup_logging():
    with open('logging.yaml') as f:
        logging.config.dictConfig(yaml.safe_load(f.read()))


def main():
    adownloader.run(**config)

if __name__ == '__main__':
    main()
