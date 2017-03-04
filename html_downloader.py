import urllib.request
import urllib.parse
from config import session
class HtmlDownloader(object):
    def download_book_html(self,bookurl):
        full_url = urllib.parse.urljoin("https://book.douban.com/subject/", bookurl)
        response = session.get(full_url)
        return response.content