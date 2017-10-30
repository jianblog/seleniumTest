# coding = utf-8

from framework.browser_engine import BrowserEngine
from pageobjects.testing_data import TestData
from pageobjects.jcj_recharge_page import RechargePage
from frame.logger import Logger

import time
import unittest

logger = Logger(logger = "BrowserEngine").getlog()


class ViewRegisterPage(unittest.TestCase):
    """ 注册功能测试 """

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        
        cls.test_user = TestData.getNewUser()
        cls.register_page = RegisterPage(cls.driver)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    def test_phone_empty(self):
        """ 注册-> 手机号为空 """
        pass

    def test_phone_char(self):
        """ 注册-> 手机含非法字符 """
        pass

    def test_phone_short(self):
        """ 注册-> 手机号长度不足 """
        pass

    def test_phone_exist(self):
        """ 注册-> 手机号已注册 """
        pass

    def test_pwd_short(self):
        """ 注册-> 密码长度不足6位 """
        pass

    def test_pwd_long(self):
        """ 注册-> 密码长度大于16 """
        pass

    def test_pwd_numonly(self):
        """ 注册-> 密码仅为数字 """
        pass

    def test_pwd_abconly(self):
        """ 注册-> 密码仅为字母 """
        pass

    def test_pwd_empty(self):
        """ 注册-> 密码为空 """
        pass

    def test_sms_empty(self):
        """ 注册-> 短信验证码为空 """
        pass

    def test_sms_wrong(self):
        """ 注册-> 短信验证码错误 """
        pass

    def test_no_protocol(self):
        """ 注册-> 注册协议未选 """
        pass

    def test_reg_ok(self):
        """ 注册-> 注册成功 """
        pass
    

