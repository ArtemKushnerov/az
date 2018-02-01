import logging.config

import yaml

def setup_logging():
    with open('../logging.yaml') as f:
        logging.config.dictConfig(yaml.safe_load(f.read()))


if __name__ == '__main__':
    setup_logging()
    logging.info('hello')
