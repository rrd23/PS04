from selenium import webdriver

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import time

browser = webdriver.Chrome()

browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

assert "Википедия" in browser.title
time.sleep(8)

search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys("Планетная система")
search_box.send_keys(Keys.ENTER)

time.sleep(8)
a = browser.find_element(By.LINK_TEXT, "Планетная система")
a.click()









