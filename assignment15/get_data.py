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

list = driver.find_elements_by_xpath("//span[@class = 'a-size-medium a-color-base a-text-normal']")

print(str(len(list)) + 'products found')

for i in list:
    print(i.text)


driver.quit()