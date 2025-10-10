from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.amazon.in')

driver.maximize_window()
time.sleep(5)

driver.find_element_by_xpath("//input[@id = 'twotabsearchtextbox']").send_keys('iphones')
time.sleep(5)

driver.find_element_by_xpath("//input[@id = 'nav-search-submit-button']").click()
time.sleep(5)


driver.quit()