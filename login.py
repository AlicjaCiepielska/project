from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from buttons import Web_site_interactions
import variables as var

class logowanie:
    def __init__(self, log, has, driver):
        self.login = log
        self.haslo = has
        self.driver = driver
    def logowanie(self):

        web_site_interactions = Web_site_interactions(self.driver)
        web_site_interactions.open_website(var.INSTAGRAM)

        web_site_interactions.wait_for_button_by_text(var.PLIKI_COOKIES)
        web_site_interactions.find_button_by_text(var.PLIKI_COOKIES)
        web_site_interactions.click()

        web_site_interactions.wait_for_div_by_text(var.ZALOG)

        web_site_interactions.input_by_text(var.LOGIN_POLE)
        web_site_interactions.send_text(self.login)

        web_site_interactions.input_by_text(var.HASLO_POLE)
        web_site_interactions.send_text(self.haslo)

        web_site_interactions.find_div_by_text(var.ZALOG)
        web_site_interactions.click()
    def dalsze_dzialanie(self):
        web_site_interactions = Web_site_interactions(self.driver)
        web_site_interactions.wait_for_div_by_text(var.NIE_TERAZ)
        web_site_interactions.find_div_by_text(var.NIE_TERAZ)
        web_site_interactions.click()

        web_site_interactions.wait_for_button_by_text(var.NIE_TERAZ)
        web_site_interactions.find_button_by_text(var.NIE_TERAZ)
        web_site_interactions.click()

        link = var.INSTAGRAM + var.USERNAME + "/"
        web_site_interactions.open_website(link)



