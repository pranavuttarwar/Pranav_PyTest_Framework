import pytest
from selenium.webdriver.common.by import By


class hometotalitems:
    #global variable
    totalinventory = "//div[@class='inventory_item_description']"

    #initalize constructor for initalize driver
    def __init__(self, driver):
        self.driver = driver

    #perform
    def totalItems(self):
        values=self.driver.find_elements(By.XPATH, self.totalinventory)
        return len(values)

