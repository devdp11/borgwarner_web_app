from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://127.0.0.1:5000/")
driver.maximize_window()

element = driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-info btn-lg"]')
element.click()

username_element = driver.find_element(By.CSS_SELECTOR, 'input[id="username"]')
username_element.send_keys('root')

password_element = driver.find_element(By.CSS_SELECTOR, 'input[id="password"]')
password_element.send_keys('root')

sign_element = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
sign_element.click()

time.sleep(10)
driver.quit()