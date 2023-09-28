import time
from selenium import webdriver
from selenium.webdriver import Keys
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

    def test_ValidUsername_and_ValidPassword(self):
        EnterUserName = driver.find_element(By.ID, 'emailOrPhoneNum')
        highlight_element(EnterUserName, driver)
        EnterUserName.send_keys("devuser@lotusinsights.in")
        allure.attach(driver.get_screenshot_as_png(), name="EnterUserName",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClickNextButton = driver.find_element(By.XPATH, '//button[text()="Next"]')
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
        time.sleep(5)
        allure.attach(driver.get_screenshot_as_png(), name="FinalPage",
                      attachment_type=allure.attachment_type.PNG)

    def test_InvalidUsername_and_validPassword(self):
        EnterUserName = driver.find_element(By.XPATH, '//input[@id ="emailOrPhoneNum"]')
        highlight_element(EnterUserName, driver)
        EnterUserName.send_keys("devuser@lotusinsight.in")
        allure.attach(driver.get_screenshot_as_png(), name="EnterUserName",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClickNextButton = driver.find_element(By.XPATH, "//button[text()='Next']")
        highlight_element(ClickNextButton, driver)
        ClickNextButton.click()
        allure.attach(driver.get_screenshot_as_png(), name="ClickNextButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(10)
        allure.attach(driver.get_screenshot_as_png(), name="FinalPage",
                      attachment_type=allure.attachment_type.PNG)

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

    def test_validUsername_and_InvalidPassword(self):
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
        EnterPassword.send_keys("dev@123")
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
        allure.attach(driver.get_screenshot_as_png(), name="FinalPage",
                      attachment_type=allure.attachment_type.PNG)

    def test_InvalidUsername_and_InvalidPassword(self):
        EnterUserName = driver.find_element(By.XPATH, '//input[@id ="emailOrPhoneNum"]')
        highlight_element(EnterUserName, driver)
        EnterUserName.send_keys("devuser@lotusinsight.in")
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
        EnterPassword.send_keys("dev@123")
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

    def test_changeUserNameWithValidUserName(self):
        EnterUserName = driver.find_element(By.ID, 'emailOrPhoneNum')
        highlight_element(EnterUserName, driver)
        EnterUserName.send_keys("devuser@lotusinsights.in")
        allure.attach(driver.get_screenshot_as_png(), name="EnterUserName",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClickNextButton = driver.find_element(By.XPATH, '//button[text()="Next"]')
        highlight_element(ClickNextButton, driver)
        ClickNextButton.click()
        allure.attach(driver.get_screenshot_as_png(), name="ClickNextButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClickOnChangeButton = driver.find_element(By.XPATH, '//button[text()="Change"]')
        highlight_element(ClickOnChangeButton, driver)
        ClickOnChangeButton.click()
        allure.attach(driver.get_screenshot_as_png(), name="ClickOnChangeButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClearPreviousText = driver.find_element(By.ID, 'emailOrPhoneNum')
        highlight_element(ClearPreviousText, driver)
        ClearPreviousText.send_keys(Keys.CONTROL + 'a')
        ClearPreviousText.send_keys(Keys.DELETE)
        allure.attach(driver.get_screenshot_as_png(), name="clearPreviousText",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        EnterUserName = driver.find_element(By.XPATH, '//input[@id ="emailOrPhoneNum"]')
        highlight_element(EnterUserName, driver)

        EnterUserName.send_keys("gnanapandithan@lotusinsights.in")
        allure.attach(driver.get_screenshot_as_png(), name="EnterUserName",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClickNextButton = driver.find_element(By.XPATH, "//button[text()='Next']")
        highlight_element(ClickNextButton, driver)
        ClickNextButton.click()
        allure.attach(driver.get_screenshot_as_png(), name="ClickNextButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

    def test_changeUserNameWithInValidUserName(self):
        EnterUserName = driver.find_element(By.ID, 'emailOrPhoneNum')
        highlight_element(EnterUserName, driver)
        EnterUserName.send_keys("devuser@lotusinsights.in")
        allure.attach(driver.get_screenshot_as_png(), name="EnterUserName",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClickNextButton = driver.find_element(By.XPATH, '//button[text()="Next"]')
        highlight_element(ClickNextButton, driver)
        ClickNextButton.click()
        allure.attach(driver.get_screenshot_as_png(), name="ClickNextButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClickOnChangeButton = driver.find_element(By.XPATH, '//button[text()="Change"]')
        highlight_element(ClickOnChangeButton, driver)
        ClickOnChangeButton.click()
        allure.attach(driver.get_screenshot_as_png(), name="ClickOnChangeButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClearPreviousText = driver.find_element(By.ID, 'emailOrPhoneNum')
        highlight_element(ClearPreviousText, driver)
        ClearPreviousText.send_keys(Keys.CONTROL + 'a')
        ClearPreviousText.send_keys(Keys.DELETE)
        allure.attach(driver.get_screenshot_as_png(), name="clearPreviousText",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        EnterUserName = driver.find_element(By.XPATH, '//input[@id ="emailOrPhoneNum"]')
        highlight_element(EnterUserName, driver)

        EnterUserName.send_keys("gnanapandithan@lotusinsight.in")
        allure.attach(driver.get_screenshot_as_png(), name="EnterUserName",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClickNextButton = driver.find_element(By.XPATH, "//button[text()='Next']")
        highlight_element(ClickNextButton, driver)
        ClickNextButton.click()
        allure.attach(driver.get_screenshot_as_png(), name="ClickNextButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

    def test_login_with_sendotp(self):
        EnterUserName = driver.find_element(By.ID, 'emailOrPhoneNum')
        highlight_element(EnterUserName, driver)
        EnterUserName.send_keys("devuser@lotusinsights.in")
        allure.attach(driver.get_screenshot_as_png(), name="EnterUserName",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClickNextButton = driver.find_element(By.XPATH, '//button[text()="Next"]')
        highlight_element(ClickNextButton, driver)
        ClickNextButton.click()
        allure.attach(driver.get_screenshot_as_png(), name="ClickNextButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        SignInUsingOTP = driver.find_element(By.XPATH, '//button[text()="Sign in using OTP"]')
        highlight_element(SignInUsingOTP, driver)
        ClickNextButton.click()
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), name="Sign in using OTP",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

    def test_RightUserName_forgot_passwordWith_RightOTP(self):
        EnterUserName = driver.find_element(By.XPATH, '//input[@id ="emailOrPhoneNum"]')
        highlight_element(EnterUserName, driver)
        EnterUserName.send_keys("devuser@lotusinsights.in")
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

        checkChangeButton = driver.find_element(By.XPATH, '//button[text()= "Change"]')
        highlight_element(checkChangeButton, driver)
        allure.attach(driver.get_screenshot_as_png(), name="checkChangeButton",
                      attachment_type=allure.attachment_type.PNG)
        checkChangeButton.click()
        time.sleep(5)

        ClearPreviousText = driver.find_element(By.ID, 'emailOrPhoneNum')
        highlight_element(ClearPreviousText, driver)
        ClearPreviousText.send_keys(Keys.CONTROL + 'a')
        ClearPreviousText.send_keys(Keys.DELETE)
        allure.attach(driver.get_screenshot_as_png(), name="clearPreviousText",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        EnterUserNameAfterChangeButton = driver.find_element(By.XPATH, '//input[@id ="emailOrPhoneNum"]')
        highlight_element(EnterUserNameAfterChangeButton, driver)
        EnterUserNameAfterChangeButton.send_keys("devuser@lotusinsights.in")
        allure.attach(driver.get_screenshot_as_png(), name="EnterUserNameAfterChangeButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClickNextButtonAfterChangeButton = driver.find_element(By.XPATH, '//button[text()="Next"]')
        highlight_element(ClickNextButtonAfterChangeButton, driver)
        ClickNextButtonAfterChangeButton.click()
        allure.attach(driver.get_screenshot_as_png(), name="ClickNextButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClickSendOtpButton = driver.find_element(By.XPATH, '//button[text()="Send OTP"]')
        highlight_element(ClickSendOtpButton, driver)
        ClickSendOtpButton.click()
        allure.attach(driver.get_screenshot_as_png(), name="SendOtpButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        EnterWrongOTP = driver.find_element(By.ID, "otp")
        highlight_element(EnterWrongOTP, driver)
        EnterWrongOTP.send_keys("12345")
        allure.attach(driver.get_screenshot_as_png(), name="verifyWrongOtp",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        VerifyButtonAfterEnterOtp = driver.find_element(By.XPATH, '//button[text()="Verify OTP"]')
        highlight_element(VerifyButtonAfterEnterOtp, driver)
        VerifyButtonAfterEnterOtp.click()
        allure.attach(driver.get_screenshot_as_png(), name="VerifyButtonAfterEnterOtp",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), name="FinalPage",
                      attachment_type=allure.attachment_type.PNG)

        time.sleep(5)

        ContactSupport = driver.find_element(By.XPATH, "//a[text()='Contact Support']")
        highlight_element(ContactSupport, driver)
        ContactSupport.click()
        allure.attach(driver.get_screenshot_as_png(), name="contactSupport",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

    def test_RightUserName_forgot_passwordWith_WrongOTP(self):
        EnterUserName = driver.find_element(By.XPATH, '//input[@id ="emailOrPhoneNum"]')
        highlight_element(EnterUserName, driver)
        EnterUserName.send_keys("devuser@lotusinsights.in")
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

        checkChangeButton = driver.find_element(By.XPATH, '//button[text()= "Change"]')
        highlight_element(checkChangeButton, driver)
        allure.attach(driver.get_screenshot_as_png(), name="checkChangeButton",
                      attachment_type=allure.attachment_type.PNG)
        checkChangeButton.click()
        time.sleep(5)

        ClearPreviousText = driver.find_element(By.ID, 'emailOrPhoneNum')
        highlight_element(ClearPreviousText, driver)
        ClearPreviousText.send_keys(Keys.CONTROL + 'a')
        ClearPreviousText.send_keys(Keys.DELETE)
        allure.attach(driver.get_screenshot_as_png(), name="clearPreviousText",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        EnterUserNameAfterChangeButton = driver.find_element(By.XPATH, '//input[@id ="emailOrPhoneNum"]')
        highlight_element(EnterUserNameAfterChangeButton, driver)
        EnterUserNameAfterChangeButton.send_keys("devuser@lotusinsights.in")
        allure.attach(driver.get_screenshot_as_png(), name="EnterUserNameAfterChangeButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClickNextButtonAfterChangeButton = driver.find_element(By.XPATH, '//button[text()="Next"]')
        highlight_element(ClickNextButtonAfterChangeButton, driver)
        ClickNextButtonAfterChangeButton.click()
        allure.attach(driver.get_screenshot_as_png(), name="ClickNextButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClickSendOtpButton = driver.find_element(By.XPATH, '//button[text()="Send OTP"]')
        highlight_element(ClickSendOtpButton, driver)
        ClickSendOtpButton.click()
        allure.attach(driver.get_screenshot_as_png(), name="SendOtpButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        EnterWrongOTP = driver.find_element(By.ID, "otp")
        highlight_element(EnterWrongOTP, driver)
        EnterWrongOTP.send_keys("PlaceRightOTP")
        allure.attach(driver.get_screenshot_as_png(), name="verifyWrongOtp",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        VerifyButtonAfterEnterOtp = driver.find_element(By.XPATH, '//button[text()="Verify OTP"]')
        highlight_element(VerifyButtonAfterEnterOtp, driver)
        VerifyButtonAfterEnterOtp.click()
        allure.attach(driver.get_screenshot_as_png(), name="VerifyButtonAfterEnterOtp",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), name="FinalPage",
                      attachment_type=allure.attachment_type.PNG)

        time.sleep(5)

        ContactSupport = driver.find_element(By.XPATH, "//a[text()='Contact Support']")
        highlight_element(ContactSupport, driver)
        ContactSupport.click()
        allure.attach(driver.get_screenshot_as_png(), name="contactSupport",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

    def test_WrongUserName_checkOTP_For_CorrectOtp(self):
        EnterUserName = driver.find_element(By.XPATH, '//input[@id ="emailOrPhoneNum"]')
        highlight_element(EnterUserName, driver)
        EnterUserName.send_keys("devuser@lotusinsights.in")
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

        checkChangeButton = driver.find_element(By.XPATH, '//button[text()= "Change"]')
        highlight_element(checkChangeButton, driver)
        allure.attach(driver.get_screenshot_as_png(), name="checkChangeButton",
                      attachment_type=allure.attachment_type.PNG)
        checkChangeButton.click()
        time.sleep(5)

        ClearPreviousText = driver.find_element(By.ID, 'emailOrPhoneNum')
        highlight_element(ClearPreviousText, driver)
        ClearPreviousText.send_keys(Keys.CONTROL + 'a')
        ClearPreviousText.send_keys(Keys.DELETE)
        allure.attach(driver.get_screenshot_as_png(), name="clearPreviousText",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        EnterUserNameAfterChangeButton = driver.find_element(By.XPATH, '//input[@id ="emailOrPhoneNum"]')
        highlight_element(EnterUserNameAfterChangeButton, driver)
        EnterUserNameAfterChangeButton.send_keys("devuser@lotusinsight.in")
        allure.attach(driver.get_screenshot_as_png(), name="EnterUserNameAfterChangeButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClickNextButtonAfterChangeButton = driver.find_element(By.XPATH, '//button[text()="Next"]')
        highlight_element(ClickNextButtonAfterChangeButton, driver)
        ClickNextButtonAfterChangeButton.click()
        allure.attach(driver.get_screenshot_as_png(), name="ClickNextButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClickSendOtpButton = driver.find_element(By.XPATH, '//button[text()="Send OTP"]')
        highlight_element(ClickSendOtpButton, driver)
        ClickSendOtpButton.click()
        allure.attach(driver.get_screenshot_as_png(), name="SendOtpButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        EnterWrongOTP = driver.find_element(By.ID, "otp")
        highlight_element(EnterWrongOTP, driver)
        EnterWrongOTP.send_keys("12345")
        allure.attach(driver.get_screenshot_as_png(), name="verifyWrongOtp",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        VerifyButtonAfterEnterOtp = driver.find_element(By.XPATH, '//button[text()="Verify OTP"]')
        highlight_element(VerifyButtonAfterEnterOtp, driver)
        VerifyButtonAfterEnterOtp.click()
        allure.attach(driver.get_screenshot_as_png(), name="VerifyButtonAfterEnterOtp",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), name="FinalPage",
                      attachment_type=allure.attachment_type.PNG)

        time.sleep(5)

        ClickSignInBack = driver.find_element(By.XPATH, "//a[text()='Back to Sign In']")
        highlight_element(ClickSignInBack, driver)
        ClickSignInBack.click()
        time.sleep(5)

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

    def test_username_with_changedPassword(self):
        EnterUserName = driver.find_element(By.ID, 'emailOrPhoneNum')
        highlight_element(EnterUserName, driver)
        EnterUserName.send_keys("devuser@lotusinsights.in")
        allure.attach(driver.get_screenshot_as_png(), name="EnterUserName",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClickNextButton = driver.find_element(By.XPATH, '//button[text()="Next"]')
        highlight_element(ClickNextButton, driver)
        ClickNextButton.click()
        allure.attach(driver.get_screenshot_as_png(), name="ClickNextButton",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        EnterPassword = driver.find_element(By.XPATH, '//input[@id="password"]')
        highlight_element(EnterPassword, driver)
        EnterPassword.send_keys("ChangedPassword")
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
        time.sleep(5)
        allure.attach(driver.get_screenshot_as_png(), name="FinalPage",
                      attachment_type=allure.attachment_type.PNG)








