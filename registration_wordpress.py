#!!/usr/bin/env python 

from selenium import *
import getpass
from selenium.webdriver.common.keys import *
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import firebug_proxy
import time
import webbrowser



def logout(driver):      
    driver.get("http://wordpress.com/wp-login.php?action=logout&redirect_to=http%3A%2F%2Fwordpress.com")
                     #logout 


def post(driver,email,password,title,string,tag):
    post_url = "http://wordpress.com/post/"
    driver.get(post_url)
    driver.find_element_by_id("ipt-form-format-aside").click()
    elem  = driver.find_element_by_name("ipt_aside_title")
    elem.send_keys(title)
    elem.send_keys(Keys.TAB,string)
    elem  = driver.find_element_by_name("ipt_tags")
    elem.send_keys(tag)
    driver.find_element_by_name("publish").click()
                     #posting

def login(driver,email,password,title,string,tag):
    login_url = "http://en.wordpress.com/wp-login.php?redirect_to=http%3A%2F%2Fen.wordpress.com%2F"
    driver.get(login_url)
    elem = driver.find_element_by_name("log")
    elem.send_keys(email)
    elem = driver.find_element_by_name("pwd")
    elem.send_keys(password)
    driver.find_element_by_name("wp-submit").click()
                     #Login

def registration(email,password,title,string,tag):
    try:
        url = "https://signup.wordpress.com/signup/"
        html , driver = firebug_proxy.main(url)
        elem = driver.find_element_by_name("user_email")
        elem.send_keys(email)
        elem = driver.find_element_by_name("pass1")
        elem.send_keys(password)
        elem = driver.find_element_by_name("user_name")
        start = email.find("@")
        user_name =email[:start]
        elem.send_keys(user_name)  
        driver.find_element_by_name("Submit").click()
                      #registration

        #verification_code()
                      #verification    
    except:
        pass

    login(driver,email,password,title,string,tag)
                      #login

    post(driver,email,password,title,string,tag)
                      #posting
    logout(driver)
                      #logout 
    driver.close()


if __name__=="__main__":
    email="xxxx@hotmail.com"
    password="xxxx"
    title="creativity"
    string="creativity cant be defined it can just be done only "
    tag="creativity"
    
    registration(email,password,title,string,tag)



