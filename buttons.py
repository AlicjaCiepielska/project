from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

class Web_site_interactions:
    def __init__(self, driver):
        self.driver = driver
        self.element = None
    def open_website(self, nazwa):
        self.driver.get(nazwa)
    def find_button_by_text(self, tekst):
        przyciski = self.driver.find_element(By.XPATH, f'//button[text()="{tekst}"]')
        self.element = przyciski
    def click(self):
        self.element.click()
    def input_by_text(self, tekst):
        wpisywanie = self.driver.find_element(By.XPATH, f'//input[@aria-label="{tekst}"]')
        self.element = wpisywanie
    def send_text(self, tekst ):
        self.element.send_keys(tekst)
    def wait(self,sec):
        time.sleep(sec)

