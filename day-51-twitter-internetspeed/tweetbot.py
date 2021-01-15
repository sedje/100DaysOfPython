from dotenv import load_dotenv
# from selenium import webdriver
import twitter
import os

# CHROMEDRIVER = "chromedriver/chromedriver"


class TweetBot:
    """Simple bot for tweeting out messages using headless selenium webdriver

    Methods
    -------
    send_tweet(message)
        sends a tweet using twitter
    """

    def __init__(self):
        load_dotenv(".env")
        # self.username = os.getenv("TWITTER-EMAIL")
        # self.password = os.getenv("TWITTER-PASSWORD")
        self.apikey = os.getenv("API-KEY")
        self.api_secret = os.getenv("API-SECRET")
        self.access_token = os.getenv("ACCESS-TOKEN")
        self.access_token_secret = os.getenv("ACCESS-TOKEN-SECRET")

        self.__authenticate()

        # options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        # self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER, options=options)

    # def __login(self):
    #     """Private Login function for accessing a twitter account, requires credentials to be set in a .env file"""
    #
    #     self.driver.get(f"https://twitter.com/login?username_or_email={self.username}")
    #     pw_field = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
    #                                                  '2]/form/div/div[2]/label/div/div[2]/div/input')
    #     pw_field.send_keys(self.password)
    #
    #     login_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
    #                                                   '2]/form/div/div[3]/div')
    #     login_btn.click()
    #
    # def get_tweet(self, tweet_id):
    #     header = {"Authorization": f"Bearer {self.bearer}"}
    #     print(requests.get(f"https://api.twitter.com/2/tweets/{tweet_id}", headers=header).text)

    def __authenticate(self):
        """Private authentication function for accessing a twitter account"""
        self.api = twitter.Api(consumer_key=self.apikey,
                               consumer_secret=self.api_secret,
                               access_token_key=self.access_token,
                               access_token_secret=self.access_token_secret)

    def send_tweet(self, message):
        """function for sending tweets, includes a check to see if tweets are longer than 140 characters

        Parameters
        ----------
        message : str
            The message to be tweeted
        """

        if len(message) > 140:
            print("Message too long")
            return False
        else:
            self.api.PostUpdate(message)
            # # First call private login function to get authorized
            # self.__login()
            # tweet_box = self.driver.find_element_by_xpath(
            #     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div['
            #     '1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div['
            #     '2]/div/div/div/div')
            # tweet_box.send_keys(message)
            # tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div['
            #                                                  '2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div['
            #                                                  '1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
            # tweet_button.click()
            # self.driver.quit()
