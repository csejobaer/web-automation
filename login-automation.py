import csv 
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

import time


username = 'user'
pws = 'password'

driver = webdriver.Chrome()

driver.get('https://www.facebook.com')
time.sleep(2)

# Find an element using XPath for username field
user_field = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input')
user_field.send_keys(username)

# Find an element using XPath for password field
password_field = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input')
password_field.send_keys(pws)

# submit
submit_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
submit_btn.click()
