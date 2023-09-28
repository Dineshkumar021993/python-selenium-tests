import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

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
class TestMainPage:
    @pytest.mark.order1
    def test_EnterUsername_and_password_and_mainPage(self):
        EnterUserName = driver.find_element(By.ID, 'emailOrPhoneNum')
        EnterUserName.send_keys("devuser@lotusinsights.in")
        time.sleep(5)

        ClickNextButton = driver.find_element(By.XPATH, '//button[text()="Next"]')
        ClickNextButton.click()
        time.sleep(5)

        EnterPassword = driver.find_element(By.XPATH, '//input[@id="password"]')
        EnterPassword.send_keys("Dev@123")
        time.sleep(5)

        ClickSignButton = driver.find_element(By.XPATH, "//button[text()='Sign in']")
        ClickSignButton.click()
        time.sleep(10)

        allure.attach(driver.get_screenshot_as_png(), name="BeforeClickKitaabImage",
                      attachment_type=allure.attachment_type.PNG)

    @pytest.mark.order2
    def test_CheckKitaabImage(self):
        CheckKitaabImage = driver.find_element(By.XPATH,
                                               '//img[@class="c-sidebar-brand-full mobile-logo-width img-fluid inside-logo-full"]')
        highlight_element(CheckKitaabImage, driver)
        CheckKitaabImage.click()
        time.sleep(5)
        allure.attach(driver.get_screenshot_as_png(), name="clickKitaabImage",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClickOnDashBoard = driver.find_element(By.XPATH, '//p[text()="Dashboard"]')
        highlight_element(ClickOnDashBoard, driver)
        ClickOnDashBoard.click()
        allure.attach(driver.get_screenshot_as_png(), name="ClickOnDashBoard",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        ClickOnAddReportInDashBoard = driver.find_element(By.XPATH, '//button[@class="btn btn-primary p-l-r-20"]')
        highlight_element(ClickOnAddReportInDashBoard, driver)
        ClickOnAddReportInDashBoard.click()

        allure.attach(driver.get_screenshot_as_png(), name="ClickOnAddReportInDashBoard",
                      attachment_type=allure.attachment_type.PNG)

    @pytest.mark.order3
    def test_CheckDropDownInMainPage(self):
        CheckDropDownInMainPage = driver.find_element(By.XPATH, '//div[@class="p-dropdown-trigger"]')
        highlight_element(CheckDropDownInMainPage, driver)
        CheckDropDownInMainPage.click()
        allure.attach(driver.get_screenshot_as_png(), name="CheckDropDownInMainPage",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        CheckItemSelectionInDropDownAndCheckToastImage = driver.find_element(By.XPATH,
                                                                             '//div[text()="new org pref 1"]//parent::div//parent::li//following-sibling::li[1]//child::div//'
                                                                             'child::div[text()="MAHAVIR BEAUTY CENTER7b9c1f55-9d4d-4adf-b7ee-35e37f080858"]')
        highlight_element(CheckItemSelectionInDropDownAndCheckToastImage, driver)
        actions = ActionChains(driver)
        actions.move_to_element(CheckItemSelectionInDropDownAndCheckToastImage)
        actions.perform()
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), name="checkToastMessageScreenshot",
                      attachment_type=allure.attachment_type.PNG)
        highlight_element(CheckItemSelectionInDropDownAndCheckToastImage, driver)
        CheckItemSelectionInDropDownAndCheckToastImage.click()

        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), name="CheckItemSelectionInDropDownandCheckToastImage",
                      attachment_type=allure.attachment_type.PNG)
        driver.refresh()
        time.sleep(5)

        CheckDropDownInMainPage = driver.find_element(By.XPATH, '//div[@class="p-dropdown-trigger"]')
        CheckDropDownInMainPage.click()
        SelectingDifferentItemsInDropDown = driver.find_element(By.XPATH,
                                                                '//div[text()="new organization 23"]//parent::div//parent::li//following-sibling::li[1]//child::div//child::div[text()="Lotus Wireless Technologies India Pvt. Ltd -22-234eddc16a-7026-4ee1-986c-97bd04da935e"]')
        highlight_element(SelectingDifferentItemsInDropDown, driver)
        SelectingDifferentItemsInDropDown.click()
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), name="clickLotuswirelessInDropDown",
                      attachment_type=allure.attachment_type.PNG)
        driver.refresh()
        time.sleep(10)

        TestingScrollDownInDropDown = driver.find_element(By.XPATH, '//div[@class="p-dropdown-trigger"]')
        TestingScrollDownInDropDown.click()

        Element = driver.find_element(By.XPATH, '//div[text()="legal name"]')
        driver.execute_script("arguments[0].scrollIntoView();", Element)
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), name="TestingScrollDownInDropDown",
                      attachment_type=allure.attachment_type.PNG)
        driver.refresh()
        time.sleep(5)

        TestingScrollUpInDropDown = driver.find_element(By.XPATH, '//div[@class="p-dropdown-trigger"]')
        TestingScrollUpInDropDown.click()
        Element = driver.find_element(By.XPATH, '//div[text()="Lotus Wireless Technologies India Pvt. Ltd -22-23"]')
        driver.execute_script("arguments[0].scrollIntoView();", Element)
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), name="TestingScrollUpInDropDown",
                      attachment_type=allure.attachment_type.PNG)
        driver.refresh()
        time.sleep(5)

        CheckSearchBoxInDropDown = driver.find_element(By.XPATH, '//div[@class="p-dropdown-trigger"]')
        highlight_element(CheckSearchBoxInDropDown, driver)
        CheckSearchBoxInDropDown.click()
        CheckSearchBoxInDropDown = driver.find_element(By.XPATH,
                                                       '//input[@placeholder="Search" and @class="p-inputtext p-component form-control h-40px shadow-none"]')
        CheckSearchBoxInDropDown.send_keys("SREE BALAJII STORES")
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), name="CheckSearchBoxInDropDown",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        checkNewButtonInDropDown = driver.find_element(By.XPATH,
                                                       '//button[@class="btn btn-outline-primary mt-0 font-size-12 btn-block b-r-3"]')
        highlight_element(checkNewButtonInDropDown, driver)
        checkNewButtonInDropDown.click()
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), name="checkNewButtonInDropDown",
                      attachment_type=allure.attachment_type.PNG)
        driver.refresh()
        time.sleep(5)

        CheckingAllButtonsInNewOrgButtonInDropDown = driver.find_element(By.ID,"PR_1")
        highlight_element(CheckingAllButtonsInNewOrgButtonInDropDown, driver)
        CheckingAllButtonsInNewOrgButtonInDropDown.send_keys("Dinesh Pvt Ltd ....")
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), name="checkNewButtonInDropDown",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        CheckingAllButtonsInNewOrgButtonInDropDownDisplayName = driver.find_element(By.ID,"PR_2")
        highlight_element(CheckingAllButtonsInNewOrgButtonInDropDownDisplayName, driver)
        CheckingAllButtonsInNewOrgButtonInDropDownDisplayName.send_keys("Dinesh Pvt Ltd ....")
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), name="CheckingAllButtonsInNewOrgButtonInDropDownDisplayName",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        CheckingAllButtonsInNewOrgButtonInDropDowninDropDown = driver.find_element(By.ID,'PR_3')
        highlight_element(CheckingAllButtonsInNewOrgButtonInDropDowninDropDown, driver)
        CheckingAllButtonsInNewOrgButtonInDropDowninDropDown.click()
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), name="CheckingAllButtonsInNewOrgButtonInDropDowninDropDown",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        # CheckingElementInDropDownInDropDown = driver.find_element(By.XPATH,'//input[@value="Hungary" and @class="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused css-b52kj1"]')
        # highlight_element(CheckingElementInDropDownInDropDown, driver)
        # CheckingElementInDropDownInDropDown.click()
        # time.sleep(3)
        # allure.attach(driver.get_screenshot_as_png(), name="CheckingElementInDropDownInDropDown",
        #               attachment_type=allure.attachment_type.PNG)
        # time.sleep(5)

        checkGSTINNoDropDownNewOrg = driver.find_element(By.ID,"PR_4")
        highlight_element(checkGSTINNoDropDownNewOrg, driver)
        checkGSTINNoDropDownNewOrg.send_keys("1234567890")
        allure.attach(driver.get_screenshot_as_png(), name="checkGSTINNoDropDownNewOrg",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        checkDropDown2inDropDown = driver.find_element(By.XPATH,'(//i[@class="fi fi-ss-angle-small-down font-size-18"]'
                                                                '//parent::button[@class= "MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium'
                                                                ' MuiAutocomplete-popupIndicator css-uge3vf"])[2]')
        highlight_element(checkDropDown2inDropDown, driver)
        checkDropDown2inDropDown.click()
        allure.attach(driver.get_screenshot_as_png(), name="checkDropDown2inDropDown",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        checkEmailInNewOrgInDropDown = driver.find_element(By.ID,"PR_6")
        highlight_element(checkEmailInNewOrgInDropDown, driver)
        checkEmailInNewOrgInDropDown.send_keys("dineshkumar.pentakota@gmail.com")
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), name="checkEmailInNewOrgInDropDown",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        checkADDAddressInNewOrgInDropDown = driver.find_element(By.ID,"ADDADRS")
        highlight_element(checkADDAddressInNewOrgInDropDown, driver)
        checkADDAddressInNewOrgInDropDown.click()
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), name="checkADDAddressInNewOrgInDropDown",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        switchingToPopUpWindowToADDAddress = driver.window_handles[-1]
        driver.switch_to.window(switchingToPopUpWindowToADDAddress)
        allure.attach(driver.get_screenshot_as_png(), name="switchingToPopUpWindowToADDAddress",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(3)
        driver.find_element(By.ID,"ADDRESS_NEW").click()
        allure.attach(driver.get_screenshot_as_png(), name="switchingToPopUpWindowToADDAddress",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        checkTitleButtonInAddAddress = driver.find_element(By.ID,"ADD_1")
        highlight_element(checkTitleButtonInAddAddress, driver)
        checkTitleButtonInAddAddress.send_keys("DineshAddress")
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(), name="checkTitleButtonInAddAddress",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        checkCityButtonInAddAddress = driver.find_element(By.ID,"ADD_2")
        highlight_element(checkCityButtonInAddAddress, driver)
        checkCityButtonInAddAddress.send_keys("Anakapalli")
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(),name="checkCityButtonInAddAddress",
                      attachment_type=allure.attachment_type.PNG)








        checkPrefrencesInNewOrgInDropDown = driver.find_element(By.XPATH,'//span[text()="ALT + 1"]')
        highlight_element(checkPrefrencesInNewOrgInDropDown, driver)
        checkPrefrencesInNewOrgInDropDown.click()
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), name="checkPrefrencesInNewOrgInDropDown",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

        checkPrefrences1InNewOrgInDropDown = driver.find_element(By.XPATH, '//span[text()="Preferences"]')
        highlight_element(checkPrefrences1InNewOrgInDropDown, driver)
        checkPrefrencesInNewOrgInDropDown.click()
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), name="checkPrefrences1InNewOrgInDropDown",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

























        # driver.back()
        # time.sleep(5)
        # checkMyOrgButton = driver.find_element(By.XPATH,'//button[@class="btn btn-outline-secondary mt-0 font-size-12 btn-block b-r-3"]')
        # highlight_element(checkMyOrgButton, driver)
        # time.sleep(3)
        # allure.attach(driver.get_screenshot_as_png(), name="checkMyOrgButton",
        #               attachment_type=allure.attachment_type.PNG)
        # time.sleep(5)



