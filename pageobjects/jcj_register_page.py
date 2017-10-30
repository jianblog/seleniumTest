# coding = utf-8

from framework.base_page import BasePage

import os, time
import json


class RegisterPage(BasePage):
    # 注册页面

    def __init__(self, driver):
        super(RegisterPage, self).__init__(driver)

        # load json elements
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "elements_top.json"),"r", encoding="utf-8") as f:
            self.map_top = json.load(f)
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "elements_register.json"), "r", encoding="utf-8") as f:
            self.map_register = json.load(f)

        self.to_register()      


    def to_register(self):
        self.gotoUrl("http://jingchujie.dev")
        self.click(self.map_register['link_register'])

    def logout(self):
        self.click(self.map_top['top_logout'])

    def input_reg_phone(self, phone):
        self.typeIn(self.map_register['input_reg_phone'], phone)
        time.sleep(1)

    def get_phone_warn(self):
        return self.find_the_element(self.map_register['input_reg_phone']).get_attribute('value')

    def input_reg_password(self, password):
        self.typeIn(self.map_register['input_reg_password'], password)
        time.sleep(1)

    def get_password_warn(self):
        return self.find_the_element(self.map_register['input_reg_password']).get_attribute('value')

    def click_get_sms(self):
        self.click(self.map_register['button_get_sms'])
        time.sleep(1)

    def input_verify_code(self,code):
        self.typeIn(self.map_register['input_reg_sms'], code)
        time.sleep(1)

    def get_verify_warn(self):
        return self.find_the_element(self.map_register['input_reg_sms']).get_attribute('value')

    def check_reg_protocol(self):
        self.click(self.map_register['check_reg_protocol'])
        
    def click_reg_confirm(self):
        self.click(self.map_register['button_reg_confirm'])

    def get_regok_msg(self):
        return self.find_the_element(self.map_register['text_reg_ok']).text
