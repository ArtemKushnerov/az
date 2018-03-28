import os
import sys

import click

from modules import adownloader, logging_util
from modules.cli.parser import Parser
from modules.cli.user_config import UserConfig
from modules.entities.criteria import Criteria


@click.command()
@click.option('--number', '-n', type=click.INT, help='Number of apks to download.')
@click.option('--dexdate', '-d', help='The date on a dex file, format %Y-%m-%d, e.g. 2015-10-03')
@click.option('--apksize', '-s', help='Apk size, in bytes')
@click.option('--vtdetection', '-vt', help='Virus total rating, integer')
@click.option('--pkgname', '-pn', help='Package names')
@click.option('--markets', '-m', help='Markets, e.g. play.google.com. Possible values (can differ, since repository is updating): 1mobile,angeeks,anzhi,apk_bang,appchina,fdroid,freewarelovers,genome,hiapk,markets,mi.com,play.google.com,proandroid,slideme,torrents')
@click.option('--metadata', '-md', help='Metadata. This is a subset of latest.csv column names to keep in metadata.csv. By default sha256,pkg_name,apk_size,dex_date,markets')
@click.option('--out', '-o', help='Output folder name. By default current directory')
@click.option('--seed', '-sd', type=click.INT, help='Seed for a random algorithm')
def run(number, dexdate, apksize, vtdetection, pkgname, markets, metadata, out, seed):
    """Downloads specified number of apks satisfying specified criteria from androzoo repository. Saves specified metadata to metadata.csv.
    dexdate, apksize and vtdetection require specifying lower and upper bounds in format lower:upper, both inclusive. One of the bounds can be omitted (i.e. you can write :upper or lower:)
    pkgname, markets, metadata can be either single values or comma separated lists.

    Sample usage:

    az -n 10 -d 2015-12-11: -s :3000000  -m play.google.com,appchina

    This means: download 10 apks with the dexdate starting from the 2015-12-11(inclusive), size up to 3000000 bytes(inclusive) and present on either play.google.com or appchina
     """
    logging_util.setup_logging()
    *criteria_args, metadata = Parser(dexdate, apksize, vtdetection, markets, pkgname, metadata).parse()
    criteria = Criteria(*criteria_args)
    user_config = UserConfig()
    adownloader.run(user_config.input_file, user_config.key, number, criteria, out_dir=out if out else os.getcwd(), metadata=metadata, seed=seed)
    sys.exit(0)


