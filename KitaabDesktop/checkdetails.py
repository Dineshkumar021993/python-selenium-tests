import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import allure
import pytest
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://kitaabdev.finsights.biz/?#/kitaab-vertical-modules"
driver.get(url)
driver.maximize_window()
time.sleep(15)


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

    def test_username_button(self):
        EnterUserName = driver.find_element(By.XPATH, '//input[@id ="emailOrPhoneNum"]')
        highlight_element(EnterUserName, driver)
        EnterUserName.send_keys("devuser@lotusinsights.in")
        allure.attach(driver.get_screenshot_as_png(), name="EnterUserName",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClickNextButton = driver.find_element(By.XPATH, "//button[text()='Next']")
        highlight_element(ClickNextButton, driver)
        ClickNextButton.click()
        allure.attach(driver.get_screenshot_as_png(), name="ClickNextButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        EnterPassword = driver.find_element(By.XPATH, '//input[@id="password"]')
        highlight_element(EnterPassword, driver)
        EnterPassword.send_keys("Dev@123")
        allure.attach(driver.get_screenshot_as_png(), name="Clickpassword",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        CheckPasswordEye = driver.find_element(By.XPATH, "//i[@class = 'pi pi-eye-slash m-2 fs-5']")
        highlight_element(CheckPasswordEye, driver)
        CheckPasswordEye.click()
        allure.attach(driver.get_screenshot_as_png(), name="CheckPasswordEye",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClickSignButton = driver.find_element(By.XPATH, "//button[text()='Sign in']")
        highlight_element(ClickSignButton, driver)
        ClickSignButton.click()
        allure.attach(driver.get_screenshot_as_png(), name="clickSignInButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(10)

    def test_select_Organistion(self):
        OrganisationIdDropdown = driver.find_element(By.XPATH, '//div[@class="select-inp-header header-dp-select"]//div[@class="p-dropdown p-component p-inputwrapper p-inputwrapper-filled shadow-none"]')
        OrganisationIdDropdown.click()

        time.sleep(10)
