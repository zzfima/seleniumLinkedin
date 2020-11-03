from selenium import webdriver
from selenium.webdriver.common.by import By

site = input('input site')
min_friends_amount = input('input minimal other shared connections')
driver = webdriver.Chrome()
driver.get(site)

while True:
    el = driver.find_elements_by_class_name("li")

    for a in el:
        pass

driver.close()
