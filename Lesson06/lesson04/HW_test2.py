from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")


#<a id="getButtonBoxLink" href="https://www.godaddy.com/domainsearch/find?key=parkweb&amp;utm_source=godaddy&amp;utm_medium=parkedpages&amp;utm_campaign=x_dom-broker_parkedpages_x_x_invest_001&amp;tmskey=dpp_dbs&amp;domainToCheck=seleniumeasy.com&amp;isc=GPPTCOM&amp;itc=parkedpage_landers">Приобрести этот домен</a>
# Найти элемент "getButtonBoxLink" и проверить его наличие
check_all_button = driver.find_element(
    By.ID, "getButtonBoxLink")
check_all_button.click()

print("Элемент 'getButtonBoxLink' найден и кликнут")

driver.quit()