# -*- coding: utf-8 -*-
import pymysql
class HtmlOutputer(object):
    def __init__(self):
        self.book_ids = set()

    def college(self, new_book_ids):
        if new_book_ids is None:
            return
        for new_book_id in new_book_ids:
            if new_book_id not in self.book_ids:
                self.book_ids.add(new_book_id)

    def book_ids_size(self):
        return len(self.book_ids)
    def output_database(self):
        connect = pymysql.Connect(host='localhost',
                                  port=3306,
                                  user='root',
                                  passwd='1234',
                                  db='spider',
                                  charset='utf8')



        try:
            for book_id in self.book_ids:
                sql = "INSERT INTO book(id) VALUE (%s)"
                with connect.cursor() as cursor:
                    cursor.execute(sql,(book_id))
                connect.commit()
            print ("%d条数据存储成功"% len(self.book_ids))
        finally:
            connect.close()

    