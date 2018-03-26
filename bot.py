# Auto login bot with python and selenium

# importing the modules

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Here enter your username and password

usernameStr = 'putYourUsernameHere'
passwordStr = 'putYourPasswordHere'

# Instruct a browser window to open Google Chrome, and navigate to Gmail’s login page.
# Enter your desired web-login page here

browser = webdriver.chrome()
browser.get(('https://accounts.google.com/ServiceLogin?'
             'service=mail&continue=https://mail.google'
             '.com/mail/#identifier'))
             
# Searching for username input field by 'id' and filling it with the desired text
# Then we're searching for the 'next' button

# The send_keys() and click() commands do exactly as their names suggest — send_keys() simulates keypresses in the desired element, and click() simulates a mouse click.

# fill in username and hit the next button

username = browser.find_element_by_id('Email')
username.send_keys(usernameStr)
nextButton = browser.find_element_by_id('next')
nextButton.click()


# We simply have to instruct the browser to wait a maximum of 10 seconds before locating the password entry.
# Wait for transistion then continue to fill items

password = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.ID, 'Passwd')))
password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('signIn')
signInButton.click()







