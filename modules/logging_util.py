import logging.config
from pkg_resources import resource_stream

import yaml


def setup_logging():
    with resource_stream('modules.resources', 'logging.yaml') as f:
        logging.config.dictConfig(yaml.safe_load(f.read()))
