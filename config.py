output_dir = r'c:\SaToSS\out'
input_file ='c:\SaToSS\latest.csv'
base_url='https://androzoo.uni.lu/api/download?apikey={0}&sha256={01}'
key ='***REMOVED***'
number = 10
criteria = {
    # mandatory
    'number': 10,
    # optional, comment out those you don't need
    'dex_date': {'from': '11-12-2014'},
    # 'apk_size': {'from': 1, 'to': 4},
    # 'pkg_name': ['pkg1'],
    # 'vt_detection': {'from': 0, 'to': 5},
    'markets': ['play.google.com'],
}
