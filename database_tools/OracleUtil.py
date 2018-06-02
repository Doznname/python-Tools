# encoding=utf-8
# author: haven

import cx_Oracle
import os

class OracleUtil(object):
    """
       连接oracle工具类
       """
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'  # 或者
    # os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AL32UTF8'
    host = "192.168.43.246"
    username = "odsuser"
    password = "odsuser"
    dbname = "ciicods"
    port = "1521"
    dsn = cx_Oracle.makedsn(host, port, dbname)
    connection = cx_Oracle.connect(username, password, dsn)
    cursor = connection.cursor()

    def getOneByOne(self):
        """
        逐个获取数据
        :return:
        """
        # self.initConn()
        sql = "select * from test_01 where id >= 0 AND (url is NULL or url=' ')"
        self.cursor.execute(sql)
        result =self.cursor.fetchone()
        return list(result)
        # return result

    def updateURLByID(self, com_id, com_url):
        """
        根据id更新URL
        :param com_id:
        :param com_url:
        :return:
        """
        # self.initConn()
        if com_url == None:
            return 0
        sql = "update test_01 set url = '%s' where id ='%s'" % (com_url,com_id)
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
        sql = "insert into company_name01(com_name, province, city, status) VALUES (%s,%s,%s,%s)"
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

    def updateStatusByID(self, com_id, status):
        """
        根据id更新URL
        :param com_id:
        :param com_url:
        :return:
        """
        self.initConn()
        sql = "update region set status = '%s' where id = '%d'" % (status, com_id)
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.conn.commit()
            print "update successful"
        except:
            # 发生错误时回滚
            print
            self.conn.rollback()
            print "update failed"
        # 关闭数据库连接
        self.conn.close()