# coding = utf-8

from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.testing_data import TestData
from pageobjects.jcj_login_page import LoginPage
#from selenium.webdriver.support.select import Select
import unittest
import time
import json
import os


class GetcashPage(BasePage):

    def __init__(self, driver, account, password):
        super(RechargePage, self).__init__(driver)
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "elements_nav.json"),"r", encoding="utf-8") as f:
            self.map_nav = json.load(f)
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "elements_cash.json"),"r", encoding="utf-8") as f:
            self.map_cash = json.load(f)

        # initial goto login page
        login_page = LoginPage(driver)
        login_page.input_account(account)
        login_page.input_password(password)
        login_page.click_login()

        # after login, goto account page
        self.to_account()
        
    def to_account(self):
        self.gotoUrl("http://jingchujie.dev/acct/index.html")
        time.sleep(2)

    def to_cash(self):
        self.click(self.map_cash['link_getcash'])
        time.sleep(2)

    def input_get_cash(self, money):
        self.typeIn(self.map_cash['input_getcash_money'], money)

    def get_cash_available(self):
        element = self.find_the_element(self.map_cash['text_cash_available'])
        return element.text

    def get_cash_warn(self):
        element = self.find_the_element(self.map_cash['message_cash_warn'])
        msg = element.text
        return msg

    def click_cash_sms1(self):
        self.click(self.map_cash['button_get_sms1'])

    def input_verify_sms1(self, code):
        self.typeIn(self.map_cash['input_sms_code1'], code)

    def get_verify_message1(self):
        element = self.find_the_element(self.map_cash['message_verify_sms'])
        return element.text

    def click_cash_ready(self):
        self.click(self.map_cash['button_get_cash'])
        time.sleep(2)

    # next page
    def input_zhifu_code(self, code):
        self.typeIn(self.map_cash['input_pay_code'], code)

    def click_cash_sms2(self):
        self.click(self.map_cash['button_get_sms2'])

    def input_verify_sms2(self, code):
        self.typeIn(self.map_cash['input_sms_code2'], code)

    def click cash_confirm(self):
        self.click(self.map_cash['button_cash_confirm'])
