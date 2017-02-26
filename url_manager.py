class UrlManger(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        self.new_book_urls = set()
        self.old_book_urls = set()
    def add_new_url(self, url):
        if url is None or url in self.old_urls or url in self.new_urls:
            return
        self.new_urls.add(url)

    def add_new_urls(self, new_urls):
        if new_urls is None or len(new_urls) == 0:
            return
        for new_url in new_urls:
            self.add_new_url(new_url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_book_urls(self, new_book_urls):
        if new_book_urls is None or len(new_book_urls) == 0:
            return
        for new_book_url in new_book_urls:
            self.add_new_book_url(new_book_url)

    def add_new_book_url(self, url):
        if url is None or url in self.old_book_urls or url in self.new_book_urls:
            return
        self.new_book_urls.add(url)

    def get_new_book_url(self):
        new_book_url = self.new_book_urls.pop()
        self.old_book_urls.add(new_book_url)
        return new_book_url

    def has_new_book_url(self):
        return len(self.new_book_urls) != 0


