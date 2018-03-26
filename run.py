#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import time

usernameStr = "your_username_here"
passwordStr = "your_password_here"

driver = webdriver.Chrome("/home/shubham/Desktop/project/WebLogin/chromedriver")
driver.get(('https://www.flipkart.com/account/login?from=header'))
username = driver.find_element_by_xpath("//input[@class='_2zrpKA']")
username.send_keys(usernameStr)
password = driver.find_element_by_name('cpass')
password.send_keys(passwordStr)

signInButton = driver.find_element_by_xpath("//input[@value='Login']")
signInButton.click()
