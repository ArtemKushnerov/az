import os
import sys

import click

from modules import adownloader, logging_util
from modules.cli.parser import Parser
from modules.cli.user_config import UserConfig
from modules.entities.criteria import Criteria


@click.command()
@click.option('--number', '-n', type=click.INT, help='Number of apks to download')
@click.option('--dexdate', '-d', help='Dex date in format %Y-%m-%d')
@click.option('--apksize', '-s', type=click.INT, help='Apk size TODO: in what units')
@click.option('--vtdetection', '-vt', type=click.INT, help='Virus total rating')
@click.option('--pkgname', '-pn', help='Package names')
@click.option('--markets', '-m', help='Markets')
@click.option('--metadata', '-md', help='Metadata')
@click.option('--out', '-o', help='Output folder name')
@click.option('--seed', '-sd', type=click.INT, help='Seed for a random algorithm')
def run(number, dexdate, apksize, vtdetection, pkgname, markets, metadata, out, seed):
    """Downloads specified number of apks satisfying specified criteria from androzoo repository. Use ':' as a delimiter for range options and ',' for list options"""
    logging_util.setup_logging()
    *criteria_args, metadata = Parser(dexdate, apksize, vtdetection, markets, pkgname, metadata).parse()
    criteria = Criteria(*criteria_args)
    user_config = UserConfig()
    adownloader.run(user_config.input_file, user_config.key, number, criteria, out_dir=out if out else os.getcwd(), metadata=metadata, seed=seed)
    sys.exit(0)


