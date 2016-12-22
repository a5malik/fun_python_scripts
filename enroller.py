# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 00:20:50 2016

@author: footb

Automatically scans and enrolls you in classes at UCLA
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass
from selenium.webdriver.common.action_chains import ActionChains
import win32api, win32con
from bs4 import BeautifulSoup
import urllib2
import re


print "Please download & install chromedriver from https://sites.google.com/a/chromium.org/chromedriver/downloads"
print "After that, continue...:"

chromedriver_path = raw_input("Enter full Chromedriver.exe path(for eg C:\\Users\\footb\\Downloads\\chromedriver_win32\\chromedriver.exe): ")
username = raw_input('Enter MyUCLA username: ')
password = getpass.getpass('Enter Password: ')
quarter = raw_input('Enter quarter(W/F/S): ').upper()
year = raw_input('Enter year(last 2 digits) (16/17 etc): ')
mins = float(raw_input('Enter interval (in mins) for classes to be checked again. (eg 15): '))

full_year = 2000 + int(year)

class_list = raw_input("Enter space seperated list of class IDs FOR SPECIFIC DISCUSSION(NOT LECTURE)): ").split()

class_ids = {} #to be tried or not
for id in class_list:
    class_ids[id] = True


while(True):   
    for id in class_ids.keys():
        if class_ids[id] == False:
            continue
        url="https://sa.ucla.edu/ro/Public/SOC/Results?t={}{}&sBy=classidnumber&id={}&btnIsInIndex=btn_inIndex".format(year, quarter, id)
        content = urllib2.urlopen(url).read()
        soup = BeautifulSoup(content, 'html.parser')
        status = soup.find_all("div", class_="statusColumn")[1].get_text()
        
        if re.match(r'.*Open.*', status) == None:
            print "{}: {} is closed".format(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()), id)
            continue
        else:
            print "{}: {} is open, now enrolling".format(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()), id)
            class_ids[id] = False
        
        browser = webdriver.Chrome(chromedriver_path)                
        browser.get("https://my.ucla.edu/")
        
        browser.find_element_by_link_text('Sign In').click()
        
        time.sleep(1.5)
        
        browser.find_element_by_id("logon").send_keys(username, Keys.TAB)
        browser.find_element_by_id("pass").send_keys(password)
        
        browser.find_element_by_css_selector("button.primary-button").click()
        
        #win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
        #time.sleep(0.1)
        #win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)
        
        
        time.sleep(1.7)
        browser.find_element_by_partial_link_text('Enrollment Home').click()
        time.sleep(1)
        browser.find_element_by_partial_link_text('Find a Class and Enroll').click()
        time.sleep(1)
        browser.find_element_by_xpath("//select[@id='optSelectTerm']/optgroup[@label='{}']/option[@value='{}{}']".format(full_year, year, quarter) ).click()
        time.sleep(1.5)
        browser.find_element_by_xpath("//select[@id='search_by']/option[@value='classidnumber']").click()
        time.sleep(2.5)
        
        
        browser.find_element_by_id("ClassID").send_keys(id)
        time.sleep(1.6)
        browser.find_element_by_id("btn_go").click()
        #win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
        #time.sleep(0.1)
        #win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)
        
        time.sleep(2)
        results = browser.find_element_by_css_selector("div.results")
        all_cb = results.find_elements_by_tag_name("input")
        for cb in all_cb:
            cb.click()
        time.sleep(3)
        warning = browser.find_element_by_css_selector("div.warning_panel")
        all_warning_cb = warning.find_elements_by_tag_name("input")
        for cb in all_warning_cb:
            cb.click()
        time.sleep(2)
        
        option = browser.find_element_by_css_selector("div.info_panel")
        option.find_element_by_id("btn_Enroll").click()
        
        #enrol.find_element_by_tag_name('input').click()
    time.sleep(mins*60)