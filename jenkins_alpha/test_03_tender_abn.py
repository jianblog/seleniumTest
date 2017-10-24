# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.testing_data import TestData
from pageobjects.jcj_tender_page import TenderPage
from framework.logger import Logger


class CasePage(unittest.TestCase):
    """ 提现功能测试 """

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        time.sleep(1)

        cls.test_user = TestData.getRealUser()
        cls.tender_page = TenderPage(cls.driver, str(cls.test_user['account']), 'qqq123456')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_money_empty(self):
        """ 投资-> 金额为0 """
        pass

    def test_money_little(self):
        """ 投资-> 金额小于50 """
        pass

    def test_money_above(self):
        """ 投资-> 金额大于可投金额 """
        pass

    def test_sms_wrong(self):
        """ 投资-> 验证码错误 """
        pass

    def test_coupons_cash_above(self):
        """ 投资-> 投资金额+代金券大于剩余可投金额 """
        pass

    def test_money_only(self):
        """ 投资-> 不用代金券等 """
        pass

    def test_with_coupons_cash(self):
        """ 投资-> 用代金券 """
        pass

    def test_with_coupons_rate(self):
        """ 投资-> 用加息劵 """
        pass

    def test_with_coupons_both(self):
        """ 投资-> 同时用两种劵 """
        pass

