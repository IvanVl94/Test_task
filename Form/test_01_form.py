import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from form_page import FormPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    
def form_submission(driver):
    form_page = FormPage(driver)
    
    # Переход на страницу формы
    form_page.to_go_form_page() 

    # Заполнение формы
    
    form_page.fill_form(
        first_name="Иван",
        last_name="Петров",
        address="Ленина, 55-3",
        email="test@skypro.com",
        phone="+7985899998787",
        zip_code="",             # Оставляем пустым
        city="Москва",
        country="Россия",
        job_position="QA",
        company="SkyPro"
    )
    
    form_page.summit_button()
    
    
    zip_code_color = form_page.get_zip_code_field_color()
    assert zip_code_color == "rgb(255, 0, 0)", "Поле Zip code должно быть подсвечено красным"
     
    other_colors = form_page.get_colors_other()
    for field, color in other_colors.items():
        assert color == "rgb(0, 128, 0)", f"Поле {field} должно быть подсвечено зеленым" 

 
