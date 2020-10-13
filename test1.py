# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 09:58:46 2020

@author: 何奇川
"""
import time
import pytesseract
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from PIL import Image,ImageEnhance

account = 'castle'
password = 'castle010566'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://202.120.49.55/lims/')
button = browser.find_element_by_xpath('//*[@id="sidebar"]/div/div/div[2]/div[2]/div')
button.click()
input = browser.find_element_by_xpath('//*[@id="user"]')
input.send_keys(account)
input = browser.find_element_by_xpath('//*[@id="pass"]')
input.send_keys(password)

browser.save_screenshot('printscreen.png')
imgelement = browser.find_element_by_xpath('//*[@id="captcha-img"]')
location = imgelement.location  # 获取验证码x,y轴坐标
size = imgelement.size  # 获取验证码的长宽
rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
          int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
i = Image.open("printscreen.png")  # 打开截图
vertification_code_img = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
vertification_code_img.save('vertification_code_img.png') # 保存我们接下来的验证码图片 进行打码

sharp_img = ImageEnhance.Contrast(vertification_code_img).enhance(2.0)
sharp_img.save("sharpImg.png")

code = pytesseract.image_to_string(sharp_img).strip()
print(code)

input = browser.find_element_by_xpath('//*[@id="captcha"]')
input.send_keys(code)
button = browser.find_element_by_xpath('//*[@id="submit-button"]')
button.click()

browser.find_element_by_xpath('//*[@id="table_equipments_follow_equipments"]/tbody/tr[1]/td[2]/div/strong/a').click(); # XRD
browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/div/div/div[4]/div/span/span/span/a[2]').click() # 使用预约
Thread.sleep(1000)
js ="document.getElementById('calendar_right_nav_5f85c3d6689fa').children[1].click()"  # js点击元素
browser.execute_script(js)
#implicitly_wait(500)
#browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/div/div/div[5]/table[2]/thead/tr[1]/td/div/div[1]/a[2]').click() # 下一周


