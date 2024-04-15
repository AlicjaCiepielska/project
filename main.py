from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import variables as var
from login import logowanie


service = Service(executable_path=var.CHROME)
driver = webdriver.Chrome(service = service)

logowanie_ = logowanie(var.login,var.haslo, driver)
logowanie_.logowanie()

driver.quit()