# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.testing_data import TestData
from pageobjects.jcj_login_page import LoginPage
from framework.logger import Logger


logger = Logger(logger = "BrowserEngine").getlog()


class ViewLoginPage(unittest.TestCase):
    """     登陆功能测试 """
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        time.sleep(1)
        cls.login_page = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        #cls.driver.quit()
        pass

    def test_login_all_empty(self):
        """    登录-> 用户名和密码为空 """
        #login_page = LoginPage(self.driver)
        self.login_page.input_account("")
        self.login_page.input_password("")
        self.login_page.click_login()
        
        result = self.login_page.fail_login_message().text
        try:
            self.assertEqual("用户名为空",result)
            print("Test Pass. 用户名,密码空值验证！")
            self.driver.refresh() # 刷新方法 refresh
        except Exception as e:
            print("Test Fail. ",format(e))

    def test_login_account_empty(self):
        """    登录-> 用户名为空 """
        self.login_page.input_account("")
        self.login_page.input_password("qqq123456")
        self.login_page.click_login()

        result = self.login_page.fail_login_message().text
        try:
            self.assertEqual("用户名为空",result)
            print("Test Pass. 用户名空值验证！")
            self.driver.refresh() # 刷新方法 refresh
        except Exception as e:
            print("Test Fail. ",format(e))

    def test_login_password_empty(self):
        """    登录-> 密码为空 """
        self.login_page.input_account("18610770004")
        self.login_page.input_password("")
        self.login_page.click_login()

        result = self.login_page.fail_login_message().text
        try:
            self.assertEqual("密码为空",result)
            print("Test Pass. 密码空值验证！")
            self.driver.refresh() # 刷新方法 refresh
        except Exception as e:
            print("Test Fail. ",format(e))

    def test_login_wrong(self):
        """    登录-> 用户名或密码错误 """
        self.login_page.input_account("18610770004")
        self.login_page.input_password("123456")
        self.login_page.click_login()
        
        result = self.login_page.fail_login_message().text
        try:
            self.assertEqual("用户名或密码错误", result)
            print("Test Pass. 错误用户名或密码验证!")
            self.driver.refresh()
        except Exception as e:
            print("Test Fail. ", format(e))

    def test_login_ok(self):
        """    登录-> 用户名和密码正确 """
        test_user = TestData.getRealUser()

        self.login_page.input_account(test_user['account'])
        self.login_page.input_password("qqq123456")
        self.login_page.click_login()

        result = self.login_page.success_login_message().text 
        try:
            self.assertIn("Hello",result)
            print("Test Pass. 登录成功！")
            #self.driver.refresh() # 刷新方法 refresh
        except Exception as e:
            print("Test Fail. ",format(e))

        self.login_page.logout()
        self.login_page.to_login()

