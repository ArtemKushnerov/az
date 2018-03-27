import config
from modules import adownloader, logging_util
from modules.entities.criteria import Criteria


def main():
    criteria = Criteria.init_from_dict(config.criteria)
    adownloader.run(config.input_file, config.key, config.number, criteria, out_dir=config.output_dir, metadata=config.metadata)


if __name__ == '__main__':
    logging_util.setup_logging()
    main()
