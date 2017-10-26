# coding =utf-8
import configparser
import os.path
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger = "BrowserEngine").getlog()

class BrowserEngine(object):
    
    dir = os.path.abspath('/data/projects/notebook/autoTest/jingchujie')
    chrome_driver_path = dir + '/tools/chromedriver.exe' 
    ie_driver_path = dir +  '/tools/IEDriverServer.exe'  
    
    def __init__(self,driver):
        self.driver = driver
    
    def open_browser(self,url):
        config = configparser.ConfigParser()
        file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'config.ini')
        #logger.info("config file:" + file_path)
        config.read(file_path)
        
        browser = config.get("browserType","browserName")
        #logger.info("You had select %s browser." % browser)  
        url = config.get("testServer","URL")
        #logger.info("The test server url is: %s" % url)
        
        if browser =="Firefox":
            #display = Display(visible=0, size=(1440,900))
            #display.start()
            #self.xvfb = Xvfb(width=1440, height=900)
            #self.xvfb.start()
			
            driver = webdriver.Firefox()
			
			#driver = webdriver.Remote(
            #    command_executor='http://beta.dev:4444/wd/hub',
            #    desired_capabilities=
            #           {'browserName': 'firefox',
            #            'platform':'linux',
            #            'javascriptEnabled': True})
			
            logger.info("Starting firefox browser.")
        elif browser =="Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            #logger.info("Starting Chrome browser.")
        elif browser == "Ie":
            driver = webdriver.Ie(self.ie_driver_path)
            #logger.info("Starting IE browser.")
        
        driver.get(url)
        #driver.maximize_window()
        #logger.info("Open url: %s" % url)
        #logger.info("Maximize the current window.")  
        driver.implicitly_wait(10)  
        #logger.info("Set implicitly wait 10 seconds.")  
        
        return driver
    
    def quit_browser(self):
        #logger.info("Now, Close and quit the browser.") 
        self.driver.quit()
       # self.xvfb.stop()
        
