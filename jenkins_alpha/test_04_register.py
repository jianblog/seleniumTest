# coding = utf-8

from framework.browser_engine import BrowserEngine
from pageobjects.testing_data import TestData
from pageobjects.jcj_register_page import RegisterPage
from framework.logger import Logger

import time
import unittest

logger = Logger(logger = "BrowserEngine").getlog()


class ViewRegisterPage(unittest.TestCase):
    """ 注册功能测试 """

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.test_user = TestData.getNewUser()
        cls.driver = browse.open_browser(cls)
        cls.register_page = RegisterPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_phone_empty(self):
        """ 注册-> 手机号为空 """
        self.register_page.input_reg_phone("")
        self.register_page.click_reg_confirm()
        try:
            result = self.register_page.get_phone_warn()
            self.assertIn("请输入手机号码", result)
            print("Test Pass. test_phone_empty")
        except Exception as e:
            print("Test Fail, test_phone_empty", format(e))
        finally:
            self.register_page.to_register()

    def test_phone_char(self):
        """ 注册-> 手机含非法字符 """
        self.register_page.input_reg_phone("hello")
        self.register_page.input_reg_password("")
        try:
            result = self.register_page.get_phone_warn()
            self.assertIn("手机号输入有误", result)
            print("Test Pass. test_phone_char")
        except Exception as e:
            print("Test Fail, test_phone_char", format(e))
        finally:
            self.register_page.to_register()

    def test_phone_short(self):
        """ 注册-> 手机号长度不足 """
        self.register_page.input_reg_phone("138000100")
        self.register_page.input_reg_password("")
        try:
            result = self.register_page.get_phone_warn()
            self.assertIn("手机号输入有误", result)
            print("Test Pass. test_phone_short")
        except Exception as e:
            print("Test Fail, test_phone_short", format(e))
        finally:
            self.register_page.to_register()

    def test_phone_exist(self):
        """ 注册-> 手机号已注册 """
        test_user = TestData.getRegUser()
        self.register_page.input_reg_phone(test_user['account'])
        self.register_page.input_reg_password("")
        try:
            result = self.register_page.get_phone_warn()
            self.assertIn("该手机号码已经存在", result)
            print("Test Pass. test_phone_exist")
        except Exception as e:
            print("Test Fail, test_phone_exist", format(e))
        finally:
            self.register_page.to_register()

    def test_pwd_short(self):
        """ 注册-> 密码长度不足6位 """
        self.register_page.input_reg_phone(self.test_user['account'])
        self.register_page.input_reg_password("qq123")
        self.register_page.click_reg_confirm()
        try:
            result = self.register_page.get_password_warn()
            self.assertIn("密码要由", result)
            print("Test Pass. test_pwd_short")
        except Exception as e:
            print("Test Fail, test_pwd_short", format(e))
        finally:
            self.register_page.to_register()

    def test_pwd_long(self):
        """ 注册-> 密码长度大于16 """
        self.register_page.input_reg_phone(self.test_user['account'])
        self.register_page.input_reg_password("qqq123123123123123")
        self.register_page.click_reg_confirm()
        try:
            result = self.register_page.get_password_warn()
            self.assertIn("密码要由", result)
            print("Test Pass. test_pwd_long")
        except Exception as e:
            print("Test Fail, test_pwd_long", format(e))
        finally:
            self.register_page.to_register()

    def test_pwd_numonly(self):
        """ 注册-> 密码仅为数字 """
        self.register_page.input_reg_phone(self.test_user['account'])
        self.register_page.input_reg_password("1234567")
        self.register_page.click_reg_confirm()
        try:
            result = self.register_page.get_password_warn()
            self.assertIn("密码要由", result)
            print("Test Pass. test_pwd_numonly")
        except Exception as e:
            print("Test Fail, test_pwd_numonly", format(e))
        finally:
            self.register_page.to_register()
        

    def test_pwd_abconly(self):
        """ 注册-> 密码仅为字母 """
        self.register_page.input_reg_phone(self.test_user['account'])
        self.register_page.input_reg_password("qqqabcd")
        self.register_page.click_reg_confirm()
        try:
            result = self.register_page.get_password_warn()
            self.assertIn("密码要由", result)
            print("Test Pass. test_pwd_abconly")
        except Exception as e:
            print("Test Fail, test_pwd_abconly", format(e))
        finally:
            self.register_page.to_register()


    def test_pwd_empty(self):
        """ 注册-> 密码为空 """
        self.register_page.input_reg_phone(self.test_user['account'])
        self.register_page.input_reg_password("")
        self.register_page.click_reg_confirm()
        try:
            result = self.register_page.get_password_warn()
            self.assertIn("密码要由", result)
            print("Test Pass. test_pwd_empty")
        except Exception as e:
            print("Test Fail, test_pwd_empty", format(e))
        finally:
            self.register_page.to_register()

    def test_sms_empty(self):
        """ 注册-> 短信验证码为空 """
        self.register_page.input_reg_phone(self.test_user['account'])
        self.register_page.input_reg_password("qqq123456")
        self.register_page.click_reg_confirm()
        try:
            result = self.register_page.get_verify_warn()
            self.assertIn("请输入短信验证码",result)
            print("Test Pass. test_sms_empty")
        except Exception as e:
            print("Test Fail, test_sms_empty", format(e))
        finally:
            self.register_page.to_register()
        

    def test_sms_wrong(self):
        """ 注册-> 短信验证码错误 """
        self.register_page.input_reg_phone(self.test_user['account'])
        self.register_page.input_reg_password("qqq123456")
        self.register_page.click_get_sms()
        alert = self.register_page.getAlertMsg()
        alert = self.register_page.getAlertMsg()
        self.register_page.input_verify_code("123456")
        self.register_page.click_reg_confirm()
        try:
            result = self.register_page.get_verify_warn()
            self.assertIn("验证码校验失败",result)   
            print("Test Pass. test_sms_wrong")
        except Exception as e:
            print("Test Fail, test_sms_wrong", format(e))
        finally:
            self.register_page.to_register()
        

    def test_no_protocol(self):
        """ 注册-> 注册协议未选 """
        self.register_page.input_reg_phone(self.test_user['account'])
        self.register_page.input_reg_password("qqq123456")
        self.register_page.click_get_sms()
        alert = self.register_page.getAlertMsg()
        msg = self.register_page.getAlertMsg()
        code = msg.split("：")[1]
        self.register_page.input_verify_code(code)
        self.register_page.click_reg_confirm()
        try:
            result = self.register_page.getAlertMsg()
            self.assertIn("同意", result)
            print("Test Pass. test_no_protocol")
        except Exception as e:
            print("Test Fail, test_no_protocol", format(e))
        finally:
            self.register_page.to_register()


    def test_zreg_ok(self):
        """ 注册-> 注册成功 """
        self.register_page.input_reg_phone(self.test_user['account'])
        self.register_page.input_reg_password("qqq123456")
        self.register_page.click_get_sms()
        alert = self.register_page.getAlertMsg()
        msg = self.register_page.getAlertMsg()
        code = msg.split("：")[1]
        self.register_page.input_verify_code(code)
        self.register_page.check_reg_protocol()
        self.register_page.click_reg_confirm()
        try:
            result = self.register_page.get_regok_msg()
            self.assertIn("存管", result)
            print("Test Pass. test_zreg_ok")
            TestData.changetoReged(self.test_user['account'])
        except Exception as e:
            print("Test Fail, test_zreg_ok", format(e))
        finally:
            #self.register_page.logout()
            #self.register_page.to_register() 
            pass  # this test case always run at the end. dont cleanup

