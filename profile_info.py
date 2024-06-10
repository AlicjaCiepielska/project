from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from buttons import Web_site_interactions
import variables as var


class Saving_data:
    def __init__(self, driver):
        self.driver = driver
    def saving_info(self,name,data):
        with open(name+".txt", "w") as name:
            for n in range(len(data)):
                name.write(f"{data[n]}\n")
