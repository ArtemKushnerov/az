class UrlConstructor:
    def __init__(self, base_url='', key=''):
        self.base_url = base_url
        self.key = key

    def construct(self, apk):
        return self.base_url.format(self.key, apk.sha256)
