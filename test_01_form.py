import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
 
# Тест
def test_form_(driver):
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
 
# Заполнение формы
    first_name = driver.find_element(By.NAME, "first-name")
    first_name.clear()
    first_name.send_keys("Иван")
 
    last_name = driver.find_element(By.NAME, "last-name")
    last_name.clear()
    last_name.send_keys("Петров")
 
    address = driver.find_element(By.NAME, "address")
    address.clear()
    address.send_keys("Ленина, 55-3")
 
    email = driver.find_element(By.NAME, "e-mail")
    email.clear()
    email.send_keys("test@skypro.com")
 
    phone_number = driver.find_element(By.NAME, "phone")
    phone_number.clear()
    phone_number.send_keys("+7985899998787")
 
    zip_code = driver.find_element(By.NAME, "zip-code")
    zip_code.clear()
    zip_code.send_keys("")
 
    city = driver.find_element(By.NAME, "city")
    city.clear()
    city.send_keys("Москва")
 
    country = driver.find_element(By.NAME, "country")
    country.clear()
    country.send_keys("Россия")
 
    job_position = driver.find_element(By.NAME, "job-position")
    job_position.clear()
    job_position.send_keys("QA")
 
    company = driver.find_element(By.NAME, "company")
    company.clear()
    company.send_keys("SkyPro")
 
    # Нажатие на кнопку

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