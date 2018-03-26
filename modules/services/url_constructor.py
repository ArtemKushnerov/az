class UrlConstructor:
    def __init__(self, key='', base_url='https://androzoo.uni.lu/api/download?apikey={0}&sha256={01}'):
        self.base_url = base_url
        self.key = key

    def construct(self, apk):
        return self.base_url.format(self.key, apk.sha256)
