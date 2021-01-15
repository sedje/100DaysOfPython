from selenium import webdriver
from time import sleep
CHROMEDRIVER = "chromedriver/chromedriver"


class SpeedBot:
    """Simple bot for getting the current internet speed from speedtest.net

        Attributes
        ----------
        timeout : int, optional
        An optional timeout value for getting the internet speed. If not set, timeout default is 180

        Methods
        -------
        get_speed(timeout=180)
            Uses a headless selenium instance to get the current internet speed
    """

    def __init__(self):
        self.down = 0
        self.up = 0
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER, options=options)

    def get_speed(self, timeout=180):
        """Gets the current up and download speed and returns it as a dictionary.

           Parameters
           ----------
           timeout : int, optional
                The amount of time to wait for results
        """

        self.driver.get("https://www.speedtest.net/run")
        cookie = self.driver.find_element_by_xpath('// *[ @ id = "_evidon-banner-acceptbutton"]')
        cookie.click()
        sleep(timeout)
        self.down = float(self.driver.find_element_by_css_selector('.download-speed').text)
        self.up = float(self.driver.find_element_by_css_selector('.upload-speed').text)
        print(self.driver.find_element_by_css_selector('.download-speed').text)
        print(self.driver.find_element_by_css_selector('.upload-speed').text)
        self.driver.close()
        return {'up': self.up, 'down': self.down}