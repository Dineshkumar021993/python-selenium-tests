import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://kitaabdev.finsights.biz/"
driver.get(url)
driver.maximize_window()
time.sleep(5)


def highlight_element(element):
    """Highlights a web element by changing its border and background color."""
    for _ in range(2):
        # Highlight by changing border and background color
        driver.execute_script("arguments[0].style.border='3px solid red'; arguments[0].style.backgroundColor='yellow';", element)
        time.sleep(1)
        # Remove the highlight by resetting styles
        driver.execute_script("arguments[0].style.border=''; arguments[0].style.backgroundColor='';", element)


Click_Sign_Up_Button = driver.find_element(By.XPATH,
                                           "/html/body/div/form/div/div/div/div/div/div[2]/div[1]/a/span")
highlight_element(Click_Sign_Up_Button)
Click_Sign_Up_Button.click()
time.sleep(5)

Enter_UserName = driver.find_element(By.NAME, "email")
highlight_element(Enter_UserName)
Enter_UserName.send_keys("dineshkumar.pentakota@gmail.com")
time.sleep(5)

Enter_Password = driver.find_element(By.ID, "password")
highlight_element(Enter_Password)
Enter_Password.send_keys("Dinesh@#4")
time.sleep(5)

Checking_PasswordEye = driver.find_element(By.XPATH, "/html/body/div/form/div/div[2]/div/div/div/div[3]/div/div[1]/span/div/button/i")
highlight_element(Checking_PasswordEye)
Checking_PasswordEye.click()
time.sleep(5)


EnterPhone_Number = driver.find_element(By.NAME, "phoneNumber")
highlight_element(EnterPhone_Number)
EnterPhone_Number.send_keys("7842773980")
time.sleep(5)

Clicking_on_Agree_Terms_And_Policies = driver.find_element(By.XPATH,
                                                           "/html/body/div/form/div/div[2]/div/div/div/div[5]/div/div/div[1]/label/div/div[2]")
highlight_element(Clicking_on_Agree_Terms_And_Policies)
Clicking_on_Agree_Terms_And_Policies.click()
time.sleep(5)

Proceed_Button = driver.find_element(By.XPATH, "/html/body/div/form/div/div[2]/div/div/div/div[6]/div/div")
highlight_element(Proceed_Button)
Proceed_Button.click()
time.sleep(5)
