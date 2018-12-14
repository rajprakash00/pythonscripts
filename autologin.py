#scripting for automatic login of gmail

#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr ='Email-id'
passwordStr ='password'

browse = webdriver.Chrome()
browse =webdriver.Chrome("/usr/local/lib/python2.7/dist-packages/selenium/webdriver")
browse.get(('https://account.google.com/ServiceLogin?'
	     'service=mail&continue=https://mail.google'
	     '.com/mail/#identifier'))

username = browse.find_element_by_id('email-id')
username.send_keys(usernameStr)
nextButton = browse.find_element_by_id('next')
nextButton.click()

password = WebDriverWait(browse, 10).until(EC.presence_of_element_located((By.ID, 'password')))
password.send_keys(passwordStr)
 
signInButton = browse.find_element_by_id('signIn')
signInButton.click()
