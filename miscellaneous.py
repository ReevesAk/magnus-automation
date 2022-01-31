import requests
from selenium import webdriver


def miscellaneous():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://magnus.jalaacademy.com/Account/Login")
    driver.find_element_by_id("UserName").send_keys("training@jalaacademy.com")
    driver.find_element_by_id("Password").send_keys("jobprogram")
    driver.find_element_by_id("btnLogin").click()
    driver.get("http://magnus.jalaacademy.com/Home/Index")
    driver.find_element_by_xpath("//a[normalize-space()='More']")
    driver.get("http://magnus.jalaacademy.com/Home/Iframe")
    driver.find_element_by_xpath("//span[@class='logo-lg font_20']//b[contains(text(),'Magnus')]").click()
    driver.get("http://magnus.jalaacademy.com/Home/Iframe")

    # Find out broken links on a webpage.
    driver.get("http://magnus.jalaacademy.com/Home/Links")
    driver.find_element_by_xpath("//a[normalize-space()='Broken Links']").click()
    links = driver.find_elements_by_tag_name("a")
    for broken_links in links:
        retrieve = broken_links.get_attribute('href')
        request = requests.get(retrieve)
        # if request.status_code == 200:
        print(broken_links)


miscellaneous()
