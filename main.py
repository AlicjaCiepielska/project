from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.get("https://www.youtube.com/watch?v=NB8OceGZGjA&ab_channel=TechWithTim")
time.sleep(10)
driver.quit()