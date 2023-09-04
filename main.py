import requests
import random

from selenium_profiles.webdriver import Chrome
from selenium_profiles.profiles import profiles
from selenium.webdriver.common.by import By  # locate elements
from seleniumwire import webdriver

#   ... add more 
addrList = [
  '0xDc4fDADD37F2CD35027E7b542467a2C136A4F51a',
  '0x95683d23aa38A1dC5f51b91635ac7e62C436Ee50',
]

#   ... add more or not use
def getHeaders():
    UAList = [ "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54"]
    return UAList[random.randrange(0, len(UAList))]

def writelog(filename, log):
    file = open(filename, "a")
    file.write(log + "\n")
    file.close()

for addr in addrList:
    profile = profiles.Windows()  # or .Android
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = Chrome(profile, options=options, uc_driver=False)
    driver.implicitly_wait(99)
    # get url
    driver.get('https://zapper.xyz/zh/account/' + addr)  # test fingerprintgbh
    res = driver.find_element(By.CSS_SELECTOR, "[class='items_center gap_sm d_flex']")
    print(addr + " " + res.text)
    driver.quit()
