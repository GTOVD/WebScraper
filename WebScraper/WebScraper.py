
import pandas as pd
from bs4 import BeautifulSoup, element
from selenium import webdriver

driver = webdriver.Chrome(
    executable_path='C:/Users/vicke/Downloads/chromedriver.exe')

driver.get('https://www.linkedin.com/login')

elementID = driver.find_element_by_id('username')
elementID.send_keys(session_key)
elementID = driver.find_element_by_id('password')
elementID.send_keys(session_password)
elementID.submit()

driver.implicitly_wait(5)

elementID2 = driver.find_element_by_id('global-nav-search').click()

elementID2.send_keys('hubspot')

elementID2.submit()


"""
results = []
content = driver.page_source
soup = BeautifulSoup(content)

for element in soup.findAll(attrs='scaffold-layout__main'):
    name = element.find('div')
    if name not in results:
        results.append(name.text)

print(results)

# driver.find_element_by_class_name('search-global-typeahead__input')
"""
