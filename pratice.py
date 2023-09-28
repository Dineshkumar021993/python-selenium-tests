import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://hrms.e-biz.in/login")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="inputEmail"]').send_keys("9599")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="inputPassword"]').send_keys("Lotus@111")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="inlineCheckbox"]').click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/app-root/app-login/div[1]/div/div[1]/form/div[4]/button").click()
time.sleep(30)
# driver.find_element(By.XPATH, "/html/body/app-root/eb-hrms-layout/div/header/nav/div/eb-user-menu/ul/li[2]/div/a").click()
# time.sleep(10)
# driver.find_element(By
#                     .XPATH, "/html/body/app-root/eb-hrms-layout/div/header/nav/div/eb-user-menu/ul/li[2]/div/div/div[2]/a").click()
# time.sleep(10)
# driver.find_element(By
#                     .XPATH, "/html/body/app-root/eb-hrms-layout/div/main/section/div/app-attendance/div[3]/div/eb-default-datatable/div/div/table/tbody/tr/td[2]/a").click()
# time.sleep(10)
# element = driver.find_element(By.XPATH, "/html/body/app-root/eb-hrms-layout/div/main/section/div/app-attendance/div[4]/div/div/div[1]/div/div[2]/div/div[1]/form/input")
# element.click()
# time.sleep(3)
# element.clear()
# time.sleep(3)
# element.send_keys("08/2023")
# time.sleep(3)
# element.send_keys(Keys.CONTROL + "a")
#
# # Send the new date again
# element.send_keys("08/2023")
# element.send_keys(Keys.ENTER)
# time.sleep(10)

driver.find_element(By
                    .XPATH, "/html/body/app-root/eb-hrms-layout/div/header/nav/div/eb-user-menu/ul/li[2]/div/a").click()
time.sleep(10)
driver.find_element(By
                    .XPATH, "/html/body/app-root/eb-hrms-layout/div/header/nav/div/eb-user-menu/ul/li[2]/div/div/div[4]/a").click()
time.sleep(10)
driver.find_element(By.XPATH,"/html/body/app-root/eb-hrms-layout/div/main/section/div/eb-emp-payslips/div[3]/eb-default-flexible-datatable/div/div/div[4]/div[2]/table/tbody/tr[1]/td[9]/button").click()
time.sleep(10)
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH,"/html/body/app-root/eb-hrms-layout/div/main/section/div/eb-payslip-view/div/div/div[1]/div/div[2]/div/a").click()
time.sleep(10)










