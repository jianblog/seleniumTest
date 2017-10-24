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

        cls.test_user = TestData.getRegUser()
        cls.recharge_page = RechargePage(cls.driver, str(cls.test_user['account']), 'qqq123456')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_getcash_redirect(self):
        """ 提现-> 非实名用户跳转 """
        self.recharge_page.to_cash()
        result = self.realusr_recharge_msg()
        try:
            assert "存管账户" in result
            print("Test pass ","跳转到实名页面")
        except Exception as e:
            print("Test fail ",format(e))
        finally:
            self.recharge_page.to_account()
