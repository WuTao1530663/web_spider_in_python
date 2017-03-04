# -*- coding: utf-8 -*-
import time
import threading
import url_manager, html_parser,html_downloader, html_outputer,login

class bookSPider(object):
    def __init__(self):
        self.urls = url_manager.UrlManger()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    #    self.logined = True
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        self.lock3 = threading.Lock()



    def craw(self, root_url):
     #   with self.lock1:
     #       while ~self.logined:
     #           if login.login() == 200:
     #               print("豆瓣登录成功,开始抓取")
     #               self.logined = True
     #               break
      #          print("登录失败5秒钟后重试")
      #          time.sleep(5)

        self.urls.add_new_url(root_url[-8:-1])
        count = 0
        while self.urls.has_new_url():
            try:
                with self.lock3:
                    new_url = self.urls.get_new_url()
                html_content = self.downloader.download_book_html(new_url)
                new_book_data = self.parser.parse(new_url,html_content)
                if new_book_data is None:
                    continue
                print("正在抓取书籍 %s 的信息" % (new_book_data['书名']))
                with self.lock2:
                    self.urls.add_new_urls(new_book_data['推荐书籍ID'])
                self.outputer.college(new_book_data)
            except Exception:
                print("抓取出错")
            finally:
                count += 1
                if count % 5 == 0:
                    self.outputer.output_database()

    def main(self, root_url,threads=5):
        for i in range(threads):
            t = threading.Thread(target=self.craw, args=(root_url,))
            # t.setDaemon(True)
            t.start()


if __name__ == '__main__':
    root_url = "https://book.douban.com/subject/1770782/"
    spider = bookSPider()
    spider.main(root_url,threads=3)
    # a = 'bats\u00E0'
    # print (str(a))
    #

