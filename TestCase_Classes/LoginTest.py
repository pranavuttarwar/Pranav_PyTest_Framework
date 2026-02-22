import time

from selenium import webdriver

from POM_Files.Home_Page import HomePage
from POM_Files.Login_Page import SwagLogin
from POM_Files.Logout import Logout


class TestLogin:
    def test_TC1_Valid_Login(self):
        driver = webdriver.Edge()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        driver.implicitly_wait(5)

        sl=SwagLogin(driver)
        sl.uname("standard_user")
        sl.pwd("secret_sauce")
        sl.clkbtn()
        time.sleep(5)

        hp=HomePage(driver)
        actualText=hp.title()
        print("**Actual Title: ",actualText)
        expectedText="Swag Labs"
        print("**Expected Title: ",expectedText)

        if actualText == expectedText:
            assert True
        else:
            assert False

    def test_TC2_Invalid_Login(self):
        driver = webdriver.Edge()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        driver.implicitly_wait(5)

        sl=SwagLogin(driver)
        sl.uname("Pranav")
        sl.pwd("Uttarwar")
        sl.clkbtn()
        ActualErrorMsg=sl.err()
        print("**Actual Error: ",ActualErrorMsg)
        expectedErrorMsg="Epic sadface: Username and password do not match any user in this service"
        print("**Expected Error: ",expectedErrorMsg)

        if ActualErrorMsg == expectedErrorMsg:
            assert True
        else:
            assert False

    def test_TC3_Logout(self):   #Logout Test Case
        driver = webdriver.Edge()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        driver.implicitly_wait(5)

        sl = SwagLogin(driver)
        sl.uname("standard_user")
        sl.pwd("secret_sauce")
        sl.clkbtn()
        time.sleep(5)

        Lo=Logout(driver)
        Lo.hamb()
        Lo.urllogout()
        Hometext=Lo.loginHome()
        print("**Hometext: ",Hometext)


