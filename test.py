from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument('--incognito')
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=chromedriver)

driver.get('https://webvpn.zju.edu.cn/')
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="Calc"]/div[1]/div[1]/div/div[1]/input').send_keys('3190105607')
driver.find_element(By.XPATH, '//*[@id="loginPwd"]').send_keys('cnh112358')
driver.find_element(By.XPATH, '//*[@id="Calc"]/div[3]/button').click()

time.sleep(1)
driver.get('http://www-nexushd-org.webvpn.zju.edu.cn:8001/login.php')

driver.find_element(By.NAME, 'username').send_keys('爆裂')
driver.find_element(By.NAME, 'password').send_keys('cnh112358')
driver.find_element(By.XPATH, "//*[@id='nav_block']/form[2]/table/tbody/tr[7]/td/button[1]").click()

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="shbox_text"]').send_keys('test1')
driver.find_element(By.XPATH, '//*[@id="hbsubmit"]').click()
