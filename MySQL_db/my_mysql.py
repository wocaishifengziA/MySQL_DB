# -*- coding:utf-8 -*-
import pymysql

mysql_data = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123456',
    'port': 3306,
    'db': 'saaaa'
}


class MyMySQL(object):

    def __init__(self):
        self.conn = pymysql.connect(host=mysql_data['host'], user=mysql_data['user'], password=mysql_data['password'],
                                    port=mysql_data['port'], db=mysql_data['db'])
        self.cursor = self.conn.cursor()

    def save_to_mysql(self, table, data):
        """ data 为一个 dict"""
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
        try:
            if self.cursor.execute(sql, tuple(data.values())):
                print('Successful')
                self.conn.commit()
        except:
            print('Failed')
            self.conn.rollback()

    def save_many_to_mysql(self, table, data):
        """ 传入的 data 是一个元素全为 dict 的列表 """
        list_data = []
        keys = ', '.join(data[0].keys())
        values = ', '.join(['%s'] * len(data[0]))
        for d in data:
            list_data.append(tuple(d.values()))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
        try:
            if self.cursor.executemany(sql, list_data):
                print('Successful')
                self.conn.commit()
        except:
            print('Failed')
            self.conn.rollback()