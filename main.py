from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class Vreme:
    def __init__(self, grad):
        self.driver=webdriver.Chrome()
        self.driver.get(
            "https://google.com")

        sleep(0.5)

        boruto = "vreme " + grad

        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input").send_keys(boruto)

        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div[2]/form/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]").submit()

naruto=Vreme("Nis")