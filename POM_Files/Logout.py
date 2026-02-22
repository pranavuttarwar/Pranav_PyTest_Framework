from selenium.webdriver.common.by import By


class Logout:
    hamburger="//button[@id='react-burger-menu-btn']"
    urlLogout="//a[@id='logout_sidebar_link']"
    home="//div[@id='login_credentials']"

    def __init__(self, driver):
        self.driver = driver

    def hamb(self):
        self.driver.find_element(By.XPATH, self.hamburger).click()

    def urllogout(self):
        self.driver.find_element(By.XPATH, self.urlLogout).click()

    def loginHome(self):
        ActualText=self.driver.find_element(By.XPATH, self.home).text
        return ActualText