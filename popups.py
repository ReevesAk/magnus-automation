from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

def popups():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("http://magnus.jalaacademy.com/Account/Login")
    driver.find_element_by_id("UserName").send_keys("training@jalaacademy.com")
    driver.find_element_by_id("Password").send_keys("jobprogram")
    driver.find_element_by_id("btnLogin").click()
    driver.get("http://magnus.jalaacademy.com/Home/Index")
    driver.find_element_by_link_text("More").click()
    driver.get("http://magnus.jalaacademy.com/Home/Popup")

    # Capture alert message and get the text on the alrt box.
    driver.find_element_by_xpath("//input[@id='alertBox']").click()
    alert = Alert(driver)
    print(alert.text)
    alert.accept()

    time.sleep(2)

    # Enter a string in the prompt aler box and print the 
    # entered text in the terminal.
    driver.find_element_by_xpath("//button[@id='promptBtn']").click()
    prompt_alert = driver.switch_to.alert
    prompt_alert.send_keys("Reeves Akwa")
    prompt_alert.accept()
    text = driver.find_element_by_id("promptBox")
    print(text.text)
    time.sleep(2)

    # Click the cancel button of the alert box.
    driver.find_element_by_xpath("//input[@id='confirmBox']").click()
    cancel_prompt = driver.switch_to.alert
    cancel_prompt.dismiss()
    time.sleep(2)

    # Switch to fram using switch_to to navigate to 
    # a frame on the page.
    driver.get("http://magnus.jalaacademy.com/Home/Iframe")
    driver.find_element_by_xpath("//span[@class='logo-lg font_20']//b[contains(text(),'Magnus')]")
    driver.switch_to.frame("iframe2")
    text_in_frame = driver.find_element_by_xpath("//h1[normalize-space()='Welcome to Magnus']")
    print(text_in_frame.text)
    time.sleep(2)

    # Switch to popup using switch_to alert.
    driver.get("http://magnus.jalaacademy.com/Home/Popup")
    driver.find_element_by_xpath("//a[@id='btn-two']").click()
    driver.switch_to_window
    time.sleep(2)


    driver.close()
    driver.quit()


popups()    