from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome()
driver.maximize_window()

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Находим кнопку "Add Element" и нажимаем на нее 5 раз

add_button = driver.find_element(
    By.XPATH, "//button[text()='Add Element']")
for _ in range(5):
    add_button.click()

# <button class="added-manually" onclick="deleteElement()">Delete</button>

delete_buttons = driver.find_elements(
    By.XPATH, "//button[text()='Delete']")

# Выводим размер списка
print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

sleep(4)

driver.quit()