from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.google.com/")

search_box = driver.find_element(By.NAME, 'q')

search_box.send_keys("Python programming")
search_box.send_keys(Keys.RETURN)

driver.implicitly_wait(10)

titles = driver.find_elements(By.XPATH, '//h3')

for title in titles:
    print(title.text)

driver.quit()