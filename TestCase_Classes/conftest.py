import pytest
from selenium import webdriver

from Utility.readProperties import ReadConfig


@pytest.fixture()
def browser():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(ReadConfig.appCreds("AppCredential","siteurl"))
    driver.implicitly_wait(5)
    yield driver #yield is used to return a value temporarily and then resume the function later from the same place.
    #return driver
    driver.quit()
