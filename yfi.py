#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

usernameStr = "put_your_username_here"
passwordStr = "put_your_password_here"

driver = webdriver.Chrome("/home/shubham/Desktop/project/WebLogin/chromedriver")
driver.get(('http://user.yfibroadband.net/default_customer.asp')) 
username = driver.find_element_by_name('loginid')
username.send_keys(usernameStr)
password = driver.find_element_by_name('cpass')
password.send_keys(passwordStr)

signInButton = driver.find_element_by_xpath("//input[@value='Login']")
signInButton.click()
