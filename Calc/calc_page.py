from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class CalculPage:
    def __init__(self, driver):
        self._driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay") # Поле Задержки
        self.number_7 = (By.CSS_SELECTOR, "#seven")  # Кнопка 7
        self.number_8 = (By.CSS_SELECTOR, "#eight")  # Кнопка 8
        self.plus_button = (By.CSS_SELECTOR, "#add")  # Кнопка +
        self.equals_button = (By.CSS_SELECTOR, "#equals")  # Кнопка =
        self.result_display = (By.CSS_SELECTOR, "#result") # Результат

    def to_go_calc_page(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
    def set_delay(self, delay: int):
        self.driver.find_element(*self.delay_input).send_keys(str(delay))
        
    def button(self, button_locator):
        button_element = self.driver.find_elment(*button_locator).click()
        
    
    def calculate(self):
        self.button(self.number_7)
        self.button(self.plus_button)
        self.button(self.number_8)
        self.button(self.equals_button)
        
    def get_result(self):
        return self.driver.find_element(*self.result_display).text