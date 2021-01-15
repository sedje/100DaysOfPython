from selenium import webdriver
from time import sleep
CHROMEDRIVER = "chromedriver/chromedriver"


class SpeedBot:
    def __init__(self):
        self.down = 0
        self.up = 0
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER, options=options)

    def get_speed(self, timeout=180):
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