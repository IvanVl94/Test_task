import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@allure.epic("Калькулятор") 
@allure.severity("blocker")
@allure.title("Тестирование калькулятора")
@allure.description("В этом тест задании тестируется, функционал калькулятора")
@allure.feature("Сложение чисел и вывод результата")

class CalculPage:
    
    """Этот класс передает функционал  калькулятора
    """
    def __init__(self, driver)  -> int:
       
        self._driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay") # Поле Задержки
        self.number_7 = (By.CSS_SELECTOR, "#seven")  # Кнопка 7
        self.number_8 = (By.CSS_SELECTOR, "#eight")  # Кнопка 8
        self.plus_button = (By.CSS_SELECTOR, "#add")  # Кнопка +
        self.equals_button = (By.CSS_SELECTOR, "#equals")  # Кнопка =
        self.result_display = (By.CSS_SELECTOR, "#result") # Результат
   


    def to_go_calc_page(self)-> None:
        with allure.step("Зайти на сайт"):
             self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
    def set_delay(self, delay: int) -> int:
        with allure.step("Ввести число"):
            self.driver.find_element(*self.delay_input).send_keys(str(delay))
        
    def button(self, button_locator)-> None:
        with allure.step("Нажать на кнопку "):
            button_element = self.driver.find_elment(*button_locator).click()
        
    
    def calculate(self) -> int:
        with allure.step("Нажать на кнопки 7 + 8 ="):
            self.button(self.number_7)
            self.button(self.plus_button)
            self.button(self.number_8)
            self.button(self.equals_button)
        
    def get_result(self)-> None:
        return self.driver.find_element(*self.result_display).text