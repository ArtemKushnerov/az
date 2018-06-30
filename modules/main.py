import os
import sys

import click

from modules import az, logging_util
from modules.cli.args import Arguments
from modules.cli.parser import Parser
from modules.cli.validator import Validator
from modules.entities.criteria import Criteria
from modules.exceptions import AzException, NoArgsException



@click.command()
@click.option('--number', '-n', type=click.INT, help='Number of apks to download.')
@click.option('--dexdate', '-d', help='The date on a dex file, format %Y-%m-%d, e.g. 2015-10-03.')
@click.option('--apksize', '-s', help='Apk size, in bytes.')
@click.option('--vtdetection', '-vt', help='Virus total rating, integer.')
@click.option('--pkgname', '-pn', help='Package names.')
@click.option('--markets', '-m', help='Markets, e.g. play.google.com. Possible values (can differ, since repository is updating): 1mobile,angeeks,anzhi,apk_bang,appchina,fdroid,freewarelovers,genome,hiapk,markets,mi.com,play.google.com,proandroid,slideme,torrents.')
@click.option('--sha256', help='SHA256 hashes of apks to download.')
@click.option('--sha1', help='SHA1 hashes of apks to download.')
@click.option('--md5', help='MD5 hashes of apks to download.')
@click.option('--metadata', '-md', help='Metadata. This is a subset of latest.csv column names to keep in metadata.csv. By default sha256,pkg_name,apk_size,dex_date,markets.')
@click.option('--out', '-o', help='Output folder name. By default current directory.')
@click.option('--seed', '-sd', type=click.INT, help='Seed for a random algorithm.')
@click.option('--key', '-k', help='Androzoo api key.')
@click.option('--input-file', '-i', help='Path to input csv.')
@click.option('--threads', '-t', type=click.INT, default=4, help='Number of threads for concurrent download. 4 by default.')
@click.version_option(message='%(version)s')
def run(number, dexdate, apksize, vtdetection, pkgname, markets, metadata, out, seed, sha256, sha1, md5, key, input_file, threads):
    """Downloads specified number of apks satisfying specified criteria from androzoo repository. Saves specified metadata to metadata.csv.
    dexdate, apksize and vtdetection require specifying lower and upper bounds in format lower:upper, both inclusive. One of the bounds can be omitted (i.e. you can write :upper or lower:)
    pkgname, markets, metadata, sha256, sha1, md5 can be either single values or comma separated lists.
    Key and input file can be specified as options or via local or global config file.
    Allows downloading in the multiple threads.

    Sample usage:

    az -n 10 -d 2015-12-11: -s :3000000  -m play.google.com,appchina

    This means: download 10 apks with the dexdate starting from the 2015-12-11(inclusive), size up to 3000000 bytes(inclusive) and present on either play.google.com or appchina
     """

    try:
        args = Arguments(number, dexdate, apksize, vtdetection, markets, pkgname, metadata, sha256, sha1, md5, key, input_file)
        Validator(args).validate()
        logging_util.setup_logging()
        number, *criteria_args, metadata, key, input_file = Parser(args).parse()
        criteria = Criteria(*criteria_args)
        az.run(input_file, key, number, criteria, out_dir=out if out else os.getcwd(), metadata=metadata, seed=seed, threads=threads)
    except NoArgsException:
        with click.Context(run) as ctx:
            click.echo(run.get_help(ctx))
    except AzException as e:
        sys.exit(str(e))
    else:
        sys.exit(0)


if __name__ == '__main__':
    run(['-vt', '0:0'])
