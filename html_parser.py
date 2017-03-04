from bs4 import BeautifulSoup
import re
import urllib.parse
import requests
class HtmlParser(object):
    def parse(self,url, html_content):
        book_data = {}
        soup = BeautifulSoup(html_content, 'html.parser',from_encoding='utf-8')

        book_data['书籍ID'] = url[-8:-1]
        book_data['书名'] = soup.find('span',property="v:itemreviewed").text

        info = soup.find('div', id='info')
        book_data['评分'] = soup.find("strong", class_="ll rating_num ").text
        book_data['ISBN'] = info.find("span", text=re.compile(u'ISBN')).next_sibling
        if float(book_data['评分'])<=7.8 or book_data['ISBN'] is None:
            return None
        book_data['作者'] = info.find("span",text=re.compile(u'作者')).find_next_sibling().text
        book_data['出版社'] = info.find("span",text=re.compile(u'出版社')).next_sibling
        book_data['出版年'] = info.find("span",text=re.compile(u'出版年')).next_sibling
        book_data['页数'] = info.find("span",text=re.compile(u'页数')).next_sibling
        book_data['定价'] = info.find("span",text=re.compile(u'定价')).next_sibling

        #<strong class="ll rating_num " property="v:average"> 9.1 </strong>

        #<span property="v:votes">122319</span>
        book_data['评价人数'] = soup.find("span", property="v:votes").text
        book_data['推荐书籍ID'] = []
        #<div class="intro">
        book_data['简介'] = soup.find('div',class_='intro').text
        #<div id="db-rec-section" class="block5 subject_show knnlike">

        recommand_book_urls = soup.find('div',id="db-rec-section").find("div",class_="content clearfix")
        for book in recommand_book_urls.find_all("dl",class_=""):
            book_data['推荐书籍ID'].append(book.dd.a['href'][-8:-1])
#        for key,value in zip(book_data.keys(),book_data.values()):
#            print ("%s : %s"%(key,value))

        return book_data


if __name__ == '__main__':
    info = u"""<div id="info" class="">\
    <span>\
      <span class="pl"> 作者</span>\
        <a class="" href="/search/%E5%8D%A1%E5%8B%92%E5%BE%B7%C2%B7%E8%83%A1%E8%B5%9B%E5%B0%BC">[美] 卡勒德·胡赛尼</a>\
    </span><br>\
    <span class="pl">出版社:</span> 上海人民出版社<br>\
<span class="pl">原作名:</span> The Kite Runner<br>\
    <span>\
      <span class="pl"> 译者</span>:\
        <a class="" href="/search/%E6%9D%8E%E7%BB%A7%E5%AE%8F">李继宏</a>
    </span><br>\
    <span class="pl">出版年:</span> 2006-5<br>\
    <span class="pl">页数:</span> 362<br>\
    <span class="pl">定价:</span> 29.00元<br>\
    <span class="pl">装帧:</span> 平装<br>\
    <span class="pl">丛书:</span>&nbsp;<a href="https://book.douban.com/series/19760">卡勒德·胡赛尼作品</a><br>\
      <span class="pl">ISBN:</span> 9787208061644<br>\
</div>"""
    info = "clearfix"

    HtmlParser().parse("https://book.douban.com/subject/1082154/",requests.get("https://book.douban.com/subject/1082154/").content)

