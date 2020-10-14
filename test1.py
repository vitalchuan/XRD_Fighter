# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 09:58:46 2020

@author: 何奇川
"""
from time import sleep
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

code = pytesseract.image_to_string(sharp_img).replace(" ", "")
print(code)

input = browser.find_element_by_xpath('//*[@id="captcha"]')
input.send_keys(code)
#button = browser.find_element_by_xpath('//*[@id="submit-button"]')
#button.click()

browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr[1]/td[2]/div/strong/a').click(); # XRD
browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/div/div/div[4]/div/span/span/span/a[2]').click() # 使用预约
#browser.implicitly_wait(30)
sleep(2)
browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/div/div/div[5]/table[2]/thead/tr[1]/td/div/div[1]/a[2]').click() # 下一周

sleep(2)
action = ActionChains(browser)

#下滑到底部
browser.execute_script('window.scrollTo(0,1000)')

#移动鼠标
action.move_to_element(browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/div/div/div[5]/table[2]/tbody[3]/tr[38]/td[5]'))
sleep(1)

action.double_click(browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/div/div/div[5]/table[2]/tbody[2]/tr/td[2]/div/div[2]'))
/html/body/div[2]