from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import pytest
import allure

from appium.webdriver.common.touch_action import TouchAction

# Desired capabilities
desired_caps = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'platformVersion': '12.0',
    'deviceName': 'ApiDemos',
    'app': 'D:\\Tools\\APKFiles-1\\resources\\ApiDemos-debug.apk',
    'appPackage': 'io.appium.android.apis',
    'appActivity': 'io.appium.android.apis.ApiDemos'
}

driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
driver.implicitly_wait(10)


@allure.severity(allure.severity_level.CRITICAL)
# Define test steps
def test_accessibility_section():
    allure.attach(driver.get_screenshot_as_png(), name="Accessibility_Screenshot",
                  attachment_type=allure.attachment_type.PNG)
    driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@content-desc="Accessibility"]').click()
    allure.attach(driver.get_screenshot_as_png(), name="Accessibility_Node_Screenshot",
                  attachment_type=allure.attachment_type.PNG)
    driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Accessibility Node Provider"]').click()
    for _ in range(2):
        driver.back()


def test_media_section():
    allure.attach(driver.get_screenshot_as_png(), name="Media_Screenshot", attachment_type=allure.attachment_type.PNG)
    driver.find_element(MobileBy.ACCESSIBILITY_ID, "Media").click()
    driver.back()


def test_preference_dependencies():
    allure.attach(driver.get_screenshot_as_png(), name="Preference_Dependencies_Screenshot",
                  attachment_type=allure.attachment_type.PNG)
    driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@index='9']").click()
    driver.find_element(MobileBy.ACCESSIBILITY_ID, "3. Preference dependencies").click()
    driver.find_element(MobileBy.XPATH, "//android.widget.RelativeLayout[@index='0']").click()
    element = driver.find_element(MobileBy.XPATH,
                                  "/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.RelativeLayout")
    element.click()
    element1 = driver.find_element(MobileBy.XPATH,
                                   "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText")
    element1.send_keys("nocode")
    driver.find_element(MobileBy.ID, "android:id/button1").click()
    for _ in range(3):
        driver.back()
        driver.implicitly_wait(10)


def test_hover_events():
    allure.attach(driver.get_screenshot_as_png(), name="Hover_Events_Screenshot",
                  attachment_type=allure.attachment_type.PNG)
    driver.implicitly_wait(10)
    driver.find_element(MobileBy.ACCESSIBILITY_ID, "Views").click()
    driver.implicitly_wait(5)
    driver.find_element(MobileBy.ACCESSIBILITY_ID, "Hover Events").click()
    driver.implicitly_wait(5)
    driver.find_element(MobileBy.ACCESSIBILITY_ID, "Hover Here").click()
    driver.implicitly_wait(5)
    driver.find_element(MobileBy.XPATH,
                        '//android.widget.CheckBox[@content-desc="Make container intercept hover events"]').click()
    driver.implicitly_wait(5)
    driver.back()
    driver.implicitly_wait(5)


def test_controls_section():
    allure.attach(driver.get_screenshot_as_png(), name="Controls_Screenshot",
                  attachment_type=allure.attachment_type.PNG)
    driver.find_element(MobileBy.ACCESSIBILITY_ID, "Controls").click()
    driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@content-desc="1. Light Theme"]').click()
    driver.find_element(MobileBy.ID, "io.appium.android.apis:id/check1").click()
    driver.find_element(MobileBy.XPATH, '//android.widget.CheckBox[@content-desc="Checkbox 1"]').click()
    driver.find_element(MobileBy.ACCESSIBILITY_ID, "Checkbox 2").click()
    driver.find_element(MobileBy.XPATH, '//android.widget.CheckBox[@content-desc="Checkbox 2"]').click()
    driver.find_element(MobileBy.XPATH, "//android.widget.RadioButton[@index='0']").click()
    driver.find_element(MobileBy.XPATH, '//android.widget.RadioButton[@content-desc="RadioButton 2"]').click()
    driver.find_element(MobileBy.ID, "io.appium.android.apis:id/toggle1").click()
    driver.find_element(MobileBy.ID, "io.appium.android.apis:id/toggle2").click()
    driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Mercury"]').click()
    driver.find_element(MobileBy.XPATH, '//android.widget.CheckedTextView[@text="Jupiter"]').click()
    element = driver.find_element(MobileBy.ID, 'io.appium.android.apis:id/button')
    touch_action = TouchAction(driver)
    touch_action.long_press(element).wait(5000).release().perform()
    allure.attach(driver.get_screenshot_as_png(), name="Controls_Long_Press_Screenshot",
                  attachment_type=allure.attachment_type.PNG)

