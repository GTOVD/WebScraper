
import pandas as pd
from bs4 import BeautifulSoup, element
from selenium import webdriver
import requests
from WebScraper.pram import credentials

<<<<<<< HEAD
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument('--incognito')

# session_key = credentials['username']
# session_password = credentials['password']
=======
driver = webdriver.Chrome(
    executable_path='C:/Users/vicke/Downloads/chromedriver.exe')
>>>>>>> 5459fb805da97599fd2d07beed21d377797f3ecc

# driver = webdriver.Chrome(
#     executable_path='C:/Users/vicke/Downloads/chromedriver.exe')

# driver.get('https://www.linkedin.com/login')
# driver.get('https://www.linkedin.com/company/hubspot/people/')

# elementID = driver.find_element_by_id('username')
# elementID.send_keys(session_key)
# elementID = driver.find_element_by_id('password')
# elementID.send_keys(session_password)
# elementID.submit()

content = open('WebScraper/linkedin.html', encoding='utf-8').read()

# print(content.read())
soup = BeautifulSoup(content, features="html.parser")

for element in soup.findAll("a", {"class": "ember-view"}):
    if element['href'].startswith('/in/'):
        link = element['href']

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'authority': 'www.linkedin.com'
}


r = requests.get('https://www.linkedin.com'+link, headers=headers)
print(r)
# if name not in results:
#     results.append(name.text)

# personID = 2010
# person = driver.find_element_by_id(personID).click()

# driver.back()


# Navitgation not working due to browser size and element names
# elementID2 = driver.find_element_by_id('global-nav-search')
# elementID2.click()

# elementID2 = driver.find_element_by_class_name(
#     'search-global-typeahead__input')
# elementID2.send_keys("hubspot")
# elementID2.submit()
# """

# """
# results = []
# content = driver.page_source
# soup = BeautifulSoup(content)

# for element in soup.findAll(attrs='scaffold-layout__main'):
#     name = element.find('div')
#     if name not in results:
#         results.append(name.text)

# print(results)

# # driver.find_element_by_class_name('search-global-typeahead__input')
# """
