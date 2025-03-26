import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@allure.epic("Шопинг") 
@allure.severity("blocker")
@allure.title("Тестирование онлайн магазина")
@allure.description("В этом тест задании тестируется возможноть пользовалелей купить товар через сайт,с актуальной суммой за все товары")
@allure.feature("Регистрация, покупка товара, оплата товара, сравнение итоговой суммы с купленными товарами")

class ShopPage:
    """Этот класс передает
    сущность пользователя (логины, пароли, выбор товара, оплата)
    """
    def __init__(self, driver) -> str:
        self._driver = driver
        self.name_user_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button_input = (By.XPATH, "//input[@type='submit']")
        self.element_1_input= (By.ID, "add-to-cart-sauce-labs-backpack")
        self.element_2_input = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.element_3_input = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.shoping_cart_input = (By.XPATH, "//a[@class='shopping_cart_link']")
        self.checkout_input = (By.ID, "checkout")
        self.firstName_input = (By.NAME, "firstName")
        self.lastName_input =(By.NAME, "lastName")
        self.postalCode_input =(By.NAME, "postalCode")
        self.continue_input = (By.ID, "continue").click()
        self.total_label_input = (By.XPATH, "//div[@class='summary_total_label']")
        
        
     
    def to_do_shop_test(self)-> None:
        """Эта функция заходит на сайт"""
        with allure.step("Заходим на сайт"):
            self._driver.get("https://www.saucedemo.com/")
    
    
    def shop_form_credentials(self, name_user, password) -> str:
        
        """Эта функция помогает зарегистрироватся на сайте """
        with allure.step("Проходим регистрацию на сайте "):
        
            self.driver.find_element(*self.name_user_input).send_keys(name_user)
            self.driver.find_element(*self.password_input).send_keys(password)
   
    def summit_button(self, button)-> None:
        """Эта функция нажимает кнопку , чтобы ввойти в магазин """
        with allure.step("Нажимает 'Войти в магазин'"):
            self.driver.find_element(*self.login_button_input).click()
    
        
    def shop_button(self)-> None:
        """Эта функция помогает добавить товар в корзину """
        with allure.step("Добавляем товары "):
            self.summit_button(self.element_1_input)
            self.summit_button(self.element_2_input)
            self.summit_button(self.element_3_input)
    
       
    def shoping_cart_button(self)-> None:
        """Эта функция переходит в корзину"""
        with allure.step("Переходим в корзину "):
            self.driver.find_element(*self.shoping_cart_input).click()
    
    def checkount_button(self)-> None:
        """Эта функция переходит на страницу оплаты"""
        with allure.step("Переходим на страницу оплаты"):
            self.driver.find_element(*self.checkout_input).click()
    
       
    def shop_form(self, firstName, lastName, postalCode)-> str:
        """Эта функция помогает ввести данные для оплаты"""
        with allure.step("Вводим данные для оплаты "):
            self.driver.find_element(*self.firstName_input).send_keys(firstName)
            self.driver.find_element(*self.lastName_input).send_keys(lastName)
            self.driver.find_element(*self.postalCode_input).send_keys(postalCode)
        
    def continue_button(self)-> None:
        """Эта функция помогает нажать кнопку. для оплаты"""
        with allure.step("НАжимаем оплатить "):
            self.driver.find_element(*self.continue_input).click()
     
      
    def total_label(self) -> str:
        """Эта функция выводит общую сумму закупок"""
        with allure.step("Вводит общую сумму покупки "):
            return self.driver.find_element(*self.total_label_input).text
        
        
    