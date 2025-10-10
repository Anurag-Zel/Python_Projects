from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com')

input = driver.find_element_by_name('q')
input.send_keys('selenium')
time.sleep(5)

button = driver.find_element_by_name('btnK')
button.click()