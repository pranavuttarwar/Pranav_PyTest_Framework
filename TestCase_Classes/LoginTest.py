import time

from selenium import webdriver

from POM_Files.Home_Page import HomePage
from POM_Files.Home_Total_Items import hometotalitems
from POM_Files.Login_Page import SwagLogin
from POM_Files.Logout import Logout
from Utility.CustomLogger import logGen
from Utility.readProperties import ReadConfig
from Utility.screenshotUtility import screenshotUtility


class TestLogin:
    logger=logGen().loggen()
    def test_TC1_Valid_Login(self, inibrowser):
        driver = inibrowser
        sl=SwagLogin(driver)
        sl.uname(ReadConfig.appCreds("AppCredential","username"))
        self.logger.info("Valid Username added")
        sl.pwd(ReadConfig.appCreds("AppCredential","password"))
        self.logger.info("Valid Password added")
        sl.clkbtn()
        self.logger.info("Clicked on Login button after credentials.")

        time.sleep(5)

        hp=HomePage(driver)
        actualText=hp.title()
        print("**Actual Title: ",actualText)
        expectedText="Swag Labs"
        print("**Expected Title: ",expectedText)

        if actualText == expectedText:
            assert True
        else:
            screenshotUtility.captureSS(driver,"test_TC1_Valid_Login")
            assert False


    def test_TC2_Invalid_Login(self, inibrowser,request):
        driver = inibrowser

        sl=SwagLogin(driver)
        sl.uname(ReadConfig.appCreds("InvalAppCredential","username"))
        sl.pwd(ReadConfig.appCreds("InvalAppCredential","password"))
        sl.clkbtn()
        ActualErrorMsg=sl.err()
        print("**Actual Error: ",ActualErrorMsg)
        expectedErrorMsg="Epic sadface: Username and password do not match any user in this service"
        print("**Expected Error: ",expectedErrorMsg)

        if ActualErrorMsg == expectedErrorMsg:
            assert True
            self.logger.info("Error message correct on login for invalid username and password.")
        else:
            #approch1
            #screenshotUtility.captureSS(driver, "test_TC2_Valid_Login")
            #approch2- to get test case automatically.
            screenshotUtility.captureSS(driver, request.node.name)
            assert False

    def test_TC3_Hometotalitem(self, inibrowser):
        driver = inibrowser
        sl = SwagLogin(driver)
        sl.uname(ReadConfig.appCreds("AppCredential", "username"))
        self.logger.info("Valid Username added")
        sl.pwd(ReadConfig.appCreds("AppCredential", "password"))
        self.logger.info("Valid Password added")
        sl.clkbtn()
        self.logger.info("Clicked on Login button after credentials.")
        time.sleep(5)
        hpi=hometotalitems(driver)
        actualItemValue=hpi.totalItems()
        print("**Actual Item: ",actualItemValue)
        expectedItemValue=6
        print("**Expected Item: ", expectedItemValue)

        if actualItemValue == expectedItemValue:
            assert True
            self.logger.info("Expected item value and actual item values are same.")
        else:
            assert False



    def test_TC4_Logout(self, inibrowser):   #Logout Test Case
        driver = inibrowser

        sl = SwagLogin(driver)
        sl.uname(ReadConfig.appCreds("AppCredential", "username"))
        self.logger.info("Valid Username added")
        sl.pwd(ReadConfig.appCreds("AppCredential", "password"))
        self.logger.info("Valid Password added")
        sl.clkbtn()
        self.logger.info("Clicked on Login button after credentials.")
        time.sleep(5)

        Lo=Logout(driver)
        Lo.hamb()
        Lo.urllogout()
        Hometext=Lo.loginHome()
        print("**Hometext: ",Hometext)
        self.logger.info("Logout successful")


