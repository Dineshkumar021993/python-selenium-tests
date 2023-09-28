from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import allure

desired_caps = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'platformVersion': '12.0',
    'deviceName': 'kitaabDesktopandMobile',
    'app': 'D:\\Tools\\APKFiles-1\\resources\\app.apk',
    'appPackage': 'in.lotusinsights.kitaab',
    'appActivity': 'in.lotusinsights.kitaab.MainActivity'
}

driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
driver.implicitly_wait(10)


@allure.severity(allure.severity_level.CRITICAL)
class TestLoginPage:

    def test_click_skip_Button(self):
        Element = driver.find_element(MobileBy.XPATH, '//android.widget.Button[@content-desc="Skip"]')
        Element.click()
        time.sleep(5)

    def test_click_GetStarted(self):
        Element = driver.find_element(MobileBy.XPATH, '//android.widget.Button[@content-desc="Get Started"]')
        Element.click()
        time.sleep(5)

    def test_click_userName(self):
        Element = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, "UiSelector().index(3)")
        Element.click()
        Element.send_keys("dineshkumar.pentakota@gmail.com")
        time.sleep(5)

    def test_click_password(self):
        Element = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, "UiSelector().index(5)")
        Element.click()
        Element.send_keys("Dinesh@#4567")
        time.sleep(5)

    def test_click_phoneno(self):
        Element = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, "UiSelector().index(7)")
        Element.click()
        Element.send_keys("7842773980")
        time.sleep(5)

    def test_checkbox(self):
        Element = driver.find_element(MobileBy.XPATH, "//android.widget.CheckBox[@index='8']")
        Element.click()
        time.sleep(5)

    def test_proceed(self):
        Element = driver.find_element(MobileBy.XPATH, '//android.widget.Button[@content-desc="Proceed"]')
        Element.click()
        time.sleep(5)


driver.quit()
