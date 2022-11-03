# -*- coding: utf-8 -*-
# python 3.8.10
#pip install selenium,pandas,requests

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import chrome_helper
from time import sleep

def check_mail():
    person=pd.read_excel(r'file/111年教補問卷名單.xlsx')

    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    try:
        driver= webdriver.Chrome(r'file/chrome/chromedriver.exe',chrome_options=options) #Chrome
    except:
        os.remove(r'file\chrome\mapping.json')
        chrome_helper.check_browser_driver_available() #Chrome版本自動選擇參考，https://medium.com/drunk-wis/python-selenium-chrome-browser-%E8%88%87-driver-%E6%83%B1%E4%BA%BA%E7%9A%84%E7%89%88%E6%9C%AC%E7%AE%A1%E7%90%86-cbaf1d1861ce
        driver= webdriver.Chrome(r'file/chrome/chromedriver.exe',chrome_options=options) #Chrome
    i=0
    while i<len(person):
        driver.get("https://pec.mohw.gov.tw/MONITOR_INDICATOR/Monitor_Questionnaire.aspx")
        driver.find_element('name',"txtIDNO").send_keys(person.iloc[i,1])
        driver.find_element('name',"txtName").send_keys(person.iloc[i,0])
        driver.find_element('name',"txtEmail").send_keys(person.iloc[i,2])
        driver.find_element('name',"btnTrySend").click()

        driver.switch_to.alert.accept()
        i+=1

def re_send_mail():
    person=pd.read_excel(r'file/111年教補問卷名單.xlsx')

    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    try:
        driver= webdriver.Chrome(r'file/chrome/chromedriver.exe',chrome_options=options) #Chrome
    except:
        os.remove(r'file\chrome\mapping.json')
        chrome_helper.check_browser_driver_available() #Chrome版本自動選擇參考，https://medium.com/drunk-wis/python-selenium-chrome-browser-%E8%88%87-driver-%E6%83%B1%E4%BA%BA%E7%9A%84%E7%89%88%E6%9C%AC%E7%AE%A1%E7%90%86-cbaf1d1861ce
        driver= webdriver.Chrome(r'file/chrome/chromedriver.exe',chrome_options=options) #Chrome
    i=0
    while i<len(person):
        driver.get("https://pec.mohw.gov.tw/MONITOR_INDICATOR/Monitor_Questionnaire.aspx")
        driver.find_element('name',"txtIDNO").send_keys(person.iloc[i,1])
        driver.find_element('name',"txtName").send_keys(person.iloc[i,0])
        driver.find_element('name',"txtEmail").send_keys(person.iloc[i,2])
        driver.find_element('name',"btnSendSN").click()
        driver.switch_to.alert.accept()
        i+=1
        
re_send_mail()