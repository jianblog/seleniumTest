# coding=utf-8
import time
import unittest
#from framework.base_page import BasePage
from framework.browser_engine import BrowserEngine
from pageobjects.testing_data import TestData
from pageobjects.jcj_tender_page import TenderPage
from framework.logger import Logger


class CasePage(unittest.TestCase):
    """ 投资功能测试 """

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
        self.tender_page.to_tender()
        self.tender_page.select_tender_item()
        self.tender_page.input_tender_money("")
        self.tender_page.click_tender_confirm()
        result = self.tender_page.get_money_warn()
        try:
            self.assertEqual("请输入投标金额!",result)
            print("Test pass，提示信息%s" % result)
        except Exception as e:
            self.get_window_img()
            print("Test Fail: ",result,"Exceptions:", format(e))
        finally:
            self.tenter_page.to_account() #进入投资理财页面
        
    def test_money_little(self):
        """ 投资-> 金额小于50 """
        self.tender_page.select_tender_item() #选择标的
        self.tender_page.input_tender_money("1") #输入投资金额
        self.tender_page.click_tender_confirm() #确认投资
        result = self.tender_page.get_money_warn() #错误提示
        try:
            self.assertEqual("投标金额不能低于50元!",result)
            print("Test pass，提示信息%s" % result)
        except Exception as e:
            self.get_window_img()
            print("Test Fail: ",result,"Exceptions:", format(e))
        finally:
            self.tenter_page.to_account() #进入投资理财页面
        
    def test_money_above(self):
        """ 投资-> 金额大于可投金额 """
        self.tender_page.select_tender_item() #选择标的
        s_money = self.tender_page.get_tender_available() #获取剩余可投金额
        money = s_money.replace(",","")  # 替换字符串中的内容
        t_money = float(money) + 1 
        self.tender_page.input_tender_money(t_money) #输入投资金额
        result = self.tender_page.get_money_warn() #错误提示
        try:
            self.assertIn("您输入的金额大于借款余额!",result)
            print("Test pass，提示信息%s" % result)
        except Exception as e:
            self.get_window_img()
            print("Test Fail: ",result,"Exceptions:", format(e))
        finally:
            self.tenter_page.to_account() #进入投资理财页面
        

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

