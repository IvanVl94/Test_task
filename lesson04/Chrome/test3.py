from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome()
driver.maximize_window()

#Запустить 

driver.get("http://uitestingplayground.com/classattr")

#<button class="btn class2 btn-primary btn-test" type="button">Button</button>

blue_button = driver.find_element(
    By.XPATH,"//button[contains(concat(' ', normalize-space(@class), ' '), 'btn-primary ')]")


blue_button.click()

sleep(4)

driver.quit()