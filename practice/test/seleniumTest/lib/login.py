# coding:UTF-8 -*-

from selenium import webdriver
import time
import sys
sys.path.append("..")
from config.config import *

browser = webdriver.Chrome()
browser.get(url_chaos)
user_name = browser.find_element_by_id("user")
user_name.send_keys("")
time.sleep(1)
user_passwd = browser.find_element_by_id("pwd")
user_passwd.send_keys("")
time.sleep(1)
code_input = browser.find_element_by_id("code-input")
code_input.send_keys("")
time.sleep(1)
login_button = browser.find_element_by_id("submit").click()
time.sleep(1)
login_again = browser.find_element_by_id("submit").click()
time.sleep(1)
ops_mang = browser.find_element_by_css_selector('a[href="/show_ops_manage"]').click()
