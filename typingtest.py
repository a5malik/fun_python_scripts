# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 13:01:16 2016

@author: footb

Reads and enters text on the typing test page.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

import time

browser = webdriver.Chrome("C:\\Users\\footb\\Downloads\\chromedriver_win32\\chromedriver.exe")
browser.get("http://typing-speed-test.aoeu.eu/")
time.sleep(2)
inp = browser.find_element_by_id("input")
cur = browser.find_element_by_class_name("currentword").text

start_time = time.time()
while(time.time()-start_time <= 60):
    inp.send_keys(cur)
    inp.send_keys(Keys.SPACE)
    cur = browser.find_element_by_class_name("currentword").text
