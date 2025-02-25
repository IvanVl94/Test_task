from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver.get("http://the-internet.herokuapp.com/inputs")
sleep(5)

type_number = driver.find_element(
    By.XPATH,"//input[@type='number']")

type_number.send_keys('1000')

sleep(2)

type_number.clear()

type_number.send_keys('999')

sleep(2)

driver.quit()