from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("http://uitestingplayground.com/textinput")

#<input class="form-control" type="text" placeholder="MyButton" id="newButtonName">
rename_but = driver.find_element(
    By.CSS_SELECTOR, "#newButtonName")

rename_but.send_keys('SkyPro')
#<button class="btn btn-primary" type="button" id="updatingButton">Button That Should Change it's Name Based on Input Value</button>
add_buttom = driver.find_element(
    By.CSS_SELECTOR, "#updatingButton")
add_buttom.click()

#<button class="btn btn-primary" type="button" id="updatingButton">SkyPro</button>
element = driver.find_element(
    By.LINK_TEXT, "SkyPro")

txt = element.text

print(txt)

driver.quit()