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

    def test_forgot_password(self):
        EnterUserName = driver.find_element(By.XPATH, '//input[@id ="emailOrPhoneNum"]')
        highlight_element(EnterUserName, driver)
        EnterUserName.send_keys("devuser@lotusinsight.in")
        allure.attach(driver.get_screenshot_as_png(), name="EnterUserName",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ForgotPassword = driver.find_element(By.XPATH, "//a[text()='Forgot Password?']")
        highlight_element(ForgotPassword, driver)
        ForgotPassword.click()
        allure.attach(driver.get_screenshot_as_png(), name="ClickForgotPasswordButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        RedirectedForgotPasswordPage = driver.find_element(By.NAME, "emailOrPhoneNum")
        highlight_element(RedirectedForgotPasswordPage, driver)
        RedirectedForgotPasswordPage.send_keys("devuser@lotusinsights.in")
        allure.attach(driver.get_screenshot_as_png(), name="EnterUserNameInRedirectedPage",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        clickNextButton = driver.find_element(By.ID, "forgotpasswordNextBtn")
        highlight_element(clickNextButton, driver)
        allure.attach(driver.get_screenshot_as_png(), name="clickNextButton",
                      attachment_type=allure.attachment_type.PNG)
        clickNextButton.click()
        time.sleep(5)

        ContactSupport = driver.find_element(By.XPATH, "//a[text()='Contact Support']")
        highlight_element(ContactSupport, driver)
        ContactSupport.click()
        allure.attach(driver.get_screenshot_as_png(), name="contactSupport",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        # ClickSignInBack = driver.find_element(By.XPATH, "//a[text()='Back to Sign In']")
        # highlight_element(ClickSignInBack, driver)
        # ClickSignInBack.click()
        # time.sleep(10)

    def test_with_wrongUsername_and_password(self):
        EnterUserName = driver.find_element(By.XPATH, '//input[@id ="emailOrPhoneNum"]')
        highlight_element(EnterUserName, driver)
        EnterUserName.send_keys("devuser@lotusinsights.in")
        allure.attach(driver.get_screenshot_as_png(), name="Enterusername",
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
        EnterPassword.send_keys("dev@123")
        allure.attach(driver.get_screenshot_as_png(), name="EnterPassword",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClickSignButton = driver.find_element(By.XPATH, "//button[text()='Sign in']")
        highlight_element(ClickSignButton, driver)
        ClickSignButton.click()
        allure.attach(driver.get_screenshot_as_png(), name="ClickSignInButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(10)

    def test_checkMFA(self):
        checkLearnMore_In_MFA = driver.find_element(By.XPATH, "//button[text()='Learn More']")
        highlight_element(checkLearnMore_In_MFA, driver)
        checkLearnMore_In_MFA.click()
        time.sleep(5)
        allure.attach(driver.get_screenshot_as_png(), name="Click MFA Button",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        checkingFirstThreeButtons = driver.find_element(By.XPATH, '//button[@data-testid="carousel-btn"]')
        highlight_element(checkingFirstThreeButtons, driver)
        checkingFirstThreeButtons.click()
        allure.attach(driver.get_screenshot_as_png(), name="First Button",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        checkingSecondThreeButtons = driver.find_element(By.XPATH, '//button[@data-testid="carousel-btn1"]')
        highlight_element(checkingSecondThreeButtons, driver)
        checkingFirstThreeButtons.click()
        allure.attach(driver.get_screenshot_as_png(), name="Second Button",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        checkingThirdThreeButtons = driver.find_element(By.XPATH, '//button[@data-testid="carousel-btn2"]')
        highlight_element(checkingThirdThreeButtons, driver)
        checkingFirstThreeButtons.click()
        allure.attach(driver.get_screenshot_as_png(), name="Third Button",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)
