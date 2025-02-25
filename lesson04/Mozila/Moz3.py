
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")
sleep(2)

username = driver.find_element(
    By.ID,"userneme")

username.send_keys('tomsmith')

sleep(2)

password = driver.find_element(
    By.ID,"password")

password.send_keys('SuperSecretPassword!')

#<i class="fa fa-2x fa-sign-in"> Login</i>

login_button = driver.find_element(
    By.CLASS_NAME,"fa fa-2x fa-sign-in")

login_button.click()


driver.quit()