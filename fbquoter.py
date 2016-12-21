# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 20:44:09 2016

@author: footb

logs into fb and randomly messages fight club quotes from IMDB.(or any IMDB quotes url)

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains
import time

from bs4 import BeautifulSoup
import urllib2
import re
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', dest='name', default="Steven Yin")

args = parser.parse_args()

myemail = ""
mypass = ""

url="http://www.imdb.com/title/tt0137523/quotes"
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content, 'html.parser')
quotes = soup.find_all("div", class_="quote")

browser = webdriver.Chrome("C:\\Users\\footb\\Downloads\\chromedriver_win32\\chromedriver.exe")

browser.get("http://www.facebook.com")

email = browser.find_element_by_id("email");
email.send_keys(myemail, Keys.TAB)

password = browser.find_element_by_id("pass")
password.send_keys(mypass, Keys.RETURN)

name = browser.find_element_by_partial_link_text(args.name)
url = name.get_attribute("href")

#actions = ActionChains(browser)
#actions.move_to_element(name).context_click(name).perform()
#actions.send_keys(Keys.ARROW_DOWN).perform()
#actions.send_keys(Keys.RETURN).perform()
#name.click()
#time.sleep(5)

#browser.find_element_by_class_name("_1mf").send_keys("hey")
browser.get(url)
for i in range(1):
    quote = random.choice(quotes)
    browser.find_element_by_id("js_n").send_keys("Random IMDB Fight club quote by Python script", Keys.RETURN)
    browser.find_element_by_id("js_n").send_keys(quote.contents[0].contents[1].contents[1].string, Keys.RETURN)
    browser.find_element_by_id("js_n").send_keys(quote.contents[0].contents[1].contents[2][2:], Keys.RETURN)
    browser.find_element_by_id("js_n").send_keys("XXXX", Keys.RETURN)


