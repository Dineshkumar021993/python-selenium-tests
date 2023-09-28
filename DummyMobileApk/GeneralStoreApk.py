from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

# Desired capabilities
desired_caps = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'platformVersion': '12.0',
    'deviceName': 'Generalstore',
    'app': 'D:\\Tools\\APKFiles-1\\resources\\General-store.apk',
    'appPackage': 'com.androidsample.generalstore',
    'appActivity': 'com.androidsample.generalstore.SplashActivity'
}

driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
driver.implicitly_wait(10)

drop_down_click = driver.find_element(MobileBy.ID, "android:id/text1")
drop_down_click.click()

select_element_onDropDown = driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@index='7']")
select_element_onDropDown.click()

Enter_Text = driver.find_element(MobileBy.ID, "com.androidsample.generalstore:id/nameField")
Enter_Text.send_keys("P.Dinesh Kumar")

RadioButton_Male = driver.find_element(MobileBy.ID, "com.androidsample.generalstore:id/radioMale")
RadioButton_Male.click()

RadioButton_FeMale = driver.find_element(MobileBy.ID, "com.androidsample.generalstore:id/radioFemale")
RadioButton_FeMale.click()

LetsShop_button = driver.find_element(MobileBy.ID, "com.androidsample.generalstore:id/btnLetsShop")
LetsShop_button.click()

driver.implicitly_wait(5)
# scrolling page

for i in range(3):
    start_x = 546
    start_y = 2017
    end_x = 569
    end_y = 437
    duration = 400
    driver.swipe(start_x, start_y, end_x, end_y, duration)

driver.implicitly_wait(5)

# scrolling back again
for i in range(3):
    start_x = 597
    start_y = 332
    end_x = 624
    end_y = 1840
    duration = 400
    driver.swipe(start_x, start_y, end_x, end_y, duration)


# finding element
driver.implicitly_wait(5)
driver.find_element(MobileBy.XPATH,'//android.widget.TextView[@text="ADD TO CART"]').click()

start_x = 560
start_y = 2109
end_x = 560
end_y = 597
duration = 400
driver.swipe(start_x, start_y, end_x, end_y, duration)


driver.find_element(MobileBy
                    .XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[2]').click()

# check product items
driver.find_element(MobileBy.ID,"com.androidsample.generalstore:id/appbar_btn_cart").click()

# click on send emails button
driver.find_element(MobileBy.XPATH,'//android.widget.CheckBox[@text="Send me e-mails on discounts related to selected products in future"]').click()

# uncheck the button
driver.find_element(MobileBy.XPATH,'//android.widget.CheckBox[@text="Send me e-mails on discounts related to selected products in future"]').click()

# # please read terms and conditions
# driver.find_element(MobileBy.XPATH,'//android.widget.TextView[@text="Please read our terms of conditions"]').click()

# check main website for payment
driver.find_element(MobileBy.XPATH,'//android.widget.Button[@text="Visit to the website to complete purchase"]').click()

driver.implicitly_wait(5)