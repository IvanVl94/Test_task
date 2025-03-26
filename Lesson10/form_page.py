import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

@allure.epic("Форма пользователя на странице") 
@allure.severity("blocker")
@allure.title("Тестирование формы сайта с данными о пользователе")
@allure.description("В этом тест задании тестируется, заполнение формы с данными на выявление багов, при пустой ячейке")
@allure.feature("Ввод данных пользователя и регистрация, с пустой ячейкой")

class FormPage:
    """Этот класс передает 
    сущность пользователя и данные для заполнения страницы"""
    
    def __init__(self, driver) -> str: 
        with allure.step("Ввести данные пользователя"):
            self._driver = driver
            self.first_name_input = (By.NAME, "first-name")
            self.last_name_input = (By.NAME, "last-name")
            self.address_input = (By.NAME, "address")
            self.email_input = (By.NAME, "e-mail")
            self.phone_number_input = (By.NAME, "phone")
            self.zip_code_input = (By.NAME, "zip-code")
            self.city_input = (By.NAME, "city")
            self.country_input = (By.NAME, "country")
            self.job_position_input = (By.NAME, "job-position")
            self.company_input = (By.NAME, "company")
            self.button_input = (By.XPATH, "//button[contains(text(), 'Submit')]")
        
    def to_go_form_page(self) -> None:
        """Эта функция переходит на сайт"""
        with allure.step("Переходим на сайт"):
            self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
            
    def fill_form(self, first_name, last_name, address, email, phone_number, zip_code, city, job_position, company) -> str:
        """Эта функция помогает внести данные пользователя"""
        with allure.step("Вводим данные "):
            self.driver.find_element(*self.first_name_input).send_keys(first_name)
            self.driver.find_element(*self.last_name_input).send_keys(last_name)
            self.driver.find_element(*self.email_input).send_keys(email)
            self.driver.find_element(*self.address_input).send_keys(address)
            self.driver.find_element(*self.phone_number_input).send_keys(phone_number)
            self.driver.find_element(*self.zip_code_input).send_keys(zip_code)
            self.driver.find_element(*self.city_input).send_keys(city)
            self.driver.find_element(*self.job_position_input).send_keys(job_position)
            self.driver.find_element(*self.company_input).send_keys(company)
    
    def summit_button(self)-> None:
        """Эта функция помогает нажать кнопку"""
        with allure.step("Нажать на кнопку"):
            self.driver.find_element(*self.button_input).click()
    
    def get_zip_code_field_color(self)-> str:
        """Эта функция помогает определить какая ячейки выделена крассным цветом"""
        with allure.step("Проверяем цвет ячейки"):
            return self.driver.find_element(*self.zip_code_input).value_of_css_property("background-color")
    
    def get_colors_other(self)-> str:
        """Эта функция помогает определить какие ячейки выделена зеленым  цветом"""
        with allure.step("Проверяем цвет остальных ячейек"):
            colors = {}
            for field in [self.first_name_input, self.last_name_input, self.address_input, 
                self.email_input, self.phone_number_input, self.city_input, 
                self.country_input, self.job_position_input, self.company_input]:
                colors[field] = self.driver.find_element(*field).value_of_css_property("border-color")
        
            return colors
        
        