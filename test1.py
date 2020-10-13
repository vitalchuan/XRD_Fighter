# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 09:58:46 2020

@author: 何奇川
"""

from selenium import webdriver

account = 'castle'
password = 'castle010566'
browser = webdriver.Chrome();
browser.get('http://202.120.49.55/lims/')
button = browser.find_element_by_xpath('//*[@id="sidebar"]/div/div/div[2]/div[2]/div')
button.click();
input = browser.find_element_by_xpath('//*[@id="user"]')
input.send_keys(account)
input = browser.find_element_by_xpath('//*[@id="pass"]')
input.send_keys(password)
