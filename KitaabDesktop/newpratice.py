import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from spellchecker import SpellChecker


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://kitaabdev.finsights.biz/"
driver.get(url)
driver.maximize_window()
time.sleep(5)


# driver.implicitly_wait(3)


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

        # print("the cookies found:", driver.get_cookies())

        # clickCreateNewOrganisation = driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-sm']")
        # clickCreateNewOrganisation.click()
        # time.sleep(5)

        # captureDisplaynamestar = driver.find_element(By.XPATH,'(//div[@class="p-rel"])[1]')
        # captureDisplaynamestar1 = captureDisplaynamestar.text
        # assert "*" in captureDisplaynamestar1, "Mandatory star (*) not found in Display Name field."

        # captureDisplayNameStar = driver.find_element(By.XPATH, '(//div[@class="p-rel"])[1]')
        # captureDisplayNameStar = captureDisplayNameStar.text
        #
        # if "*" in captureDisplayNameStar:
        #     print("Mandatory star (*) found in Display Name field.")
        # else:
        #     assert False, "Mandatory star (*) not found in Display Name field."
        # time.sleep(5)
        #
        # sendMore50characters = driver.find_element(By.XPATH, '//input[@id="PR_1"]')
        # legal_name = "A" * 51  # Creating a string with more than 50 characters
        # # legal_name = "ABC@#$"*14
        # sendMore50characters.send_keys(legal_name)
        # entered_text = sendMore50characters.get_attribute("value")
        # if len(entered_text) > 50:
        #     print("User was able to enter more than 50 characters.")
        # else:
        #     print("User cannot enter more than 50 characters.")
        #
        # time.sleep(5)

        # Locate the country element
        # country_element = driver.find_element(By.NAME,'country')
        # # Get the default value of the country element
        # default_country_value = country_element.get_attribute('value')
        # # Assert that the default value is "India"
        # assert default_country_value == "India", f"Expected default country to be 'India' but found '{default_country_value}'"
        # # Optionally, you can print a message to indicate success
        # print("Default country is 'India'")

        # country_element = driver.find_element(By.NAME,'country')
        # # Get the default value of the country element
        # default_country_value = country_element.get_attribute('value')
        # if default_country_value == "India":
        #     print("Default country is 'India'")
        # else:
        #     print("Default country is not 'India'")
        #
        # time.sleep(5)
        #
        # country_element1 = driver.find_element(By.NAME, 'country')
        # country_element1.click()
        # # Get the default value of the country element
        #
        # default_country_value = country_element1.get_attribute('value')
        # if default_country_value == "Haiti":
        #     print("Default country is 'Haiti'")
        # else:
        #     print("Default country is not 'Haiti'")
        #
        # # print("Default country is 'Haiti'") if default_country_value == "Haiti" else print("Default country is not 'Haiti'")
        # time.sleep(5)
        #
        # # Locate the incorporation type element
        # incorporation_type_element = driver.find_element(By.NAME, 'incorporationType')
        # # Get the default value of the incorporation type element
        # default_incorporation_type = incorporation_type_element.get_attribute('value')
        # # Assert that the default value is "Pvt.Ltd"
        # assert default_incorporation_type == "Private Limited Company", f"Expected default incorporation type to be 'Pvt.Ltd' but found '{default_incorporation_type}'"
        # # Optionally, you can print a message to indicate success
        # print("Default incorporation type is 'Pvt.Ltd'")

        print("the title of website:", driver.title)
        # clickoncreatebutton = driver.find_element(By.XPATH, '//a[@class="btn btn-primary dropdown-toggle h-36px"]')
        # clickoncreatebutton.click()
        # time.sleep(3)
        #
        # clickonmasters = driver.find_element(By.XPATH, '//button[@id="MODULE0"]')
        # clickonmasters.click()
        # time.sleep(3)
        #
        # clickonledgers = driver.find_element(By.XPATH,
        #                                      '//button[@class="btn btn-link btn-sm font-size-12 text-dark text-start text-color-3" and text()="Ledgers"]')
        # clickonledgers.click()
        # time.sleep(5)
        #
        # # Getledgertext = driver.find_element(By.XPATH, '//p[text()="Create Ledger"]')
        # # print('GetLegerText:', Getledgertext.text)
        # #
        # clickonundergroupdropdown = driver.find_element(By.XPATH, '//input[@name="underGroup"]')
        # clickonundergroupdropdown.click()
        # clickonledgerdropdown = driver.find_elements(By.XPATH,
        #                                              '//ul[@class="MuiAutocomplete-listbox autocomplete-listbox css-xul3t5"]//li')
        # # print("Number of elements in dropdown:",len(clickonledgerdropdown))
        #
        # Print the text of each element
        # for element in clickonledgerdropdown:
        #     print(f"Get the text elements in dropdown: {element.text}")
        # #     to print output in string format in console then we use print(f"Get the text elements in dropdown: {element.text}")
        #
        # # Wait for 5 seconds
        # time.sleep(5)

        # if u want to use get_attribute value then u can use this code
        # clickonledgername = driver.find_element(By.NAME, "name")
        # print(clickonledgername.text)
        # # print("the attribute value of id:", clickonledgername.get_attribute("id"))
        #
        # # ledger_under_group_dropdown = driver.find_element(By.XPATH, "//*[@id='i2-listbox']")
        # # list_of_values_in_group_dropdown = ledger_under_group_dropdown.find_elements(By.TAG_NAME, 'li')
        # # group_drop_down_count = len(list_of_values_in_group_dropdown)
        # # print(f'Number of values present in the group dropdown: {group_drop_down_count}')

        # submit method work same as enter button keyword
        # EnterTextinLedgers = driver.find_element(By.NAME, "name")
        # EnterTextinLedgers.send_keys("dinesh")
        # # EnterTextinLedgers.submit()
        # time.sleep(2)
        # EnterTextinLedgers.clear()

        # implementing webdriver wait to elements
        # checkcheckboxes = driver.find_element(By.XPATH, '//div[@class="p-checkbox p-component"]')
        # wait = WebDriverWait(driver, timeout=5, poll_frequency=1, ignored_exceptions=[Exception])
        # checkcheckboxes1 = wait.until(
        #     EC.element_to_be_clickable(checkcheckboxes))
        # checkcheckboxes1.click()

        # for i in range(1, 10):
        #     print(i)

        clickonkitaabimage = driver.find_element(By.XPATH,
                                                 '//img[@class="c-sidebar-brand-full mobile-logo-width img-fluid inside-logo-full"]')
        clickonkitaabimage.click()
        time.sleep(3)

        clickonstatutory = driver.find_element(By.XPATH,
                                               '(//button[@class="btn btn-link text-color-2 text-start l-h-15 p-20-total"])[5]')
        clickonstatutory.click()
        time.sleep(3)

        clickonewaybill = driver.find_element(By.XPATH, '(//div[@class="d-flex align-items-center"])[6]')
        clickonewaybill.click()
        driver.implicitly_wait(10)

        clickontable = driver.find_element(By.XPATH, '//div[@class="p-datatable-wrapper"]')
        rows = clickontable.find_elements(By.TAG_NAME, 'tr')

        header_row = rows[0]
        header_cells = header_row.find_elements(By.TAG_NAME, 'th')
        for cell in header_cells:
            print('\033[1m' + cell.text + '\033[0m', end="\t")
        # spell = SpellChecker()
        print()

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')

            for cell in cells:
                print(cell.text, end="\t")
                # misspelled = spell.unknown(cell.text.split())

                # If there are misspelled words, print them
                # if misspelled:
                #     corrected_words = [spell.correction(word) for word in misspelled]
                #     print("\nMisspelled words:", misspelled)
                #     print("Corrected words:", corrected_words)

            print()

        # clickoncreatenew = driver.find_element(By.XPATH, '(//*[contains(text()," Create EWB")])[1]')
        # clickoncreatenew.click()
        # clickontable1 = driver.find_element(By.XPATH, '//div[@class="table-responsive p-0"]')
        # rows1 = clickontable1.find_elements(By.TAG_NAME, 'tr')
        #
        # header_row = rows1[0]
        # header_cells = header_row.find_elements(By.TAG_NAME, 'th')
        # for cell in header_cells:
        #     print('\033[1m' + cell.text + '\033[0m', end="\t")
        #
        # print()
        #
        # for row in rows1:
        #     cells = row.find_elements(By.TAG_NAME, 'td')
        #
        #     for cell in cells:
        #         print(cell.text, end="\t")
        #
        #     print()

        clickonbulkgeneration = driver.find_element(By.XPATH, '//*[contains(text(),"Bulk Generation")]')
        clickonbulkgeneration.click()

        checkboxes = driver.find_elements(By.XPATH, '//div[@class="p-checkbox-box"]')
        for checkbox in checkboxes:
            checkbox.click()
            time.sleep(2)

            if all(checkbox.is_selected() for checkbox in checkboxes):
                print("all check boxes are clicked")
            else:
                print("all check boxes are not clicked")

        time.sleep(5)

        

