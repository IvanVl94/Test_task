from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class ShopPage:
    def __init__(self, driver):
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
        
        
    # Заходим на сайт   
    def to_do_shop_test(self):
        self._driver.get("https://www.saucedemo.com/")
    
    # Регистрируемся
    def shop_form(self, name_user, password):
        self.driver.find_element(*self.name_user_input).send_keys(name_user)
        self.driver.find_element(*self.password_input).send_keys(password)
       
    def summit_button(self, button):
        self.driver.find_element(*self.login_button_input).click()
    
    # Довавляем элементы    
    def shop_button(self):
        self.summit_button(self.element_1_input)
        self.summit_button(self.element_2_input)
        self.summit_button(self.element_3_input)
    
    # Переходим в корзину    
    def shoping_cart_button(self):
        self.driver.find_element(*self.shoping_cart_input).click()
    
    def checkount_button(self):
        self.driver.find_element(*self.checkout_input).click()
    
    # Заносим свои данные    
    def shop_form(self, firstName, lastName, postalCode):
        self.driver.find_element(*self.firstName_input).send_keys(firstName)
        self.driver.find_element(*self.lastName_input).send_keys(lastName)
        self.driver.find_element(*self.postalCode_input).send_keys(postalCode)
        
    def continue_button(self):
        self.driver.find_element(*self.continue_input).click()
     
    # Вывод общей суммы закупок   
    def total_label(self):
        return self.driver.find_element(*self.total_label_input).text
        
        
    