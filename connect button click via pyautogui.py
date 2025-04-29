from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from selenium import webdriver




service= Service(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.set_window_position(0, 0)
options.add_argument("window-size=1020,580")


driver.get('https://www.linkedin.com/login')
time.sleep(2)

uf=driver.find_element(By.CSS_SELECTOR,'#username')
pf=driver.find_element(By.CSS_SELECTOR,'#password')

uf.send_keys('@gmail.com')
pf.send_keys('.')

lb=driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
lb.click()
time.sleep(5)

profile_url = "https://www.linkedin.com/in/deep-makadiya-4ab258222/"
driver.get(profile_url)
time.sleep(3)

safest way
pyautogui.moveTo(127, 587)  # Change this to the pixel coordinates you want
pyautogui.click()
time.sleep(5)

pyautogui.moveTo(690, 684)  # Change this to the pixel coordinates you want
pyautogui.click()
driver.quit()