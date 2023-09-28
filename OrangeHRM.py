import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

time.sleep(10)
driver.find_element(By.CLASS_NAME, "oxd-input").send_keys("Admin")

time.sleep(5)
element = driver.find_element(By
                              .XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
element.send_keys("admin123")
time.sleep(5)
element1 = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
element1.click()
time.sleep(10)
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a').click()
time.sleep(5)
element = driver.find_element(By
                              .XPATH,
                              '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input')
element.send_keys("pentakota")
time.sleep(5)
driver.find_element(By.NAME, "middleName").send_keys("Dinesh")
time.sleep(5)
driver.find_element(By.NAME, "lastName").send_keys("kumar")
time.sleep(5)
element = driver.find_element(By
                              .XPATH,
                              '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
element.click()
time.sleep(3)
element.clear()
time.sleep(3)
element.send_keys("961")
time.sleep(5)
element.send_keys(Keys.CONTROL + "a")

# Send the new date again
element.send_keys("961")
time.sleep(5)
# login to new user
# (driver.find_element(By
#                      .XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span")
#  .click())
# time.sleep(5)
# (driver.find_element(By.XPATH,
#                      "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input")
#  .send_keys("dineshkumar"))
# driver.find_element(By.XPATH,
#                     "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div/label/span").click()
# time.sleep(5)
# driver.find_element(By.XPATH,
#                     "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input").send_keys(
#     "dinesh@#4")
# time.sleep(5)
# driver.find_element(By.XPATH,
#                     "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input").send_keys(
#     "dinesh@#4")
# time.sleep(5)

# upload a photo
# driver.switch_to.frame(0)
# element = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div")
# element.click()
# time.sleep(10)
# element.send_keys("D://pictures/resultset.jpg")
# time.sleep(10)

driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
time.sleep(10)
# driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input").send_keys("123456789")
# time.sleep(5)
# element = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/i")
# time.sleep(5)
# element.click()
# time.sleep(5)
# driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input").click()
# time.sleep(10)

element = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[1]/div/div/div/div[2]/div/div[1]")
time.sleep(5)
element.click()
time.sleep(5)

element.send_keys("C:\\Users\\Dinesh\\Picturesresultset.jpg")



