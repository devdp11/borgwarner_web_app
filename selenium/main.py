from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://127.0.0.1:5000/")
driver.maximize_window()

def login():
    element = driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-info btn-lg"]')
    element.click()

    username_element = driver.find_element(By.CSS_SELECTOR, 'input[id="username"]')
    username_element.send_keys('root')

    password_element = driver.find_element(By.CSS_SELECTOR, 'input[id="password"]')
    password_element.send_keys('root')

    sign_element = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    sign_element.click()

    timesleep(2)
    quiz()

def quiz():
    element = driver.find_element(By.CSS_SELECTOR, 'a[class="nav-link collapsed"]')
    element.click()

    timesleep(2)

    element = driver.find_element(By.CSS_SELECTOR, 'a[href="/questionario_tecnicomanutencao"]')
    element.click()

    timesleep(2)

    number_member_element = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Número Técnico"]')
    number_member_element.send_keys('28244')

    timesleep(1)

    select_element = driver.find_element(By.CSS_SELECTOR, 'select[id="pl"]')
    select = Select(select_element)
    select.select_by_value('o')

    timesleep(2)

    check_element_1 = driver.find_element(By.CSS_SELECTOR, 'input[name="check[]"]')
    check_element_1.click()

    check_element_2 = driver.find_element(By.CSS_SELECTOR, 'input[name="check2[]"]')
    check_element_2.click()

    timesleep(2)
    
    check_element_3 = driver.find_element(By.CSS_SELECTOR, 'input[name="check4[]"]')
    check_element_3.click()

    check_element_4 = driver.find_element(By.CSS_SELECTOR, 'input[name="check6[]"]')
    check_element_4.click()

    timesleep(2)

    check_element_5 = driver.find_element(By.CSS_SELECTOR, 'input[name="check8[]"]')
    check_element_5.click()

    check_element_6 = driver.find_element(By.CSS_SELECTOR, 'input[name="check10[]"]')
    check_element_6.click()

    timesleep(2)

    check_element_7 = driver.find_element(By.CSS_SELECTOR, 'input[name="check12[]"]')
    check_element_7.click()

    check_element_8 = driver.find_element(By.CSS_SELECTOR, 'input[name="check14[]"]')
    check_element_8.click()

    check_element_9 = driver.find_element(By.CSS_SELECTOR, 'input[name="check19[]"]')
    check_element_9.click()

    timesleep(2)

    submit_element = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
    submit_element.click()

    closebot()

def timesleep(args):
    time.sleep(args)

def closebot():
    time.sleep(10)
    driver.quit()

login()