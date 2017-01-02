'''
Testing execution enterance
'''

import unittest

import sys
import test_case

def show_usage():
    print("please assign a test sute, example: python run.py --test_sute test_suite_baidu")

# get parameters from run.py
def get_parameter():
    pass


if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromName("test_case.test_baidu_search.BaiduPage.test_baidu_search"))
    #result = unittest.TextTestRunner().run(test_suite)
    #Sprint(result)
    try:
        import HTMLTestRunner
        filePath = "d://pyResult.html"
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
