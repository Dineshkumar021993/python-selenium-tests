import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UIAutomator2'
desired_caps['deviceName'] = 'Vysor Device'
desired_caps['deviceName'] = '13'


driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)