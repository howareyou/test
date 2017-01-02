# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import os
import time
from time import sleep
import unittest
import traceback

class BaiduPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie(
            executable_path="C:\\Users\\Kun\\Downloads\\IEDriverServer_x64_2.53.1\\IEDriverServer.exe")
        #currently, use a fixed driver path. should be replaced by given paramters to decide which driver should be used
        self.driver.get("https://www.baidu.com")

    def tearDown(self):
        self.driver.close()

    def test_baidu_search(self):
        "Lanuch baidu home page and search keyword AKQA"
        try:
            self.driver.find_element_by_id("kw").send_keys('AKQA')
            sleep(1)
            self.driver.find_element_by_id("su").click()
            try:
                WebDriverWait(self.driver, 15, 1).until(EC.title_contains("AKQA"))
            except TimeoutException:
                print(traceback.print_exc())
                self.fail("Can't load control within 10s")
            time_tag = time.strftime("%Y%m%d%H%M%S", time.localtime())
            screenshot_file_name = os.getcwd() + "\\test_result\\" + time_tag + "SELENIUM.PNG"
            print(screenshot_file_name)
            self.driver.save_screenshot(screenshot_file_name)

        except TimeoutException:
            print(traceback.print_exc())
            self.fail("Can't load control within sepcial time")
        finally:
            pass
