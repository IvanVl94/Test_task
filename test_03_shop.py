import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://www.saucedemo.com/")


WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.NAME, "user-name")))
WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.NAME, "password")))
WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.NAME, "login-button")))


user_name_login = driver.find_element(
    By.NAME, "user-name")
user_name_login.send_keys("standard_user")
user_password = driver.find_element(
    By.NAME, "password")
user_password.send_keys("secret_sauce")

driver.find_element(
    By.ID, "login-button").click()

#<button class="btn btn_primary btn_small btn_inventory " data-test="add-to-cart-sauce-labs-backpack" id="add-to-cart-sauce-labs-backpack" name="add-to-cart-sauce-labs-backpack">Add to cart</button>
#<button class="btn btn_primary btn_small btn_inventory " data-test="add-to-cart-sauce-labs-bolt-t-shirt" id="add-to-cart-sauce-labs-bolt-t-shirt" name="add-to-cart-sauce-labs-bolt-t-shirt">Add to cart</button>
#<button class="btn btn_primary btn_small btn_inventory " data-test="add-to-cart-sauce-labs-onesie" id="add-to-cart-sauce-labs-onesie" name="add-to-cart-sauce-labs-onesie">Add to cart</button>


driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()


driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()

driver.find_element(
    By.ID, "checkout").click()

First_name = driver.find_element(
    By.NAME, "firstName")
First_name.send_keys("Иван")

Last_name = driver.find_element(
    By.NAME, "lastName")
Last_name.send_keys("secret_sauce")

postal_code = driver.find_element(
    By.NAME, "postalCode")
postal_code.send_keys("413311")

driver.find_element(
    By.ID, "continue").click()

total_element = WebDriverWait(driver, 45).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='summary_total_label']"))
)
total = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text

print(total)

assert total == 'Total: $58.29'


sleep(5)
driver.quit()

