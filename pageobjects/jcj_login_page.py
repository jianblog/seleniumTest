# coding=utf-8
import sys
sys.path.append("..")
import os
import json

from framework.base_page import BasePage


class LoginPage(BasePage):
    # 登录页面入口
    login_link = "link_text=>立即登录" #"xpath=>html/body/div[2]/div[5]/div[1]/div/div[2]/a[2]"
    
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        # loading json
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "elements_top.json"),"r", encoding="utf-8") as f:
            self.map_top = json.load(f)
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "elements_login.json"),"r", encoding="utf-8") as f:
            self.map_login = json.load(f)

        # initial goto login page
        self.to_login()
 
 
    def to_login(self):
        element = self.find_the_element(self.map_top['top_login'])
        element.click()
        self.sleep(1)

    def logout(self):
        element = self.find_the_element(self.map_top['top_logout'])
        element.click()
        self.sleep(2)

    def input_account(self, value):
        element = self.find_the_element(self.map_login['input_account'])
        element.clear()
        element.send_keys(value)

    def input_password(self, password):
        element = self.find_the_element(self.map_login['input_password'])
        element.send_keys(password)

    def click_login(self):
        element = self.find_the_element(self.map_login['button_login'])
        element.click()
        self.sleep(1)

    def success_login_message(self):
        element = self.find_the_element(self.map_top['banner_message_login'])
        return element

    def fail_login_message(self):
        element = self.find_the_element(self.map_login['message_login'])
        return element
