from datetime import datetime


class screenshotUtility:
    @staticmethod
    def captureSS(driver,test_name):
        #current date and time
        crrnt_time=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        #screenshot file name
        screenshot_path= f".\\Screenshots\\{test_name}_{crrnt_time}.png"

        driver.save_screenshot(screenshot_path)


