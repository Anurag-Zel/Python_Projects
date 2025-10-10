from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.amazon.in')
driver.maximize_window()

time.sleep(5)

button1 = driver.find_element_by_link_text('Electronics')
button1.click()

time.sleep(5)

button2 = driver.find_element_by_link_text('Audio')
button2.click()

time.sleep(5)

driver.quit()