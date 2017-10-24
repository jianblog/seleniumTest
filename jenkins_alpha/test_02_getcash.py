# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.testing_data import TestData
from pageobjects.jcj_recharge_page import RechargePage
from framework.logger import Logger


class CasePage(unittest.TestCase):
    """ 提现功能测试 """

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        time.sleep(1)

        cls.test_user = TestData.getRealUser()
        cls.recharge_page = RechargePage(cls.driver, str(cls.test_user['account']), 'qqq123456')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_cash_empty(self):
        """ 提现-> 金额为空 """
        pass

    def test_case_small(self):
        """ 提现-> 金额小于3元 """
        pass

    def test_case_float(self):
        """ 提现-> 金额小数位过多 """
        pass

    def test_cash_char(self):
        """ 提现-> 金额包含中文字符 """
        pass

    def test_cash_all(self):
        """ 提现-> 金额等于账户余额 """
        pass

    def test_cash_over(self):
        """ 提现-> 金额大于余额 """
        pass

    def test_sms1_empty(self):
        """ 提现-> 验证码为空 """
        pass

    def test_sms1_wrong(self):
        """ 提现-> 错误验证码 """
        pass

    def test_pay_empty(self):
        """ 提现-> 支付密码为空 """
        pass

    def test_pay_wrong(self):
        """ 提现-> 支付密码错误 """
        pass

    def test_sms2_empty(self):
        """ 提现-> 支付验证码为空 """
        pass

    def test_sms2_wrong(self):
        """ 提现-> 支付验证码错误 """
        pass

    def test_cash_ok(self):
        """ 提现-> 提现成功 """
        pass

