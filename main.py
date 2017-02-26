# -*- coding: utf-8 -*-
import url_manager,html_parser,image_downloader,html_downloader,html_outputer



class bookSPider(object):
    def __init__(self):
        self.urls = url_manager.UrlManger()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()


    def craw(self,root_url):
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
             print("已经收集 %d 条书籍数据" % self.outputer.book_ids_size())
             try :
                new_url = self.urls.get_new_url()
                print("正在抓取页面 %s"%(new_url))
                html_content = self.downloader.download_html(new_url)
                new_urls, new_book_ids = self.parser.parse(html_content)
                self.urls.add_new_urls(new_urls)
                #self.urls.add_new_book_urls(new_book_urls)
                self.outputer.college(new_book_ids)
             except:
                print("craw fail")
        self.outputer.output_database()
import urllib.request
import requests

if __name__ == '__main__':

    root_url = "https://book.douban.com/"
    spider = bookSPider()
    spider.craw(root_url)
  #a = 'bats\u00E0'
  #print (str(a))
  #

