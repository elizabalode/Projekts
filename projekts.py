from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.city24.lv/"
driver.get(url)


wait = WebDriverWait(driver, 10)


wait.until(EC.presence_of_element_located((By.ID, "onetrust-reject-all-handler")))

find = driver.find_element(By.ID, "onetrust-reject-all-handler")
find.click()


element = wait.until(EC.element_to_be_clickable((By.XPATH, '//img[@onclick="onFinishedPlaying()"]')))
element.click()


find2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Atrašanās vieta, atslēgvārds, City24 ID..."]')))
find2.clear()
find2.send_keys("Skanste")


element2 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'autocomplete__item')))
element2.click()


element3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "btn--primary") and contains(@class, "btn--extended") and contains(@class, "search__search-btn")]')))
element3.click()


element4 = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[starts-with(text(), "Kārtot")]')))
element4.click()


element5 = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="select__option select__option--focused" and @value="price-asc"]')))
element5.click()


time.sleep(5)


img_element = driver.find_element(By.XPATH, '//img[@alt="Pārdod dzīvokli - Merks Duntes Zīles - jaunais projekts - Rīga, Skanste, Pededzes iela 3 - 61 m², 3 istabas, 170 000 € - City24.lv nekustamo īpašumu sludinājumu portāls"]')


img_url = img_element.get_attribute('src')


with open('url_list.txt', 'a') as file:
    file.write(img_url + '\n')


driver.quit()
