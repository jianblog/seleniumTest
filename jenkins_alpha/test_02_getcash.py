# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.testing_data import TestData
from pageobjects.jcj_getcash_page import GetcashPage

from framework.logger import Logger


class ViewCashPage(unittest.TestCase):
    """ 提现功能测试 """

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        time.sleep(1)

        cls.test_user = TestData.getRealUser()
        cls.cash_page = GetcashPage(cls.driver, str(cls.test_user['account']), 'qqq123456')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_cash_empty(self):
        """ 提现-> 金额为空 """
        self.cash_page.to_cash()

        self.cash_page.input_get_cash("")
        self.cash_page.click_cash_ready()
        result = self.cash_page.get_cash_warn()
        try:
            self.assertIn("请输入提现金额", result)
            print("Test Pass. 金额为空")
        except Exception as e:
            print("Test Fail, test_cash_empty.",format(e))
        finally:
            self.cash_page.to_account()

    def test_case_small(self):
        """ 提现-> 金额小于3元 """
        self.cash_page.to_cash()
       
        self.cash_page.input_get_cash("2")
        self.cash_page.click_cash_textarea()
        result = self.cash_page.get_cash_warn()

        try:
            self.assertIn("提现金额在3元以上", result)
            print("Test Pass. 金额小于3元")
        except Exception as e:
            self.cash_page.get_window_img()
            print("Test Fail, test_case_small.",format(e))
        finally:
            self.cash_page.to_account()

    def test_case_float(self):
        """ 提现-> 金额小数位过多 """
        self.cash_page.to_cash()

        self.cash_page.input_get_cash("102.4532")
        self.cash_page.input_verify_sms1("1234")
        result = self.cash_page.get_cash_warn()

        try:
            self.assertIn("请输入提现金额", result)
            print("Test Pass. 金额小数位数过多")
        except Exception as e:
            self.cash_page.get_window_img()
            print("Test Fail, test_case_float.", format(3))
        finally:
            self.cash_page.to_account()

    def test_cash_char(self):
        """ 提现-> 金额包含非数字字符 """
        self.cash_page.to_cash()

        self.cash_page.input_get_cash("e")
        self.cash_page.click_input_sms1()
        self.cash_page.click_cash_ready()
        result = self.cash_page.get_cash_warn()

        try:
            self.assertIn("请输入提现金额", result)
            print("Test Pass. 金额小数位数过多")
        except Exception as e:
            print("Test Fail, test_case_char", format(3))
        finally:
            self.cash_page.to_account()
        

    def test_cash_all(self):
        """ 提现-> 金额等于账户余额 """
        self.cash_page.to_cash()

        cash_str = self.cash_page.get_cash_available() 
        cash_account = cash_str[:-1]
        self.cash_page.input_get_cash(cash_account)
        self.cash_page.click_input_sms1()
        self.cash_page.click_cash_ready()
        result = self.cash_page.get_cash_warn()

        try:
            self.assertIn("最多能提现", result)
            print("Test Pass. 金额等于账户余额")
        except Exception as e:
            print("Test Fail, test_cash_all", format(e))
        finally:
            self.cash_page.to_account()

    def test_cash_over(self):
        """ 提现-> 金额大于余额 """
        self.cash_page.to_cash()

        cash_account = self.cash_page.get_cash_available()[:-1]
        cash_account = str(float(cash_account) + 1)
        self.cash_page.input_get_cash(cash_account)
        self.cash_page.click_input_sms1()
        self.cash_page.click_cash_ready()
        result = self.cash_page.get_cash_warn()

        try:
            self.assertIn("提现金额大于", result)
            print("Test Pass. 提现金额大于余额")
        except Exception as e:
            print("Test Fail, test_case_over.", format(e))
        finally:
            self.cash_page.to_account()

    def test_sms1_empty(self):
        """ 提现-> 验证码为空 """
        self.cash_page.to_cash()

        self.cash_page.input_get_cash("50")
        self.cash_page.click_cash_sms1()
        # 两次关闭短信提示窗
        time.sleep(1)
        alert = self.cash_page.getAlertMsg() 
        time.sleep(1)
        alert = self.cash_page.getAlertMsg()
        self.cash_page.input_verify_sms1("")
        self.cash_page.click_cash_ready()
        result = self.cash_page.get_sms1_warn()

        try:
            self.assertIn("请输入短信验证码",result)
            print("Test Pass. 验证码为空")
        except Exception as e:
            self.cash_page.get_window_img()
            print("Test Fail, test_sms1_empty.", format(e))
        finally:
            self.cash_page.to_account()

    def test_sms1_wrong(self):
        """ 提现-> 错误验证码 """
        self.cash_page.to_cash()

        self.cash_page.input_get_cash("50")
        self.cash_page.click_cash_sms1()
        # 两次关闭短信提示窗
        time.sleep(1)
        alert = self.cash_page.getAlertMsg()
        time.sleep(1)
        alert = self.cash_page.getAlertMsg()

        self.cash_page.input_verify_sms1("1111")
        self.cash_page.click_cash_textarea()
        #self.cash_page.click_cash_ready()
        result = self.cash_page.get_sms1_warn()

        try:
            self.assertIn("验证码校验失败",result)
            print("Test Pass. 验证码错误")
        except Exception as e:
            print("Test Fail, test_sms1_wrong.", format(e))
        finally:
            self.cash_page.to_account()

    def test_pay_empty(self):
        """ 提现-> 支付密码为空 """
        self.cash_page.to_cash()

        self.cash_page.input_get_cash("50")
        self.cash_page.click_cash_sms1()
        time.sleep(1)
        alert = self.cash_page.getAlertMsg()
        time.sleep(1)
        msg = self.cash_page.getAlertMsg()[-6:]

        self.cash_page.input_verify_sms1(msg)
        self.cash_page.click_cash_textarea()
        self.cash_page.click_cash_ready()
        self.cash_page.wait(3)
        self.cash_page.click_cash_confirm()
        time.sleep(1)
        result = self.cash_page.getAlertMsg()

        try:
            self.assertIn("请输入支付密码!",result)
            print("Test Pass. 支付密码为空")
        except Exception as e:
            self.cash_page.get_window_img()
            print("Test Fail, test_pay_empty.", format(e))
        finally:
            self.cash_page.to_account()

    def test_pay_wrong(self):
        """ 提现-> 支付密码错误 """
        pass

    def test_sms2_empty(self):
        """ 提现-> 支付验证码为空 """
        self.cash_page.to_cash()

        self.cash_page.input_get_cash("50")
        self.cash_page.click_cash_sms1()
        time.sleep(1)
        alert = self.cash_page.getAlertMsg()
        msg = self.cash_page.getAlertMsg()[-6:]

        self.cash_page.input_verify_sms1(msg)
        self.cash_page.click_cash_textarea()
        self.cash_page.click_cash_ready()
        self.cash_page.wait(3)

        self.cash_page.input_pay_code(self.test_user['account'][-6:])
        self.cash_page.click_cash_confirm()
        result = self.cash_page.getAlertMsg()

        try:
            self.assertIn("请输入短信验证码!",result)
            print("Test Pass. 支付验证码为空")
        except Exception as e:
            print("Test Fail, test_sms2_empty.", format(e))
        finally:
            self.cash_page.to_account()
        
    def test_sms2_wrong(self):
        """ 提现-> 支付验证码错误 """
        self.cash_page.to_cash()

        self.cash_page.input_get_cash("50")
        self.cash_page.click_cash_sms1()
        time.sleep(1)
        alert = self.cash_page.getAlertMsg()
        msg = self.cash_page.getAlertMsg()[ -6: ]

        self.cash_page.input_verify_sms1(msg)
        self.cash_page.click_cash_textarea()
        self.cash_page.click_cash_ready()
        self.cash_page.wait(5)

        self.cash_page.input_pay_code(self.test_user[ 'account' ][ -6: ])
        self.cash_page.wait(2)
        self.cash_page.click_cash_sms2()
        alert = self.cash_page.getAlertMsg()
        self.cash_page.wait(2)
        self.cash_page.input_verify_sms2("0001")
        self.cash_page.click_cash_confirm()
        #time.sleep(3)
        #self.cash_page.wait(5)
        alert = self.cash_page.getAlertMsg()
        #self.cash_page.wait(5)
        #time.sleep(3)
        result = self.cash_page.getAlertMsg()
        print("result:", result)

        try:
            self.assertIn("短信验证码错误", result)
            print("Test Pass. 支付验证码错误")
        except Exception as e:
            print("Test Fail, test_sms2_wrong.", format(e))
        finally:
            self.cash_page.to_account()

    def test_cash_ok(self):
        """ 提现-> 提现成功 """
        pass

