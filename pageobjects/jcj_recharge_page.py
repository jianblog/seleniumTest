# coding = utf-8

from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.testing_data import TestData
from pageobjects.jcj_login_page import LoginPage
from selenium.webdriver.support.select import Select
import unittest
import time
import json
import os


class RechargePage(BasePage):

    def __init__(self, driver, account, password):
        super(RechargePage, self).__init__(driver)
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "elements_nav.json"),"r", encoding="utf-8") as f:
            self.map_nav = json.load(f)
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "elements_recharge.json"),"r", encoding="utf-8") as f:
            self.map_recharge = json.load(f)

        # initial goto login page
        login_page = LoginPage(driver)
        login_page.input_account(account)
        login_page.input_password(password)
        login_page.click_login()

        # after login, goto account page
        self.to_account()
        

    def to_account(self):
        #element = self.find_the_element(self.map_nav['nav_account'])
        #self.click(self.map_nav['nav_account'])
        self.gotoUrl("http://jingchujie.dev/acct/index.html")
        #element.click()
        time.sleep(2)

    def to_recharge(self):
        #element = self.find_the_element(self.map_recharge['page_account']['link_recharge'])
        self.click(self.map_recharge['link_recharge'])
        #element.click()
        time.sleep(2)

    def input_recharge_money(self, money):
        #element = self.find_the_element(self.map_recharge['page_account']['input_recharge_money'])
        self.typeIn(self.map_recharge['input_recharge_money'], money)
        #element.send_keys(money)

    def get_recharge_money(self):
        element = self.find_the_element(self.map_recharge['input_recharge_money'])
        return element.text

    def click_bank_default(self):
        self.click(self.map_recharge['select_bankno'])

    def click_recharge_ready(self):
        #element = self.find_the_element(self.map_recharge['page_account']['button_recharge_ready'])
        #element.click()
        self.click(self.map_recharge['button_recharge_ready'])

    def get_recharge_msg(self):
        element = self.find_the_element(self.map_recharge['window_recharge_notice'])
        msg = element.text

        # get message and close it
        element = self.find_the_element(self.map_recharge['window_recharge_confirm'])
        element.click()

        return msg

    def input_recharge_phone(self, phone):
        #element = self.find_the_element(self.map_recharge['page_account']['input_recharge_phone'])
        #element.send_keys(phone)
        self.typeIn(self.map_recharge['input_recharge_phone'], phone)

    def click_get_sms(self):
        #element = self.find_the_element(self.map_recharge['page_account']['button_get_sms'])
        #element.click()
        self.click(self.map_recharge['button_get_sms'])

    def input_verify_code(self, code):
        #element = self.find_the_element(self.map_recharge['page_account']['input_verify_code'])
        #element.send_keys(code)
        self.typeIn(self.map_recharge['input_verify_code'], code)

    def select_protocol(self):
        self.click(self.map_recharge['check_recharge_protocol'])

    def click_recharge_confirm(self):
        #element = self.find_the_element(self.map_recharge['page_account']['button_recharge_confirm'])
        #element.click()
        self.click(self.map_recharge['button_recharge_confirm'])
        time.sleep(2)

    def get_redirect_msg(self):
        return self.find_the_element(self.map_recharge['message_recharge_redirect']).text

