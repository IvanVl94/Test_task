import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.NAME, "first-name")))
WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.NAME, "last-name")))
WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.NAME, "address")))
WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.NAME, "e-mail")))
WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.NAME, "city")))
WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.NAME, "phone")))
WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.NAME, "country")))
WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.NAME, "zip-code")))
WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.NAME, "job-position")))
WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.NAME, "company")))


first_name = driver.find_element(
    By.NAME, "first-name")
first_name.send_keys("Иван")
last_name = driver.find_element(
    By.NAME, "last-name")
last_name.send_keys("Петров")
Address = driver.find_element(
    By.NAME, "address")
Address.send_keys("Ленина, 55-3")
E_mail = driver.find_element(
    By.NAME, "e-mail")
E_mail.send_keys("test@skypro.com")
Phone = driver.find_element(
    By.NAME, "phone")
Phone.send_keys("+7985899998787")
Zip_code = driver.find_element(
    By.NAME, "zip-code")
Zip_code.send_keys("")  # Оставляем пустым
City = driver.find_element(By.NAME, "city")
City.send_keys("Москва")
Contry = driver.find_element(
    By.NAME, "country")
Contry.send_keys("Россия")
Jod = driver.find_element(
    By.NAME, "job-position")
Jod.send_keys("QA")
Company  = driver.find_element(
    By.NAME, "company")
Company.send_keys("SkyPro")

driver.find_element(
    By.XPATH, "//button[contains(text(), 'Submit')]").click()

# Проверяем, что поле Zip code подсвечено красным

def color_zip():
    assert "alert-danger" in driver.find_element(By.ID, 'zip-code').get_attribute('class')

def colors_another_():
    assert 'alert-success' in driver.find_element(By.ID, 'first-name').get_attribute('class')
    assert 'alert-success' in driver.find_element(By.ID, 'last-name').get_attribute('class')
    assert 'alert-success' in driver.find_element(By.ID, 'address').get_attribute('class')
    assert 'alert-success' in driver.find_element(By.ID, 'e-mail').get_attribute('class')
    assert 'alert-success' in driver.find_element(By.ID, 'phone').get_attribute('class')
    assert 'alert-success' in driver.find_element(By.ID, 'city').get_attribute('class')
    assert 'alert-success' in driver.find_element(By.ID, 'job-position').get_attribute('class')
    assert 'alert-success' in driver.find_element(By.ID, 'company').get_attribute('class')
    assert 'alert-success' in driver.find_element(By.ID, 'country').get_attribute('class')

driver.quit()