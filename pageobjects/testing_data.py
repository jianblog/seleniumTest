# coding = utf-8

"""
测试用例使用用户账号数据源

"""
import os
import sys
import datetime
#import xlrd, xlsxwriter
import mysql.connector
from framework.logger import Logger

# create a logger instance
logger =Logger(logger="BasePage").getlog()


class TestData(object):
    dbstring = {
        'user': 'dfhxp2p',
        'password': 'powerp0p',
        'host': 'ali.dev',
        'port': '3306',
        'database': 'test'
    }


    def popUser(self, user_file):
        """
        Using external EXCEL file as user sources
        :param user_file:
        :return:
        """
        userbook = xlrd.open_workbook(user_file)
        userDatas = userbook.sheet_by_index(0)
        if userDatas.nrows > 0:
            self.userTest = userDatas.row_values(-1)

            workbook = xlsxwriter.Workbook(user_file)
            sheet = workbook.add_worksheet()
            for i in range(userDatas.nrows - 1):
                sheet.write_row(i, 0, userDatas.row_values(i))
            workbook.close()
        else:
            self.userTest = None

    @staticmethod
    def __dbQuery(sql):
        cn = mysql.connector.connect(user=TestData.dbstring['user'],
                          password=TestData.dbstring['password'],
                          host=TestData.dbstring['host'],
                          port=TestData.dbstring['port'],
                          database=TestData.dbstring['database'])
        cursor = cn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            raise Exception("No available testing user:" + sql)
        cn.close()
        user = {
                "account": result[0][0],
                "realname": result[0][1],
                "idnum": result[0][2],
                "banknum": result[0][3]
               }
        print(user)
        return user

    @staticmethod
    def __dbUpdate(sql):
        cn = mysql.connector.connect(user=TestData.dbstring['user'],
                          password=TestData.dbstring['password'],
                          host=TestData.dbstring['host'],
                          port=TestData.dbstring['port'],
                          database=TestData.dbstring['database'])
        cursor = cn.cursor()
        try:
            cursor.execute(sql)
            cn.commit()
        except Exception as e:
            logger.error("user status updated fails: " + sql )
        finally:
            cn.close()

    @staticmethod
    def getFreshUser():
        sql = "select account, realname, idnum, cardnum from test_jcj_user where type is null  order by rand() limit 2"
        return TestData.__dbQuery(sql)

    @staticmethod
    def getRegUser():
        sql = "select account, realname, idnum, cardnum from test_jcj_user  where type=1 order by rand() limit 2"
        return TestData.__dbQuery(sql)

    @staticmethod
    def getRealUser():
        dt = datetime.datetime.now()
        ymd = str(dt.year) + str(dt.month) + str(dt.day)
        sql = "select account, realname, idnum, cardnum from test_jcj_user  where type=2 and (limitday <> '" + ymd + "' or limitday is null) order by rand()"
        return TestData.__dbQuery(sql)

    @staticmethod
    def changetoReged(mobile):
        sql = "update test_jcj_user set type=1 where account='" + str(mobile) + "'"
        TestData.__dbUpdate(sql)

    @staticmethod
    def changetoRealed(mobile):
        sql = "update test_jcj_user set type=2 where type=1 and account='" + str(mobile) + "'"
        TestData.__dbUpdate(sql)

    @staticmethod
    def inactiveUser(mobile):
        dt = datetime.datetime.now()
        ymd = str(dt.year) + str(dt.month) + str(dt.day)
        sql = "update test_jcj_user set limitday=ymd where account='" + str(mobile) + "'"
        TestData.__dbUpdate(sql)
