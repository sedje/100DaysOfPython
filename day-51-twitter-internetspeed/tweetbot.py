from dotenv import load_dotenv
from selenium import webdriver
import os
from time import sleep
CHROMEDRIVER = "chromedriver/chromedriver"


class TweetBot:
    def __init__(self):
        load_dotenv(".env")
        self.username = os.getenv("TWITTER-EMAIL")
        self.password = os.getenv("TWITTER-PASSWORD")
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER, options=options)

    def login(self):
        self.driver.get(f"https://twitter.com/login?username_or_email={self.username}")
        pw_field = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
                                                     '2]/form/div/div[2]/label/div/div[2]/div/input')
        pw_field.send_keys(self.password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
                                                      '2]/form/div/div[3]/div')
        login_btn.click()

    def send_tweet(self, message):

        if len(message) > 140:
            print("Message too long")
            return False
        else:
            self.login()
            tweet_box = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div['
                '1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div['
                '2]/div/div/div/div')
            tweet_box.send_keys(message)
            tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div['
                                                             '2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div['
                                                             '1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
            tweet_button.click()
            self.driver.quit()
