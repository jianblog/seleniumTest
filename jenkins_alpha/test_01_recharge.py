# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.testing_data import TestData
from pageobjects.jcj_recharge_page import RechargePage
from framework.logger import Logger


logger = Logger(logger = "BrowserEngine").getlog()


class ViewRechargePage(unittest.TestCase):
    """ 充值功能测试 """
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        time.sleep(1)

        cls.test_user = TestData.getRealUser()
        cls.recharge_page = RechargePage(cls.driver, str(cls.test_user['account']), 'qqq123456')
        
    @classmethod
    def tearDownClass(cls):
        #cls.driver.quit()
        pass


    def test_money_zero(self):
        """    充值-> 金额为0 """
        self.recharge_page.to_recharge()
        self.recharge_page.input_recharge_money(0)
        self.recharge_page.click_recharge_ready()

        result = self.recharge_page.get_recharge_msg()

        try:
            self.assertEqual("充值金额不能为空或者0", result)
            print("Test Pass. 充值金额为0！")
            #self.driver.refresh() # 刷新方法 refresh
        except Exception as e:
            print("Test Fail: ",result,"Exceptions:", format(e))
        finally:
            self.recharge_page.to_account()

    def test_money_empty(self):
        """    充值-> 金额为空 """
        self.recharge_page.to_recharge()
        self.recharge_page.input_recharge_money("")
        self.recharge_page.click_bank_default()

        result = self.recharge_page.get_recharge_msg()

        try:
            self.assertIn("充值金额不能为空或者0", result)
            print("Test Pass. 充值金额为空")
        except Exception as e:
            print("Test Fail: ", result, " Exceptions:", format(e))
        finally:
            self.recharge_page.to_account()

    def test_money_bad(self):
        """    充值-> 金额为非法字符 """
        self.recharge_page.to_recharge()
        self.recharge_page.input_recharge_money("！@#")
        self.recharge_page.click_bank_default()

        try:
            result = self.recharge_page.get_recharge_money()
            assert "！@#" not in result
            print("Test Pass. 金额非法")
        except Exception as e:
            print("Test Fail, Exceptions:", format(e))
        finally:
            self.recharge_page.to_account()
        

    def test_phone_bad(self):
        """    充值-> 手机号非非法字符 """
        self.recharge_page.to_recharge()
        self.recharge_page.input_recharge_money("1005.56")
        self.recharge_page.click_bank_default()
        self.recharge_page.click_recharge_ready()

        #
        self.recharge_page.input_recharge_phone("！@#12321")
        self.recharge_page.click_get_sms()
        time.sleep(3)
        result = self.recharge_page.getAlertMsg()

        try:
            assert "手机号为空或格式不正确" in result
            print("Test pass.预留手机号格式不正确")
            self.recharge_page.wait(10)
        except Exception as e:
            print("Test Fail, Exceptions:", format(e))

        finally:
            self.recharge_page.to_account()

    def test_phone_empty(self):
        """    充值-> 预留手机号为空 """
        self.recharge_page.to_recharge()
        self.recharge_page.input_recharge_money("1005.56")
        self.recharge_page.click_bank_default()
        self.recharge_page.click_recharge_ready()

        self.recharge_page.input_recharge_phone("")
        self.recharge_page.click_get_sms()
        result = self.recharge_page.getAlertMsg()

        try:
            assert "手机号为空或格式不正确" in result
            print("Test pass.预留手机号为空")
        except Exception as e:
            print("Test Fail, Exceptions:", format(e))
        finally:
            self.recharge_page.to_account()

    def test_verify_empty(self):
        """    充值-> 验证码为空 """
        self.recharge_page.to_recharge()
        self.recharge_page.input_recharge_money("1005.56")
        self.recharge_page.click_bank_default()
        self.recharge_page.click_recharge_ready()

        self.recharge_page.input_recharge_phone(self.test_user['account'])
        self.recharge_page.click_recharge_confirm()

        try:
            result = self.recharge_page.getAlertMsg()
            assert "请输入短信验证码!" in result
            print("Test pass.验证码为空")
        except Exception as e:
            print("Test Fail, Exceptions:", format(e))
        finally:
            self.recharge_page.to_account()

    def test_verify_wrong(self):
        """    充值-> 验证码错误 """
        self.recharge_page.to_recharge()
        self.recharge_page.input_recharge_money("1005.56")
        self.recharge_page.click_bank_default()
        self.recharge_page.click_recharge_ready()

        self.recharge_page.input_recharge_phone(self.test_user['account'])
        self.recharge_page.click_get_sms()
        time.sleep(5)
        alert = self.recharge_page.getAlertMsg()
        self.recharge_page.input_verify_code("1111")

        self.recharge_page.click_recharge_confirm()
        alert =  self.recharge_page.getAlertMsg()

        # need wait alert windows pop
        time.sleep(3)
        try:
            result = self.recharge_page.getAlertMsg()
            self.recharge_page.get_window_img()
            assert "验证码失效或错误" in result
            print("Test Pass. 验证码错误")
        except Exception as e:
            print("Test Fail, Exceptions:", format(e))
        finally:
            self.recharge_page.to_account()
            self.recharge_page.wait(5)
            pass

    def test_recharge_protocol(self):
        """    充值-> 未选支付协议 """
        self.recharge_page.to_recharge()
        self.recharge_page.input_recharge_money("1005.56")
        self.recharge_page.click_bank_default()
        self.recharge_page.click_recharge_ready()

        self.recharge_page.input_recharge_phone(self.test_user['account'])
        self.recharge_page.click_get_sms()
        time.sleep(5)
        alert = self.recharge_page.get_alertmsg()
        self.recharge_page.input_verify_code("0000")
        self.recharge_page.select_protocol()

        self.recharge_page.click_recharge_confirm()

        try:
            result =  self.recharge_page.getAlertMsg()
            assert "请阅读并同意《支付服务协议》!" in result
            print("Test Pass. 取消选择支付协议")
        except Exception as e:
            print("Test Fail, Exceptions:", format(e))
        finally:
            self.recharge_page.to_account()
            self.recharge_page.wait(5)

    def test_recharge_ok(self):
        """    充值-> 充值成功 """
        self.recharge_page.to_recharge()
        self.recharge_page.input_recharge_money("1005.56")
        self.recharge_page.click_bank_default()
        self.recharge_page.click_recharge_ready()

        self.recharge_page.input_recharge_phone(self.test_user['account'])
        self.recharge_page.click_get_sms()
        time.sleep(5)
        alert = self.recharge_page.getAlertMsg()
        self.recharge_page.input_verify_code("0000")
        self.recharge_page.click_recharge_confirm()
        alert =  self.recharge_page.getAlertMsg()

        try:
            self.recharge_page.wait(8)
            result = self.recharge_page.get_recharge_msg()
            assert "交易成功" in result
            print("Test Pass. 充值成功")
        except Exception as e:
            print("Test Fail, Exceptions:", format(e))
        finally:
            self.recharge_page.to_account()
            self.recharge_page.wait(5)
