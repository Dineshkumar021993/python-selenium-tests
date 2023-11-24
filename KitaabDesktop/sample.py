import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://kitaabdev.finsights.biz/#/login")
driver.maximize_window()
time.sleep(2)


class TestLoginPage:
    def test_username_button(self):
        EnterUserName = driver.find_element(By.XPATH, '//input[@id ="emailOrPhoneNum"]')
        EnterUserName.send_keys("devuser@lotusinsights.in")
        time.sleep(5)

        ClickNextButton = driver.find_element(By.XPATH, "//button[text()='Next']")
        ClickNextButton.click()
        time.sleep(5)

        EnterPassword = driver.find_element(By.XPATH, '//input[@id="password"]')
        EnterPassword.send_keys("Dev@123")
        time.sleep(5)

        ClickSignButton = driver.find_element(By.XPATH, "//button[text()='Sign in']")
        ClickSignButton.click()
        time.sleep(5)

        GetCookies = driver.get_cookies()
        print("Size of cookies:", len(GetCookies))
