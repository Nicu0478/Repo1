import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()

# BY ID:

chrome.get("https://formy-project.herokuapp.com/form")
first_name_field = chrome.find_element(By.ID, "first-name")
first_name_field.send_keys("Ion")
time.sleep(4)

chrome.get("https://formy-project.herokuapp.com/autocomplete")
street_number_field = chrome.find_element(By.ID, "street_number")
street_number_field.send_keys("IL Caragiale")
time.sleep(4)

chrome.get("https://formy-project.herokuapp.com/autocomplete")
locality_field = chrome.find_element(By.ID, "locality")
locality_field.send_keys("Botosani")
time.sleep(3)'''

# Link text:

'''chrome.get("https://formy-project.herokuapp.com/")
checkbox = chrome.find_element(By.LINK_TEXT, "Checkbox").click()
checkbox.click()
time.sleep(3)

chrome.get("https://formy-project.herokuapp.com/")
dropdown = chrome.find_element(By.LINK_TEXT, "Dropdown").click()
dropdown.click()
time.sleep(3)

chrome.get("https://formy-project.herokuapp.com/")
inputs = chrome.find_element(By.LINK_TEXT, "Inputs").click()
inputs.click()
time.sleep(3)

# Parțial link text:

chrome.get("https://formy-project.herokuapp.com/")
horizontal_link = chrome.find_elements(By.PARTIAL_LINK_TEXT, "Horizontal")
time.sleep(3)

chrome.get('https://the-internet.herokuapp.com/')
java_script_link = chrome.find_elements(By.PARTIAL_LINK_TEXT, 'Java')[1].click()
time.sleep(3)

chrome.get('https://the-internet.herokuapp.com/')
hovers_link = chrome.find_element(By.PARTIAL_LINK_TEXT, "Hovers").click()
time.sleep(3)'''

# Nume:

'''chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
first_name_field = chrome.find_element(By.NAME, "firstname").send_keys("Gigel")
time.sleep(3)

last_name_field = chrome.find_element(By.NAME, 'lastname').send_keys('Buruiana')
time.sleep(3)
'''
'''chrome.get('https://phptravels.net/')
where_to_field = chrome.find_element(By.NAME, 'to').send_keys('Tenerife')
time.sleep(3)'''

# Tag:

'''chrome.get("https://the-internet.herokuapp.com/")
user_field = chrome.find_element(By.TAG_NAME, "input")
user_field.send_keys("tomsmith")
time.sleep(2)

password_field = chrome.find_elements(By.TAG_NAME, 'input')[1]
password_field.send_keys('SuperSecretPassword!')
time.sleep(2)

login_button = chrome.find_elements(By.TAG_NAME, 'input')[2]
login_button.click()
time.sleep(2)'''



# Class name:

'''chrome.get('https://formy-project.herokuapp.com//form')
form = chrome.find_elements(By.CLASS_NAME, 'form-control')
form[0].send_keys('Gigi')
form[1].send_keys('Maxim')
form[2].send_keys('Ospatar')
time.sleep(3)'''

# CSS:

#ID
'''chrome.get('https://formy-project.herokuapp.com/form')
first_name_field = chrome.find_element(By.CSS_SELECTOR,'#first-name')
first_name_field.send_keys('Gigi')
time.sleep(3)

# Class
last_name_field = chrome.find_elements(By.CSS_SELECTOR, '.form-control')[1]
last_name_field.send_keys('Ion')
time.sleep(3)

#Xpath

chrome.get('https://www.saucedemo.com/')
username_field = chrome.find_element(By.XPATH, "//input[@id = 'user-name']").send_keys('standard_user')
time.sleep(3)

password_field = chrome.find_element(By.XPATH, "//input[@type = 'password']").send_keys('secret_sauce')
time.sleep(3)

login_field = chrome.find_element(By.XPATH, "//input[@value = 'Login']").click()
time.sleep(3)
