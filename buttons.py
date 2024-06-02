from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from waiting import Waiting

class Web_site_interactions:
    def __init__(self, driver):
        self.driver = driver
        self.element = None
        self.waiter = Waiting(self.driver)
    def open_website(self, nazwa):
        self.driver.get(nazwa)


    def find_button_by_text(self, tekst):
        przyciski = self.driver.find_element(By.XPATH, f'//button[text()="{tekst}"]')
        self.element = przyciski
    def wait_for_button_by_text(self,tekst):
        self.waiting1(By.XPATH, f'//button[text()="{tekst}"]')
    def find_div_by_text(self, tekst):
        div = self.driver.find_element(By.XPATH, f'//div[text()="{tekst}"]')
        self.element = div
    def wait_for_div_by_text(self,tekst):
        self.waiting2(By.XPATH, f'//div[text()="{tekst}"]')
    def find_button_by_classname(self, name_):
        przyciski = self.driver.find_element(By.CLASS_NAME, name_)
        self.element = przyciski
    def find_div_by_classname(self, name):
        div = self.driver.find_element(By.CLASS_NAME, name)
        self.element = div
    def find_span_by_text(self, tekst):
        span = self.driver.find_element(By.XPATH, f'//span[text()="{tekst}"]')
        self.element = span
    def find_a_by_text(self, tekst):
        a = self.driver.find_element(By.XPATH, f'//a[text()="{tekst}"]')
        self.element = a
    def find_css_selector(self, tekst):
        css_selector = self.driver.find_element(By.XPATH, f'//css_selector[text()="{tekst}"]')
        self.element = css_selector
    def get_href_from_a(self, element):
        href = element.get_attribute('href')
        return href

    def get_child_elements(self, element=None):
        if element is None:
            return self.element.find_elements(By.XPATH, "./child::*")
        else:
            return element.find_elements(By.XPATH, "./child::*")
    def get_parent_elemets(self):
        self.element =  self.element.find_element(By.XPATH, "./..")
    

    def click(self):
        self.element.click()
    def input_by_text(self, tekst):
        wpisywanie = self.driver.find_element(By.XPATH, f'//input[@aria-label="{tekst}"]')
        self.element = wpisywanie
    def send_text(self, tekst ):
        self.element.send_keys(tekst)


    def wait(self,sec):
        time.sleep(sec)
    def waiting1(self, method,nazwa):
        self.waiter.set_nazwa(nazwa)
        self.waiter.set_method(method)
        self.waiter.element_is_present()
    def waiting2(self, method,nazwa):
        self.waiter.set_nazwa(nazwa)
        self.waiter.set_method(method)
        self.waiter.element_is_clickable()



