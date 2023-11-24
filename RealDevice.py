import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

desired_caps = {'platformName': 'Android',
                'automationName': 'UIAutomator2',
                'deviceName': '13'}

driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
