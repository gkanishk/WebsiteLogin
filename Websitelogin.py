# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


usernameStr = 'uid'
passwordStr = 'password'

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(('https://uims.cuchd.in/uims/'))

# fill in username and hit the next button

username = browser.find_element_by_id('txtUserId')
username.send_keys(usernameStr)

nextButton = browser.find_element_by_id('btnNext')
nextButton.click()

# wait for transition then continue to fill items

password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, "txtLoginPassword")))

password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('btnLogin')
signInButton.click()