# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.testing_data import TestData
from pageobjects.jcj_getcash_page import GetcashPage
from framework.logger import Logger


class CasePage_abn(unittest.TestCase):
    """ 非实名用户 提现功能测试 """

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        time.sleep(1)

        cls.test_user = TestData.getRegUser()
        cls.cash_page = GetcashPage(cls.driver, str(cls.test_user['account']), 'qqq123456')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_getcash_redirect(self):
        """ 提现-> 非实名用户跳转 """
        self.cash_page.to_cash()
        result = self.cash_page.get_redirect_msg()
        try:
            assert "存管账户" in result
            print("Test pass ","跳转到实名页面")
        except Exception as e:
            print("Test fail ",format(e))
        finally:
            self.cash_page.to_account()
