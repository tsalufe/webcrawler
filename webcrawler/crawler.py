import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class FirefoxCrawler(object):

    headless = True

    executable_path = '/usr/local/bin/geckodriver'

    implicitly_wait = 30

    def __init__(self, headless = True, executable_path = None, implicitly_wait = 30):

        self.headless = headless

        if executable_path is not None:
            self.executable_path = executable_path

        if implicitly_wait > 0:
            self.implicitly_wait = implicitly_wait

    def get_driver(self):

        options = Options()
        options.headless = self.headless
        return webdriver.Firefox(options = options, executable_path = self.executable_path)

    def load_page(self, url):
        
        driver = self.get_driver()
        driver.get(url)
        return driver
