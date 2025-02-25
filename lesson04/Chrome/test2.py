from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome()
driver.maximize_window()

#Запустить 

driver.get("http://uitestingplayground.com/dynamicid")
#<button class="btn btn-primary" type="button" id="4dc2e406-2e7b-be74-0cfb-262cbc83aca7">Button with Dynamic ID</button>
blue_button = driver.find_element(
    By.XPATH,"//button[text()='Button with Dynamic ID']")

blue_button.click()

sleep(4)

driver.quit()