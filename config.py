output_dir = r'c:\SaToSS\azoo500'
input_file = r'c:\SaToSS\latest.csv'
base_url = 'https://androzoo.uni.lu/api/download?apikey={0}&sha256={01}'
key = '***REMOVED***'
number = 500
metadata = ['sha256', 'pkg_name', 'apk_size', 'dex_date', 'markets']
criteria = {
    'dex_date': {'from': '11-12-2015'},
    # use curly braces for markets(i.e. set)
    'markets': {'play.google.com'},
}
