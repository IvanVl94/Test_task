import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from calc_page import CalculPage

@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()

def calculate_test(driver):
    Calc_page = CalculPage(driver)
    # Заходим на страницу
    
    Calc_page.to_go_calc_page()
    
    # Задержка
    
    Calc_page.set_delay(45)
    
    # Вводим числа
    Calc_page.calculate()
    
    # Результат
    
    result = Calc_page.get_result()
    assert result == 15, "Результат должен быть равен 15"
