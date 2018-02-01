apks_to_analyze = 100

analyze_only_malware = False
analyze_only_existing_on_disk = True

api_key = '***REMOVED***'


# Paths
datasets_dir = 'D:\google_play'
apk_dir = datasets_dir + '/apks'
decompiled_apks_dir = datasets_dir + '/decompiled_apks'
csv_path = 'c:\SaToSS\latest.csv'
results_path = '../../results/'
results_file = 'results.txt'
dataset_save_path_file = 'dataset.csv'
not_found_permissions_file = 'not_found_permissions.txt'
target_api_level_distribution_file = 'target_api_level_distribution.png'
estimated_api_level_distribution_file = 'estimated_target_api_level_distribution.png'
permissions_csv_file = datasets_dir + '/permissions.csv'

# Concurrency
concurrency_module = 'dummy'

concurrent_download = False
pool_size_downloading = 4

concurrent_decompiling = True
pool_size_decompiling = 10

