import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import allure
import pytest
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://kitaabdev.finsights.biz/#/login"
driver.get(url)
driver.maximize_window()
time.sleep(5)


def highlight_element(element, driver):
    """Highlights a web element by changing its border and background color."""
    for _ in range(2):
        # Highlight by changing border and background color
        driver.execute_script("arguments[0].style.border='3px solid red'; arguments[0].style.backgroundColor='yellow';",
                              element)
        time.sleep(1)
        # Remove the highlight by resetting styles
        driver.execute_script("arguments[0].style.border=''; arguments[0].style.backgroundColor='';", element)


@allure.severity(allure.severity_level.CRITICAL)
class TestLoginPage:
    def test_click_sign_up_button(self):
        Element = driver.find_element(By.XPATH, "/html/body/div/form/div/div/div/div/div/div[2]/div[1]/a/span")
        highlight_element(Element, driver)
        Element.click()
        time.sleep(5)

        # Capture and attach a screenshot
        allure.attach(driver.get_screenshot_as_png(), name="Sign-Up-Now Button",
                      attachment_type=allure.attachment_type.PNG)

        # assert Element.text == "Sign Up Now"

    def test_enter_username(self):
        Element = driver.find_element(By.NAME, "email")
        highlight_element(Element, driver)
        Element.send_keys("dineshkumar.pentakota@gmail.com")
        time.sleep(5)

        # Capture and attach a screenshot
        allure.attach(driver.get_screenshot_as_png(), name="Enter Username", attachment_type=allure.attachment_type.PNG)

    def test_enter_password(self):
        Element = driver.find_element(By.ID, "password")
        highlight_element(Element, driver)
        Element.send_keys("Dinesh@#4")
        time.sleep(5)

        # Capture and attach a screenshot
        allure.attach(driver.get_screenshot_as_png(), name="Enter Password", attachment_type=allure.attachment_type.PNG)

    def test_click_password_eye(self):
        Element = driver.find_element(By.XPATH,
                                      "/html/body/div/form/div/div[2]/div/div/div/div[3]/div/div[1]/span/div/button/i")
        highlight_element(Element, driver)
        Element.click()
        time.sleep(5)

        # Capture and attach a screenshot
        allure.attach(driver.get_screenshot_as_png(), name="Password Eye", attachment_type=allure.attachment_type.PNG)

    def test_enter_phone_number(self):
        Element = driver.find_element(By.NAME, "phoneNumber")
        highlight_element(Element, driver)
        Element.send_keys(7842773980)
        time.sleep(5)

        # Capture and attach a screenshot
        allure.attach(driver.get_screenshot_as_png(), name="Phone Number", attachment_type=allure.attachment_type.PNG)

    def test_click_agree_terms(self):
        Element = driver.find_element(By.XPATH,
                                      "/html/body/div/form/div/div[2]/div/div/div/div[5]/div/div/div[1]/label/div/div[2]")
        highlight_element(Element, driver)
        Element.click()
        time.sleep(5)

        # Capture and attach a screenshot
        allure.attach(driver.get_screenshot_as_png(), name="Terms and Policies",
                      attachment_type=allure.attachment_type.PNG)

    def test_click_proceed_button(self):
        Element = driver.find_element(By.XPATH, "/html/body/div/form/div/div[2]/div/div/div/div[6]/div/div")
        highlight_element(Element, driver)
        Element.click()
        time.sleep(5)

        # Capture and attach a screenshot
        allure.attach(driver.get_screenshot_as_png(), name="Proceed Button", attachment_type=allure.attachment_type.PNG)




