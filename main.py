import logging.config

import yaml

from modules import adownloader
import config

def setup_logging():
    with open('logging.yaml') as f:
        logging.config.dictConfig(yaml.safe_load(f.read()))


def main():
    adownloader.run(config.input_file, config.base_url, config.key, config.number, config.criteria, out_dir='azoo_dataset')

if __name__ == '__main__':
    main()
