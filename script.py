from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
import os
import time
import sys

class AutoSign():
  def __init__(self, webvpn_username, webvpn_password, nhd_username, nhd_password, sckey):
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
    self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=chromedriver)
    
    self.webvpn_username = webvpn_username
    self.webvpn_password = webvpn_password
    self.nhd_username = nhd_username
    self.nhd_password = nhd_password
    self.sckey = sckey
    
    self.cnt = 0;
    
    self.content = ''
  
  def run(self):
    self.webvpn_login()
    for i in range(len(self.nhd_username)):
      self.nhd_login(self.nhd_username[i], self.nhd_password[i])
      self.nhd_signin(self.nhd_username[i])
  
  def webvpn_login(self):
    self.driver.get('https://webvpn.zju.edu.cn/')
    time.sleep(5)
    try:
      self.driver.find_element(By.XPATH, '//*[@id="Calc"]/div[1]/div[1]/div/div[1]/input').send_keys(self.webvpn_username)
      self.driver.find_element(By.XPATH, '//*[@id="loginPwd"]').send_keys(self.webvpn_password)
      self.driver.find_element(By.XPATH, '//*[@id="Calc"]/div[3]/button').click()
      print("webvpn???????????????")
    except:
      print("webvpn???????????????")
      if self.sckey:
        title = u'ERROR!'
        content = 'webvpn???????????????'
        data = {'text': title, 'desp': content}
        requests.post(f'http://sc.ftqq.com/{self.sckey}.send', data)
      
  def nhd_login(self, username, password):
    time.sleep(1)
    self.driver.get('http://www-nexushd-org.webvpn.zju.edu.cn:8001/login.php')

    try:
      self.driver.find_element(By.NAME, 'username').send_keys(username)
      self.driver.find_element(By.NAME, 'password').send_keys(password)
      self.driver.find_element(By.XPATH, "//*[@id='nav_block']/form[2]/table/tbody/tr[7]/td/button[1]").click()
      print("NHD???????????????")
    except:
      print("NHD???????????????")
      if self.sckey:
        title = u'ERROR!'
        self.content += username + ' NHD???????????????\n'
        data = {'text': title, 'desp': self.content}
        self.cnt += 1
        if self.cnt == len(self.nhd_username):
          requests.post(f'http://sc.ftqq.com/{self.sckey}.send', data)
      
  def nhd_signin(self, username):
    time.sleep(1)
    
    try:
      self.driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr[1]/td/table[2]/tbody/tr/td/table/tbody/tr/td[2]/span/a[2]').click()
      self.driver.find_element(By.NAME, 'content').send_keys('test')
      self.driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr/td/table[2]/tbody/tr/td/div/table/tbody/tr/td/form/input[2]').click()
      print(username + "????????????")
      if self.sckey:
        title = u'SUCCESS!'
        self.content += username + ' ???????????????\n'
        data = {'text': title, 'desp': self.content}
        self.cnt += 1
        if self.cnt == len(self.nhd_username):
          requests.post(f'http://sc.ftqq.com/{self.sckey}.send', data)
    except:
      print(username + "???????????????")
      if self.sckey:
        title = u'SUCCESS!'
        self.content += username + ' ??????????????????\n'
        data = {'text': title, 'desp': self.content}
        self.cnt += 1
        if self.cnt == len(self.nhd_username):
          requests.post(f'http://sc.ftqq.com/{self.sckey}.send', data)
      
    self.driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr[1]/td/table[2]/tbody/tr/td/table/tbody/tr/td[1]/span/a[1]').click()

def split(str):
  res = str.split('!')
  return res
  
if __name__ == "__main__":
  webvpn_username = sys.argv[1]
  webvpn_password = sys.argv[2]
  nhd_username = sys.argv[3]
  nhd_password = sys.argv[4]
  sckey = sys.argv[5]
  
  nhd_username = split(nhd_username)
  nhd_password = split(nhd_password)
  
  signer = AutoSign(webvpn_username, webvpn_password, nhd_username, nhd_password, sckey)
  signer.run()
