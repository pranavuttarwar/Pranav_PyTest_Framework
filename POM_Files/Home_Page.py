from selenium.webdriver.common.by import By


class HomePage:
    #global Locators
    Header="//div[@class='app_logo']"

    #initalize constructor for webdrive
    def __init__(self, driver):
        self.driver = driver

    #perform
    def title(self):
        actualTitle=self.driver.find_element(By.XPATH, self.Header).text
        return actualTitle