import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from shop_page import ShopPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  
    yield driver
    driver.quit()

def form_shop_test(driver):
    form_shop = ShopPage(driver)
    # Заходим на сайт   
    form_shop.to_do_shop_test()
    # Регистрируемся
    form_shop.shop_form(
        name_user="standard_user",
        password="secret_sauce"
    )
    
    form_shop.summit_button()
    
    # Довавляем элементы
    form_shop.shop_button()
    
    # Переходим в корзину
    form_shop.shoping_cart_button()
    form_shop.checkount_button()
    
    # Заносим свои данные
    form_shop.shop_form(
        firstName="Иван",
        lastName="Власов",
        postalCode="413311"
    )
    form_shop.continue_button()
    
    # Вывод общей суммы закупок
    
    total_result = form_shop.total_label()
    assert total_result == "Total: $58.29" , "Итоговая сумма должны быть 58.29"
    
    
    
    
    
    
    



























    
def test_shopping(driver):  
    driver.get("https://www.saucedemo.com/")


# Авторизуемся
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    
# Добавляем товары в корзину
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()


    driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
 
 # Нажимаем Checkout
    driver.find_element(
        By.ID, "checkout").click()

    driver.find_element(By.NAME, "firstName").send_keys("Иван")
    driver.find_element(By.NAME, "lastName").send_keys("Власов")
    driver.find_element(By.NAME, "postalCode").send_keys("413311")

  # Нажимаем Continue
    driver.find_element(
        By.ID, "continue").click()

    total_element = WebDriverWait(driver, 45).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='summary_total_label']"))
)

# Проверяем, что итоговая сумма равна $58.29

    assert "Total: $58.29" in total_element.text, f"Expected total to be $58.29, but got {total_element.text}"
    
    driver.quit()





