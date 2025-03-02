from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class FormPage:
    def __init__(self, driver): 
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
        
    def to_go_form_page(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
            
    def fill_form(self, first_name, last_name, address, email, phone_number, zip_code, city, job_position, company):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.address_input).send_keys(address)
        self.driver.find_element(*self.phone_number_input).send_keys(phone_number)
        self.driver.find_element(*self.zip_code_input).send_keys(zip_code)
        self.driver.find_element(*self.city_input).send_keys(city)
        self.driver.find_element(*self.job_position_input).send_keys(job_position)
        self.driver.find_element(*self.company_input).send_keys(company)
    
    def summit_button(self):
        self.driver.find_element(*self.button_input).click()
    
    def get_zip_code_field_color(self):
        return self.driver.find_element(*self.zip_code_input).get_attribute('class')
    
    def get_colors_other(self):
        colors = {}
        for field in [self.first_name_input, self.last_name_input, self.address_input, 
            self.email_input, self.phone_number_input, self.city_input, 
            self.country_input, self.job_position_input, self.company_input]:
            colors[field] = self.driver.find_element(*field).value_of_css_property("border-color")
        
        return colors
        
        