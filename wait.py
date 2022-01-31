from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def wait():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get("http://magnus.jalaacademy.com/Account/Login")
    driver.find_element_by_id("UserName").send_keys("training@jalaacademy.com")
    driver.find_element_by_id("Password").send_keys("jobprogram")
    delayed_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"btnLogin"))
        )
    delayed_element.click()


wait()   