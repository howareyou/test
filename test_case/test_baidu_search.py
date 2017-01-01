# -*- coding: utf-8 -*-

from selenium import webdriver

from time import sleep
import unittest


class BaiduPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie(
            executable_path="C:\\Users\\Kun\\Downloads\\IEDriverServer_x64_2.53.1\\IEDriverServer.exe")
        self.driver.get("https://www.baidu.com")

    def tearDown(self):
        self.driver.close()

    def test_baidu_search(self):
        "Lanuch baidu home page and search keywords"
        self.driver.find_element_by_id("kw").send_keys('selenium')
        sleep(1)
        self.driver.find_element_by_id("su").click()
        sleep(1)
        self.driver.save_screenshot("D:\\SELENIUM.PNG")
