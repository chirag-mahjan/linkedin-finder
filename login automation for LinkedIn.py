from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service= Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)

driver.get('https://www.linkedin.com/login')
time.sleep(2)

uf=driver.find_element(By.CSS_SELECTOR,'#username')
pf=driver.find_element(By.CSS_SELECTOR,'#password')

uf.send_keys('mahajanchirag2385@gmail.com')
pf.send_keys('chirag.1415')

lb=driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
lb.click()
time.sleep(5)
input()

driver.quit()
