from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from buttons import Web_site_interactions
import variables as var

class Profile_fetch:
    def __init__(self, driver):
        self.driver = driver
        self.web_site_interactions = Web_site_interactions(self.driver)
        self.actions = ActionChains(self.driver)
    def go_to_followers(self):
        self.web_site_interactions.open_website(var.INSTAGRAM+var.USERNAME+"/followers/")
    def go_to_following(self):
        self.web_site_interactions.open_website(var.INSTAGRAM + var.USERNAME + "/following/")
    def DFS_finding_link(self, web_el):
        tab = self.web_site_interactions.get_child_elements(web_el)
        for i in range(len(tab)):
            if tab[i].tag_name == "a":
                return tab[i]
            else:
                wynik = self.DFS_finding_link(tab[i])
                if wynik!=False:
                    if wynik.tag_name == "a":
                        return wynik
        return False

    def get_following_links(self):
        linki = []
        a_elements = []
        self.web_site_interactions.wait(3)
        self.web_site_interactions.find_a_by_text("Obserwowani: ")
        self.web_site_interactions.click()
        self.web_site_interactions.wait(5)

        self.web_site_interactions.find_div_by_classname("_acbs")
        self.web_site_interactions.get_parent_elemets()

        child_el = self.web_site_interactions.get_child_elements()
        obserwowani = child_el[3]
        self.web_site_interactions.element = obserwowani
        child_el = self.web_site_interactions.get_child_elements()
        self.web_site_interactions.element = child_el[0]
        child_el = self.web_site_interactions.get_child_elements()
        self.web_site_interactions.element = child_el[0]
        child_el = self.web_site_interactions.get_child_elements()

        rodzic_obserwujących = self.web_site_interactions.element

        for n in range(len(child_el)):
            a_elements.append(self.DFS_finding_link(child_el[n]))
            linki.append(self.web_site_interactions.get_href_from_a(self.DFS_finding_link(child_el[n])))

        previous_child_el = child_el
        a_elements[0].send_keys(Keys.END)
        time.sleep(5)
        child_el = self.web_site_interactions.get_child_elements(rodzic_obserwujących)

        while len(previous_child_el) != len(child_el):
            previous_child_el = child_el
            a_elements[0].send_keys(Keys.END)
            time.sleep(5)
            child_el = self.web_site_interactions.get_child_elements(rodzic_obserwujących)

        for n in range(len(linki), len(child_el)):
            a_elements.append(self.DFS_finding_link(child_el[n]))
            linki.append(self.web_site_interactions.get_href_from_a(self.DFS_finding_link(child_el[n])))

        print(len(linki))
        print("x")
        return linki

    def get_followers_links(self):
        linki = []
        a_elements = []
        self.web_site_interactions.wait(3)
        self.web_site_interactions.find_a_by_text(" obserwujących")
        self.web_site_interactions.click()
        self.web_site_interactions.wait(5)

        self.web_site_interactions.find_div_by_classname("_ac76")
        self.web_site_interactions.get_parent_elemets()
        self.web_site_interactions.get_parent_elemets()

        child_el = self.web_site_interactions.get_child_elements()
        obserwujacy = child_el[2]
        self.web_site_interactions.element = obserwujacy
        child_el = self.web_site_interactions.get_child_elements()
        self.web_site_interactions.element = child_el[0]
        child_el = self.web_site_interactions.get_child_elements()
        self.web_site_interactions.element = child_el[0]
        child_el = self.web_site_interactions.get_child_elements()

        rodzic_obserwujących = self.web_site_interactions.element

        for n in range(len(child_el)):
            a_elements.append(self.DFS_finding_link(child_el[n]))
            linki.append(self.web_site_interactions.get_href_from_a(self.DFS_finding_link(child_el[n])))

        previous_child_el = child_el
        a_elements[0].send_keys(Keys.END)
        time.sleep(5)
        child_el = self.web_site_interactions.get_child_elements(rodzic_obserwujących)

        while len(previous_child_el) != len(child_el):
            previous_child_el = child_el
            a_elements[0].send_keys(Keys.END)
            time.sleep(5)
            child_el = self.web_site_interactions.get_child_elements(rodzic_obserwujących)

        for n in range(len(linki), len(child_el)):
            a_elements.append(self.DFS_finding_link(child_el[n]))
            linki.append(self.web_site_interactions.get_href_from_a(self.DFS_finding_link(child_el[n])))

        print(len(linki))
        print("x")
        return linki