# coding = utf-8

from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.testing_data import TestData
from pageobjects.jcj_login_page import LoginPage
import unittest
import time
import json
import os


class TenderPage(BasePage):

    def __init__(self, driver, account, password):
        super(RechargePage, self).__init__(driver)
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "elements_nav.json"),"r", encoding="utf-8") as f:
            self.map_nav = json.load(f)
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "elements_tender.json"),"r", encoding="utf-8") as f:
            self.map_tender = json.load(f)

        # initial goto login page
        login_page = LoginPage(driver)
        login_page.input_account(account)
        login_page.input_password(password)
        login_page.click_login()

        # after login, goto account page
        self.to_tender()


    def to_tender(self):
        self.gotoUrl("http://jingchujie.dev/licai.html")
        time.sleep(2)

    def select_tender_item(self):
        self.click(self.map_tender['link_tender_item'])

    def get_tender_available(self):
        return self.find_the_element(self.map_tender['text_tender_avaliable']).text

    def get_cash_avaliable(self):
        return self.find_the_element(self.map_tender['text_cash_available']).text

    def input_tender_money(self, money):
        self.typeIn(self.map_tender['input_tender_money'], money)

    def get_money_warn(self):
        return self.find_the_element(self.map_tender['message_money_warn']).text

    def get_tender_sms(self):
        self.click(self.map_tender['button_get_sms'])

    def input_verify_sms(self, code):
        self.typeIn(self.map_tender['input_sms_code'], code)

    def get_sms_warn(self):
        return self.find_the_element(self.map_tender['message_sms_verify']).text

    def click_tender_confirm(self):
        self.click(self.map_tender['button_tender_confirm'])

    def use_coupons_cash(self):
        self.click(self.map_tender['list_coupons'])
        element = self.find_the_element(self.map_tender['coupons_cash'])
        element[1].click()
        self.click(self.map_tender['button_coupons_confirm'])

    def use_coupons_rate(self):
        self.click(self.map_tender['list_coupons'])

        self.typeIn(self.map_tender['list_coupons_grid'], Keys.TAB)
        self.typeIn(self.map_tender['list_coupons_grid'], Keys.END)

        element = self.find_the_element(self.map_tender['coupons_rate'])
        element[-1].click()
        self.click(self.map_tender['button_coupons_confirm'])

    def get_tender_ok(self):
        return self.find_the_element(self.map_tender['message_tender_ok']).text

    
