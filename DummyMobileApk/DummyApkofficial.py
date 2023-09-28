from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import allure
import pytest

from appium.webdriver.common.touch_action import TouchAction

# Desired capabilities
desired_caps = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'platformVersion': '12.0',
    'deviceName': 'DummyApk',
    'app': 'D:\\Tools\\APKFiles-1\\resources\\ApiDemos-debug.apk',
    'appPackage': 'io.appium.android.apis',
    'appActivity': 'io.appium.android.apis.ApiDemos'
}

# Initialize the Appium driver
driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
driver.implicitly_wait(30)


# Function to highlight an element
def highlight_element(element):
    driver.execute_script(
        "arguments[0].style.border = '2px solid red'; arguments[0].style.backgroundColor = 'yellow';", element)


def test_accessibility_section():
    # Attach a screenshot to the report
    allure.attach(driver.get_screenshot_as_png(), name="Accessibility_Screenshot",
                  attachment_type=allure.attachment_type.PNG)

    # Click on the "Accessibility" element and highlight it
    element = driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@content-desc="Accessibility"]')
    highlight_element(element)
    element.click()

    # Attach another screenshot
    allure.attach(driver.get_screenshot_as_png(), name="Accessibility_Node_Screenshot",
                  attachment_type=allure.attachment_type.PNG)

    # Click on "Accessibility Node Provider"
    element = driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Accessibility Node Provider"]')
    highlight_element(element)
    element.click()

    # Navigate back twice
    for _ in range(2):
        driver.back()


def test_media_section():
    allure.attach(driver.get_screenshot_as_png(), name="Media_Screenshot",
                  attachment_type=allure.attachment_type.PNG)
    element = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Media")
    highlight_element(element)
    element.click()
    driver.back()


def test_preference_dependencies():
    allure.attach(driver.get_screenshot_as_png(), name="Preference_Dependencies_Screenshot",
                  attachment_type=allure.attachment_type.PNG)
    element = driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@index='9']")
    highlight_element(element)
    element.click()

    element = driver.find_element(MobileBy.ACCESSIBILITY_ID, "3. Preference dependencies")
    highlight_element(element)
    element.click()

    element = driver.find_element(MobileBy.XPATH, "//android.widget.RelativeLayout[@index='0']")
    highlight_element(element)
    element.click()

    element = driver.find_element(MobileBy.XPATH,
                                  "/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.RelativeLayout")
    highlight_element(element)
    element.click()

    element = driver.find_element(MobileBy.XPATH,
                                  "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText")
    highlight_element(element)
    element.send_keys("nocode")

    element = driver.find_element(MobileBy.ID, "android:id/button1")
    highlight_element(element)
    element.click()

    # Navigate back three times
    for _ in range(3):
        driver.back()


def test_hover_events():
    allure.attach(driver.get_screenshot_as_png(), name="Hover_Events_Screenshot",
                  attachment_type=allure.attachment_type.PNG)

    element = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Views")
    highlight_element(element)
    element.click()

    element = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Hover Events")
    highlight_element(element)
    element.click()

    element = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Hover Here")
    highlight_element(element)
    element.click()

    # Toggle "Make container intercept hover events"
    element = driver.find_element(MobileBy.XPATH,
                                  '//android.widget.CheckBox[@content-desc="Make container intercept hover events"]')
    highlight_element(element)
    element.click()

    # Navigate back
    driver.back()


def test_controls_section():
    allure.attach(driver.get_screenshot_as_png(), name="Controls_Screenshot",
                  attachment_type=allure.attachment_type.PNG)

    element = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Controls")
    highlight_element(element)
    element.click()

    # Click on various controls and elements
    element = driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@content-desc="1. Light Theme"]')
    highlight_element(element)
    element.click()

    element = driver.find_element(MobileBy.ID, "io.appium.android.apis:id/check1")
    highlight_element(element)
    element.click()

    element = driver.find_element(MobileBy.XPATH, '//android.widget.CheckBox[@content-desc="Checkbox 1"]')
    highlight_element(element)
    element.click()

    element = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Checkbox 2")
    highlight_element(element)
    element.click()

    element = driver.find_element(MobileBy.XPATH, '//android.widget.CheckBox[@content-desc="Checkbox 2"]')
    highlight_element(element)
    element.click()

    element = driver.find_element(MobileBy.XPATH, "//android.widget.RadioButton[@index='0']")
    highlight_element(element)
    element.click()

    element = driver.find_element(MobileBy.XPATH, '//android.widget.RadioButton[@content-desc="RadioButton 2"]')
    highlight_element(element)
    element.click()

    element = driver.find_element(MobileBy.ID, "io.appium.android.apis:id/toggle1")
    highlight_element(element)
    element.click()

    element = driver.find_element(MobileBy.ID, "io.appium.android.apis:id/toggle2")
    highlight_element(element)
    element.click()

    element = driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Mercury"]')
    highlight_element(element)
    element.click()

    element = driver.find_element(MobileBy.XPATH, '//android.widget.CheckedTextView[@text="Jupiter"]')
    highlight_element(element)
    element.click()

    # Perform a long press on an element
    element = driver.find_element(MobileBy.ID, 'io.appium.android.apis:id/button')
    highlight_element(element)
    touch_action = TouchAction(driver)
    touch_action.long_press(element).wait(5000).release().perform()

    # Attach a screenshot
    allure.attach(driver.get_screenshot_as_png(), name="Controls_Long_Press_Screenshot",
                  attachment_type=allure.attachment_type.PNG)
