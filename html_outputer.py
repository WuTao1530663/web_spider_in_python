# -*- coding: utf-8 -*-
import pymysql
class HtmlOutputer(object):
    def __init__(self):
        self.old_book_ids = set()
        self.new_book_ids = set()
    def college(self, book_ids):
        if book_ids is None:
            return
        for book_id in book_ids:
            if book_id not in self.old_book_ids and book_id not in self.new_book_ids:
                self.new_book_ids.add(book_id)

    def book_ids_size(self):
        return len(self.old_book_ids)
    def output_database(self):
        connect = pymysql.Connect(host='localhost',
                                  port=3306,
                                  user='root',
                                  passwd='1234',
                                  db='spider',
                                  charset='utf8')
        try:
            for book_id in self.new_book_ids:
                sql = "INSERT INTO book(id) VALUE (%s)"
                with connect.cursor() as cursor:
                    cursor.execute(sql,(book_id))
                connect.commit()
                self.old_book_ids.add(book_id)
            print ("%d条数据存储成功,已存数据%d条"% len(self.new_book_ids),len(self.old_book_ids))
        finally:
            self.new_book_ids = set()
            connect.close()

    