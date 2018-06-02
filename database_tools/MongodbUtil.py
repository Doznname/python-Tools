# encoding=utf-8
# author: doo

import pymongo

class MongodbUtil(object):
    """
    连接mondb工具类
    """
    #集合名称(会自动创建)
    collection_name = 'collection_name'
    def __init__(self):
        self.mongo_uri = 'mongodb://localhost:27017'
        # 数据库名
        self.mongo_db ='test'

    def open_connection(self):
        """
        启动连接mongodb
        :return:
        """
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_connection(self):
        """
        关闭连接
        :return:
        """
        self.client.close()

    def save(self, item):
        """
        处理item，向mongodb中存储item数据
        :param item:
        :return item:
        """
        try:
            self.db[self.collection_name].insert(dict(item))
            flag = True
        except:
            flag = False
        return flag
    def save2(self,col_name, item):
        """
        处理item，向mongodb指定的cloumn中存储item数据
        :param item:
        :return item:
        """
        try:
            self.db[col_name].insert(dict(item))
            flag = True
        except:
            flag = False
        return flag
