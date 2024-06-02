from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Waiting:
    def __init__(self,driver):
        self.driver = driver
        self.method = None
        self.nazwa = None
    def set_method(self, method):
        self.method = method
    def set_nazwa(self,nazwa):
        self.nazwa = nazwa
    def element_is_present(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((self.method,self.nazwa)))
    def element_is_clickable(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((self.method,self.nazwa)))

