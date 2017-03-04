# -*- coding: utf-8 -*-
import pymysql
import html_parser,requests
class HtmlOutputer(object):
    def __init__(self):
        self.saved = 0
        self.datas = []
        self.connect = pymysql.Connect(host='localhost',
                                  port=3306,
                                  user='root',
                                  passwd='1234',
                                  db='spider',
                                  charset='utf8')
        with self.connect.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS BOOK")#
            # 书籍ID 书名 作者 出版社 出版年 页数 定价 ISBN 评分 评价人数 推荐书籍ID

            cursor.execute("CREATE TABLE BOOK (书籍ID VARCHAR(255),书名 VARCHAR(255),作者 VARCHAR(255),出版社 VARCHAR(255),\
                        出版年 VARCHAR(255),页数 INT,定价 VARCHAR(255),ISBN VARCHAR(255),评分 DOUBLE,评价人数 INT,推荐书籍ID text,简介 TEXT)")
            #cursor.execute("CREATE TABLE BOOK (id INT(5) NOT NULL auto_increment,书籍ID VARCHAR(255),PRIMARY KEY(id))")

            self.connect.commit()
            self.connect.close()

    def college(self, new_book_data):
       self.datas.append(new_book_data)

    def data_size(self):
        return len(self.datas)

    def output_database(self):

        self.connect = pymysql.Connect(host='localhost',
                                       port=3306,
                                       user='root',
                                       passwd='1234',
                                       db='spider',
                                       charset='utf8')

        try:
            for data in self.datas:
                try:
                    sql = """INSERT INTO book(书籍ID,书名,作者,出版社,出版年,页数,定价,ISBN,评分,评价人数,推荐书籍ID,简介)\
                     VALUE ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")"""%(data['书籍ID'], \
                    data['书名'],data['作者'],data['出版社'],data['出版年'],int(data['页数']),\
                    data['定价'],data['ISBN'],float(data['评分']),data['评价人数'],data['推荐书籍ID'],data['简介'])
                    with self.connect.cursor() as cursor:
                        cursor.execute(sql)
                        self.connect.commit()
                        self.saved += 1
                except:
                    print("存储书籍ID：%d失败"%(data["书籍ID"]))
        finally:
            print("本次存储书籍信息%d条,共存储%d条" % (self.data_size(),self.saved))
            self.datas.clear()
            self.connect.close()


if __name__ == '__main__':
    outputer = HtmlOutputer()
    data = html_parser.HtmlParser().parse("https://book.douban.com/subject/25862578/",requests.get("https://book.douban.com/subject/25862578/").content)
    sql = "INSERT INTO 'book' VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"%(data['书籍ID'], data['书名'],data['作者'],data['出版社'],data['出版年'],data['页数'],\
                data['定价'],data['ISBN'], data['评分'],data['评价人数'],data['推荐书籍ID'],data['简介'])
    print(sql)
    outputer.college(data)
    outputer.output_database()
