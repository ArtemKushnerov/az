from dateutil.parser import parse

output_dir = r'c:\SaToSS\azoo500'
input_file =r'c:\SaToSS\latest.csv'
base_url='https://androzoo.uni.lu/api/download?apikey={0}&sha256={01}'
key ='98da5f71867dcfd6cd7878435c29a0f94bb8862c63d65439fdb862a93151c831'
number = 500
metadata = ['sha256', 'pkg_name', 'apk_size', 'dex_date', 'markets']
criteria = {
    'dex_date': {'from': parse('11-12-2015')},
    # use curly braces for markets(i.e. set)
    'markets': {'play.google.com'},
}
