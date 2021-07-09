from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_mpspecific():
    x = 0 
    y = 0
    p = "kaist"
    q = "kaist computer science"

    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys(p)
    elem.send_keys(Keys.RETURN)

    # read the number of returned pages
    stats = driver.find_element_by_id("result-stats")
    tokens = stats.text.split(" ")
    x = int(tokens[2][:-1].replace(",", ""))

    driver.get("https://www.google.com")

    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys(q)
    elem.send_keys(Keys.RETURN)

    # read the number of returned pages
    stats = driver.find_element_by_id("result-stats")
    tokens = stats.text.split(" ")
    y = int(tokens[2][:-1].replace(",", ""))
    driver.close()

    assert x >= y

if __name__ == '__main__':
    test_mpspecific()