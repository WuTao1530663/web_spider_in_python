import urllib.request
import urllib.parse
import requests
class HtmlDownloader(object):
    def download_html(self, url):
        full_url = urllib.parse.urljoin("https://book.douban.com",url)
        response = requests.get(full_url)

        return response.content