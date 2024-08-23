from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from os import getcwd
import requests
from tkinter import *
import os
from network.offline import check_internet,show_offline_gui


if not check_internet():
        show_offline_gui()
else:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    website = f"{getcwd()}//Recognisation//voice.html"
    driver.get(website)




def Listen():
    driver.get(website)
    driver.find_element(by=By.ID, value='start').click()
    while 1:
        text = driver.find_element(by=By.ID, value='output').text
        if text != "":
            driver.find_element(by=By.ID, value='end').click()
            return text

if __name__ == "__main__":
    if not check_internet():
        show_offline_gui()
    else:
        while 1:
            Listen()
            
         