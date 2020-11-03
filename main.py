from selenium import webdriver

site = input()
driver = webdriver.Chrome()
driver.get(site)
driver.close()
