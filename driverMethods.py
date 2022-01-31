from selenium import webdriver
import time


def driver_methods():
    driver = webdriver.Chrome()
    driver.get("http://magnus.jalaacademy.com/Account/Login")
    print(driver.current_url)
    print(driver.title)
    if "Magnus" in driver.page_source:
        print("Page source contains: Magnus")
    else:
        print("You are visiting an unknown page")
    elements = driver.find_elements_by_class_name("form-control")
    print(elements)
    window = driver.current_window_handle
    print(window)
    driver.find_element_by_id("UserName").send_keys("training@jalaacademy.com")
    driver.find_element_by_id("Password").send_keys("jobprogram")
    driver.find_element_by_id("btnLogin").click()
    driver.find_element_by_class_name("text-white").click()
    size = driver.get_window_size
    print(size)
    lcoation = driver.get_window_position
    print(lcoation)
    window_handles = driver.window_handles
    print(window_handles)
    time.sleep(2)
    window_switch = driver.window_handles[0]
    driver.switch_to.window(window_switch)
    driver.back()
    driver.forward()
    driver.close()
    driver.quit()


driver_methods()
