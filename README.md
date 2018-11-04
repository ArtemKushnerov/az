Downloads specified number of **randomly chosen** apks satisfying specified criteria from androzoo repository.  
Saves specified metadata to *metadata.csv*. dexdate, apksize and vtdetection require specifying lower and upper bounds in format lower:upper, both inclusive.  
One of the bounds can be omitted (i.e. you can write :upper or lower:)  
pkgname, markets, metadata, sha256, sha1, md5 can be either single values or comma separated lists. 
Key and input file can be specified as options or via local or global config file.
Allows downloading in the multiple threads.

### PREREQUISITES
- Python 3.6

### INSTALLATION

1. `pip install git+https://github.com/ArtemKushnerov/az.git@v1.2.2#egg=az`

2. create *.az* file in your home directory (~ on Linux 
and macOS, C:\Users\%USERNAME% on Windows) or in the directory where you want to invoke `az` from with the following contents:  
```
key=%API_KEY%  
input_file=%PATH_TO_INPUT_FILE%
```
Alternatively, use cli options `-k` and `-i`

Request the api key from androzoo, download and uncompress the input file from here https://androzoo.uni.lu/lists

### CONFIGURATION
You can configure api key and input file either using cli options or *.az* configuration file. The file can be placed locally (in directory where you want to invoke `az` from) or globally (in your home directory).
The precedence for reading config values is as follows: cli -> local-> global.

### SAMPLE USAGE  

  `az -n 10 -d 2015-12-11: -s :3000000  -m play.google.com,appchina`

This means: download 10 apks with the dexdate starting from the
2015-12-11 (inclusive), size up to 3000000 bytes (inclusive) and present on either play.google.com or appchina

##### Options:  
```
  -n, --number INTEGER     Number of apks to download.
  -d, --dexdate TEXT       The date on a dex file, format %Y-%m-%d, e.g.  2015-10-03.
  -s, --apksize TEXT       Apk size, in bytes.
  -vt, --vtdetection TEXT  Virus total rating, integer.
  -pn, --pkgname TEXT      Package names.
  -m, --markets TEXT       Markets, e.g. play.google.com. Possible values (can differ, since repository is updating): 1mobile,angeeks,anzhi,apk_bang,appchina,fdroid,freewarelovers,genome,hiapk,markets,mi.com,play.google.com,proandroid,slideme,torrents.
  --sha256 TEXT            SHA256 hashes.
  --sha1 TEXT              SHA1 hashes of apks to download.
  --md5 TEXT               MD5 hashes of apks to download.
  -md, --metadata TEXT     Metadata. This is a subset of latest.csv column names to keep in metadata.csv. By default sha256,pkg_name,apk_size,dex_date,markets.  
  -o, --out TEXT           Output folder name. By default current directory.
  -sd, --seed INTEGER      Seed for a random algorithm.
  -k, --key TEXT           Androzoo api key.
  -i, --input-file TEXT    Path to input csv.
  -t, --threads INTEGER    Number of threads for concurrent download. 4 by default.
  --version                Show the version and exit.
  --help                   Show this message and exit.  
```
