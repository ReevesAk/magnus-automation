from selenium import webdriver
import os


def test_screenshot():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://magnus.jalaacademy.com/Account/Login")
    driver.find_element_by_id("UserName").send_keys("training@jalaacademy.com")
    driver.find_element_by_id("Password").send_keys("jobprogram")
    driver.find_element_by_id("btnLogin").click()
    driver.save_screenshot("magnus.png")
    os.path.exists("magnus.png")
    assert "Login" == driver.title


test_screenshot()
