from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from waiting import Waiting

class Findbuttons:
    def __init__(self, driver):
        self.driver = driver
        self.element = None
        self.waiter = Waiting(self.driver)

    def find_button_by_text(self, tekst):
        przyciski = self.driver.find_element(By.XPATH, f'//button[text()="{tekst}"]')
        self.element = przyciski

    def find_div_by_text(self, tekst):
        div = self.driver.find_element(By.XPATH, f'//div[text()="{tekst}"]')
        self.element = div

    def find_button_by_classname(self, name_):
        przyciski = self.driver.find_element(By.CLASS_NAME,name_)

    def find_span_by_text(self, tekst):
        span = self.driver.find_element(By.XPATH, f'//span[text()="{tekst}"]')
        self.element = span

    def find_href(self, href):
        href = self.driver.find_element(By.LINK_TEXT,f'{href}')
        self.element = href