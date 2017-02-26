from bs4 import BeautifulSoup
import re
import urllib.parse
class HtmlParser(object):
    def parse(self, html_content):
        new_urls = []
        new_book_urls = []
        if html_content is None:
            return new_urls,new_book_urls
        soup = BeautifulSoup(html_content,'html.parser',from_encoding='utf-8')
        new_url_nodes = soup.find_all('a',href=re.compile("^(/)"))

        # book url example
        # < a class ="" href="https://book.douban.com/subject/26931151/" title="被误诊的艺术史" > 被误诊的艺术史 < / a >
        book_url_nodes = soup.find_all('a',href= re.compile("https://book.douban.com/subject/\d+"))
        for new_url_node in new_url_nodes:
            if new_url_node.attrs['href'] is not None:
                new_urls.append(new_url_node['href'])
        for book_url_node in book_url_nodes:
            if book_url_node.attrs['href'] is not None:
                new_book_urls.append(book_url_node['href'])

        new_book_ids = list(map(lambda url:url.replace("https://","").split('/')[-2], new_book_urls))
    #    new_urls = list(map(lambda url:url.))
        return new_urls,new_book_ids
