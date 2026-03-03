import pytest
from selenium import webdriver

from Utility.readProperties import ReadConfig



def openApp(driver):
    driver.maximize_window()
    driver.get(ReadConfig.appCreds("AppCredential","siteurl"))
    driver.implicitly_wait(5)
    #yield driver #yield is used to return a value temporarily and then resume the function later from the same place.
    #return driver
    #driver.quit()

@pytest.fixture
def inibrowser(browser):
        if browser=="edge":
            driver = webdriver.Edge()
            openApp(driver)
            return driver
        elif browser=="firefox":
            driver = webdriver.Firefox()
            openApp(driver)
            return driver
        elif browser=="chrome":
            driver = webdriver.Chrome()
            openApp(driver)
            return driver

#Set deafult browser

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="edge")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")




