from selenium import webdriver as wd
from time import sleep
from threading import Thread
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Number of opening Clients
NUM = 2

# Browser driver path
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

option = wd.ChromeOptions()
option.binary_location = brave_path
dservice = Service("chromedriver.exe")


def buy():
    # Creation of an instance of the browser (Brave)
    browser = wd.Chrome(service=dservice, options=option)

    # Product page connection and purchase
    browser.get(link)

    if browser.find_element(By.XPATH, '//*[@id="sp-cc-accept"]'):
        button = browser.find_element(By.XPATH, '//*[@id="sp-cc-accept"]')
        button.click()

    button = browser.find_element(By.XPATH, '//*[@id="buy-now-button"]')
    button.click()

    # Amazon Login if not logged
    if browser.find_element(By.XPATH, '//*[@id="ap_email"]'):
        login = browser.find_element(By.XPATH, '//*[@id="ap_email"]')
        login.send_keys(email)
        passw = browser.find_element(By.XPATH, '//*[@id="ap_password"]')
        passw.send_keys(psw)
        passw.submit()

    button = browser.find_element(By.XPATH, '//*[@id="submitOrderButtonId"]')
    # button.click() - Click to buy

    sleep(0.5)
    browser.close()

# Link and credentials definition
file = open('cred.txt')
link = file.readline()
email = file.readline()
psw = file.readline()
file.close()

# (Main) Thread start
for i in range(NUM):
    t = Thread(target=buy)
    t.start()
