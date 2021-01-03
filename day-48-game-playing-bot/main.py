import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv

CHDRIV = "chromedriver/chromedriver"


def questions(driver):
    # Challenge to get the price tag off an amazon page using selenium.
    driver = driver
    driver.get("https://www.amazon.nl/Lenovo-Chromebook-Laptop-touchscreen-Celeron/dp/B0845FYQ9B/ref=sr_1_2?dchild=1"
               "&pf_rd_i=16366027031&pf_rd_m=AC5DXSR5G8JPX&pf_rd_p=7ef6398f-4b6f-4808-9d0b-49c040302cb5&pf_rd_r"
               "=P224E7VNBRYP1HPDX2X9&pf_rd_s=merchandised-search-3&pf_rd_t=101&qid=1609678584&refinements"
               "=p_n_feature_nineteen_browse-bin%3A16365374031&s=electronics&sr=1-2")

    # Find elements by ID
    price = driver.find_element_by_id("priceblock_ourprice").text
    print(price)

    # Find elements by xpath
    price_xpath = driver.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text
    print(price_xpath)


def challenge1(driver):
    # Challenge to create a dictionary from the python events page element
    driver = driver
    driver.get("https://www.python.org")
    event_times = driver.find_elements_by_css_selector(".event-widget time")
    event_names = driver.find_elements_by_css_selector(".event-widget li a")
    events = {}
    for n in range(len(event_times)):
        events[n] = {
            "time": event_times[n].text,
            "name": event_names[n].text,
        }

    print(events)


def challenge2(driver):
    # Challenge to find the page count in wikipedia, done by xpath
    driver = driver
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
    count = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]').text
    print(count)


def click_links(driver):
    # Challenge to get the all portals link by its link tag and click it.
    # Second step was to fill the search field and search for the word python
    driver = driver
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
    portals = driver.find_element_by_link_text("All portals")
    portals.click()
    search = driver.find_element_by_name("search")
    search.send_keys("python")
    search.send_keys(Keys.ENTER)


def challenge3(driver):
    # Challenge to fill all fields with values and submit the form
    driver = driver
    driver.get("http://secure-retreat-92358.herokuapp.com/")
    first_name = driver.find_element_by_name("fName")
    first_name.send_keys("Anko")
    last_name = driver.find_element_by_name("lName")
    last_name.send_keys("testing")
    email = driver.find_element_by_name("email")
    email.send_keys("anko@testing.app")
    email.send_keys(Keys.ENTER)


def game(driver):
    driver = driver
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    cookie = driver.find_element_by_id("bigCookie")
    timeout = time.time() + 1
    five_min = time.time() + 60 * 5  # 5minutes
    while True:
        cookie.click()
        if time.time() > timeout:
            # Check for upgrades
            upgrades = driver.find_elements_by_id("upgrade0")
            if upgrades:
                upgrades[-1].click()

            # Check for enabled buttons
            prices = driver.find_elements_by_css_selector(".enabled .content .price")
            if prices:
                price_list = []
                for price in prices:
                    price_list.append(price.text)

                product_button = f"product{price_list.index(prices[-1].text)}"
                purchase = driver.find_element_by_id(product_button)
                purchase.click()

            timeout = time.time() + 1
            if time.time() > five_min:
                cookie_per_s = driver.find_element_by_id("cookies").text
                print(cookie_per_s)
                break


def main():
    # Options to run a headless browser
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(executable_path=CHDRIV, options=options)

    questions(driver)
    challenge1(driver)
    challenge2(driver)
    click_links(driver)
    challenge3(driver)
    game(driver)

    # driver.close() => closes active tab
    # driver.close()
    # driver.quit() => quits entire chrome browser
    driver.quit()


if __name__ == '__main__':
    main()

