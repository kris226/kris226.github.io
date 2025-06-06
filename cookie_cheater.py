from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

servis = Service("kris226.github.io\chromedriver.exe")
driver = webdriver.Chrome(service = servis)

driver.get("https://Kris226.github.io")

# https://googlechromelabs.github.io/chrome-for-testing/
# pip install selenium

cookie_button = driver.find_element(By.ID,"clicker")
upgrade_button = driver.find_element(By.ID,"upgrador")

for i in range (100000):
    cookie_button.click()
    upgrade_button.click()








while True:
    ...