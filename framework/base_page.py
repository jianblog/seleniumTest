# coding=utf-8
import time
from selenium.common.exceptions import NoSuchElementException
import os.path
from framework.logger import Logger
from selenium import webdriver


# create a logger instance  
logger =Logger(logger="BasePage").getlog()

class BasePage(object):
    """ 
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类 
    """
    def __init__(self,driver):
        self.driver = driver
    
    def gotoUrl(self, url):
        self.driver.get(url)

    # quit browser and end testing  
    def quit_browser(self):
        self.driver.quit()
    
    # 浏览器前进操作  
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")  
    
    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.") 
    
    # 隐式等待  
    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds) 
    
    # 点击关闭当前窗口  
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

    def getAlertMsg(self):
        try:
            message = self.driver.switch_to_alert().text
            self.driver.switch_to_alert().accept()
            return message
        except Exception as e:
            logger.error("No Alert windows pops")
    def wait(self, second):
        self.driver.implicitly_wait(second)
    
    # 保存图片
    def get_window_img(self):
        """ 
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下 
        """  
        file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'screenshots')  
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = os.path.join(file_path, rq + '.png') 
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except Exception as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_window_img()
   
    def find_the_element(self, selector):
        if selector['type'] == 'text':
            return self.driver.find_element_by_link_text(selector['value'])
        if selector['type'] == 'xpath':
            return self.driver.find_element_by_xpath(selector['value'])
        if selector['type'] == 'name':
            return self.driver.find_element_by_name(selector['value'])

    
    # 输入
    def typeIn(self,selector,text):
        
        el = self.find_the_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()
    
    # 清除文本框  
    def clear(self,selector):
        
        el = self.find_the_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e: 
            logger.error("Failed to clear in input box with %s" % e) 
            self.get_windows_img()
    
    # 点击元素 
    def click(self,selector):
        
        el = self.find_the_element(selector)
        try:
            el.click()
            #logger.info("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e) 
    
    # 或取网页标题
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title
    
    @staticmethod 
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)    
