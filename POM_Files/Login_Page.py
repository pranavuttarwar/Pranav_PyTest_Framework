from selenium.webdriver.common.by import By


class SwagLogin:

    #Global locators for each web element on the web page.
    Username= "//input[@id='user-name']" #Only Xpath access anywhere by using self.
    Password= "//input[@id='password']" #Only Xpath access anywhere by using self.
    BtLogin= "//input[@id='login-button']" #Only Xpath access anywhere by using self.
    Error="//h3[@data-test='error']" #Only xpath access anywhere by using self.

    #Initalize the constructor for to call web driver.
    def __init__(self, driver): #driver local variable
        self.driver = driver  #convert local variable into class variable

    #Perform Action by creating method for each web page element

    #Valid Username
    def uname(self,un):
        self.driver.find_element(By.XPATH, self.Username).send_keys(un)

    #Valid Password
    def pwd(self,pw):
        self.driver.find_element(By.XPATH, self.Password).send_keys(pw)

    #Click on the login button
    def clkbtn(self):
        self.driver.find_element(By.XPATH, self.BtLogin).click()

    #Invalid login error text
    def err(self):
        error= self.driver.find_element(By.XPATH, self.Error).text
        return error




