# encoding=utf-8
# author: doo

import MySQLdb
class MySQLUtil(object):
    """
    操作MySQL工具类
    """
    host = "localhost"
    username = "root"
    password = "root"
    database = "test"
    
    def __init__(self):
        self.conn = MySQLdb.connect(self.host, self.username, self.password, self.database, charset='utf8')
        self.cursor = self.conn.cursor()

    def getOneByOne(self):
        """
        逐个获取数据
        :return:
        """
        self.initConn()
        sql = "select * from table_name where id >= 0 AND (url is NULL or url=' ')"
        self.cursor.execute(sql)
        result =self.cursor.fetchone()
        # print result[1]
        return list(result)
        # return result

    def updateURLByID(self, com_id, com_url):
        """
        根据id更新URL
        :param com_id:
        :param com_url:
        :return:
        """
        self.initConn()
        if com_url == None:
            return 0
        sql = "update table_name set url = '%s' where id ='%s'" % (com_url,com_id)
        # param=(com_url,int(com_id))
        # print sql
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.conn.commit()
            print "update successful"
        except:
            # 发生错误时回滚
            # self.conn.rollback()
            print "update failed"
            # 关闭数据库连接
        self.conn.close()

    def insertRecords(self, items):
        self.initConn()
        sql = "insert into table_name(com_name, province, city, status) VALUES (%s,%s,%s,%s)"
        try:
            # 执行SQL语句
            self.cursor.executemany(sql, items)
            # 提交到数据库执行
            self.conn.commit()
            print "insert successful"
        except Exception, e:
            # 发生错误时回滚
            print e
            self.conn.rollback()
            print "insert failed"
        # 关闭数据库连接
        self.conn.close()


