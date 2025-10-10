from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time

driver = webdriver.Chrome()
driver.get('https://facebook.com')
emailelement = driver.find_element(By.XPATH, '//*[@id="email"]')
emailelement.send_keys('k56378944@gmail.com')

passelement = driver.find_element(By.XPATH,'//*[@id="pass"]')
passelement.send_keys('Darkzel123')

elem = driver.find_element(By.XPATH, "//button[@type='submit']")
elem.click()

take_tour = driver.find_element(By.XPATH, "//*[text()='Take a Privacy Tour']")
time.sleep(5)
take_tour.click()
time.sleep(5)

button1 = driver.find_element(By.XPATH, "//*[text()='Next']")
button1.click()
time.sleep(5)


driver.close()




