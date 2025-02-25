from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("http://uitestingplayground.com/ajax")


#<p class="bg-success">Data loaded with AJAX get request.</p>
add_buttom = driver.find_element(
    By.CSS_SELECTOR, "#ajaxButtom")
add_buttom.click()

element = driver.find_element(
    By.LINK_TEXT, "Data loaded with AJAX get request")

txt = element.text

print(txt)

driver.quit()