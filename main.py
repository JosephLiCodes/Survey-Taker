# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import selenium
import time
import email
import os
import smtplib
from email.message import EmailMessage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
accs = 'email:temp'
username = accs.split(':')[0]
password = accs.split(':',1)[1]
def doSurvey():
    driver = webdriver.Firefox()
    driver.get("https://studenthealthoc.sa.ucsb.edu/login_dualauthentication.aspx")
    #find the login for stduents button
    try:
        student_login = driver.find_element_by_id('cmdStudentDualAuthentication')
        student_login.click()
    except NoSuchElementException:
        print("student login button not found!")
    #now log in using username and password
    try:
        username_box = driver.find_element_by_id('txtUsername')
        username_box.send_keys(username)
    except NoSuchElementException:
        print("Username box not found!")
    try:
        password_box = driver.find_element_by_id('txtPassWord')
        password_box.send_keys(password)
        password_box.send_keys(Keys.ENTER)
    except NoSuchElementException:
        print("Password box not found!")
    #logged in now we need to do the survey
    time.sleep(1)
    try:
        survey_button = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/div[3]/div/a')
        survey_button.click()
    except NoSuchElementException:
        print("Survey Button not found!")
    time.sleep(1)
    try:
        continue_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/a')
        continue_button.click()
    except NoSuchElementException:
        print("Continue Button not found!")
    time.sleep(1)
    #now we are on the survey page I could change the html from 'answer button p-3' to 'answer button p-3 active'to say no as well
    q1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/main/form/div[2]/fieldset/div/div[2]/div')
    q1.click()
    q2 = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/main/form/div[3]/fieldset/div/div[2]/div')
    q2.click()
    q3 = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/main/form/div[4]/fieldset/div/div[2]/div')
    q3.click()
    q4 = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/main/form/div[5]/fieldset/div/div[2]/div')
    q4.click()
    q5 = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/main/form/div[6]/fieldset/div/div[2]/div')
    q5.click()
    #all answers selected. now its time to submit
    try:
        submit = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/footer/div/div[2]/input')
        submit.click()
    except NoSuchElementException:
        print("submit button not found!")
    #survey done
    try:
        badge = driver.find_element_by_xpath('//*[@id="showQuarantineBadge"]')
        badge.click()
    except NoSuchElementException:
        print("Button not found!")
    driver.close()
doSurvey()
