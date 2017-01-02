'''
Testing execution enterance
'''

import unittest

import sys
import time
import os
import test_case

def show_usage():
    print("please assign a test sute, example: python run.py --test_sute test_suite_baidu --browser_config ieconfig.json --result_type html")

# get parameters from run.py
def get_parameter():
    global test_suite_name, browser_config_file_name,result_type

    pass


if __name__ == '__main__':
    get_parameter()
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromName("test_case.test_baidu_search.BaiduPage.test_baidu_search"))
    try:
        import HTMLTestRunner
        time_tag = time.strftime("%Y%m%d%H%M%S", time.localtime())
        filePath = os.getcwd() + "\\test_result\\" + time_tag + "TestResult.html"
        fp = open(filePath, 'w')
        html_runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report',
                                                    description='This  is Python  Report')
        result = html_runner.run(test_suite)
        fp.close()
        print(result)
    except ImportError:
        print("Not found HTMLTestRunner, will use text test runner")
        result=unittest.TextTestRunner().run(test_suite)
        print(result)
