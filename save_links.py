from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from buttons import Web_site_interactions
import variables as var
from profile_featch import Profile_fetch

class Saving_links:
    def __init__(self, driver):
        self.driver = driver
        self.web_site_interactions = Web_site_interactions(self.driver)
        self.actions = ActionChains(self.driver)
    def 