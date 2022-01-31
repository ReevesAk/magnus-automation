import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


class ActionClass:

    def keyboard_key_press(self):
        driver = webdriver.Firefox()
        driver.get("http://magnus.jalaacademy.com/Account/Login")
        driver.find_element_by_id("UserName").send_keys("training@jalaacademy.com")
        driver.find_element_by_id("Password").send_keys("jobprogram")
        driver.find_element_by_id("btnLogin").send_keys(Keys.ENTER)

    def press_and_hold(self):
        driver = webdriver.Chrome()
        driver.get("http://magnus.jalaacademy.com/Account/Login")
        driver.find_element_by_id("UserName").send_keys("training@jalaacademy.com")
        driver.find_element_by_id("Password").send_keys("jobprogram")
        driver.find_element_by_id("btnLogin")
        action = ActionChains(driver)
        time.sleep(5)
        action.perform()

    def drag_and_drop(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://magnus.jalaacademy.com/Account/Login")
        driver.find_element_by_id("UserName").send_keys("training@jalaacademy.com")
        driver.find_element_by_id("Password").send_keys("jobprogram")
        driver.find_element_by_id("btnLogin").click()
        driver.get("http://magnus.jalaacademy.com/Home/Index")
        driver.find_element_by_link_text("More").click()
        driver.get("http://magnus.jalaacademy.com/Home/AutoComplete")
        source = driver.find_element_by_xpath("//a[normalize-space()='Autocomplete']")
        target = driver.find_element_by_id("txtSingleAutoComplete")
        actions = ActionChains(driver)
        actions.drag_and_drop(source, target).perform()

        # Delay the screen until mouse is directed to target.
        time.sleep(5)

    def move_to_element(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://magnus.jalaacademy.com/Account/Login")
        button = driver.find_element_by_xpath("//a[@class='btn btn-block btn-facebook btn-flat text-center']")
        action = ActionChains(driver)
        action.move_to_element(button).click().perform()
        time.sleep(3)

    def mouse_hover_event(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://magnus.jalaacademy.com/Account/Login")
        driver.find_element_by_id("UserName").send_keys("training@jalaacademy.com")
        driver.find_element_by_id("Password").send_keys("jobprogram")
        parent = driver.find_element_by_id("btnLogin").click()
        driver.get("http://magnus.jalaacademy.com/Home/Index")
        driver.find_element_by_link_text("More").click()
        driver.get("http://magnus.jalaacademy.com/Home/Tooltip")
        parent_element = driver.find_elements_by_xpath("//button[@id='btnTooltip']")

        # Magnus does not have a parent menu to perform
        #  mouse hover action.
        hover = ActionChains(driver).move_to_element(parent_element)
        hover.perform()
        print(hover.text)
        time.sleep(2)

    def double_click(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://magnus.jalaacademy.com/Account/Login")
        driver.find_element_by_id("UserName").send_keys("training@jalaacademy.com")
        driver.find_element_by_id("Password").send_keys("jobprogram")
        source = driver.find_elements_by_xpath("//button[@id='btnLogin']")

        # Magnus does not have an element to perform
        # mouse double click action.
        action = ActionChains(driver)
        action.double_click(source).perform()

    def get_row_count(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://magnus.jalaacademy.com/Account/Login")
        driver.find_element_by_id("UserName").send_keys("training@jalaacademy.com")
        driver.find_element_by_id("Password").send_keys("jobprogram")
        driver.find_element_by_id("btnLogin").click()
        driver.get("http://magnus.jalaacademy.com/Home/Index")
        driver.find_element_by_link_text("Employee").click()
        driver.get("http://magnus.jalaacademy.com/Employee/Search")
        driver.refresh()
        rows = len(driver.find_elements_by_tag_name("tr"))
        print(rows)
        time.sleep(3)

    def get_specific_item(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://magnus.jalaacademy.com/Account/Login")
        driver.find_element_by_id("UserName").send_keys("training@jalaacademy.com")
        driver.find_element_by_id("Password").send_keys("jobprogram")
        driver.find_element_by_id("btnLogin").click()
        driver.get("http://magnus.jalaacademy.com/Home/Index")
        driver.find_element_by_link_text("Employee").click()
        driver.get("http://magnus.jalaacademy.com/Employee/Search")
        driver.refresh()
        find_element = driver.find_elements_by_xpath("//*[@id='tblEmployee']/tbody/tr[1]")
        print(find_element)

    def get_cookie(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://magnus.jalaacademy.com/Account/Login")
        driver.find_element_by_id("UserName").send_keys("training@jalaacademy.com")
        driver.find_element_by_id("Password").send_keys("jobprogram")
        driver.add_cookie({'name': 'email', 'value': "training@jalaacademy.com"})
        cookie = driver.get_cookie("email")
        driver.find_element_by_id("btnLogin").click()
        print(cookie)
        deleted_cookie = driver.delete_cookie("email")
        print(deleted_cookie)
        time.sleep(5)

    def create_and_access_profile(self):
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=C:/home/akwa/.config/google-chrome/Profile 2")
        driver = webdriver.Chrome(options=options)
        driver.get("http://magnus.jalaacademy.com/Account/Login")
        time.sleep(10)


action = ActionClass()
action.create_and_access_profile()
