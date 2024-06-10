from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import variables as var
from login import logowanie
from profile_featch import Profile_fetch
from buttons import Web_site_interactions
from profile_info import Saving_data

service = Service(executable_path=var.CHROME)
driver = webdriver.Chrome(service = service)


logowanie_ = logowanie(var.LOGIN,var.HASLO, driver)
logowanie_.logowanie()
logowanie_.dalsze_dzialanie()
profile_fetch = Profile_fetch(driver)
profile_fetch.get_following_links()

web_site_interactions = Web_site_interactions(driver)
link = var.INSTAGRAM + var.USERNAME + "/"
web_site_interactions.open_website(link)

profile_fetch.get_followers_links()

time.sleep(1000)

driver.quit()