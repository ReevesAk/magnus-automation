from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


class WebElements:
    @staticmethod
    def test_setup():
        driver = webdriver.Chrome("/usr/bin/google-chrome")
        driver.implicitly_wait(20)
        driver.maximize_window()
        driver.get("http://magnus.jalaacademy.com/Account/Login")
        driver.find_element_by_id("UserName").send_keys("training@jalaacademy.com")
        driver.find_element_by_id("Password").send_keys("jobprogram")
        driver.find_element_by_class_name("checkmark").click()
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_class_name("text-white").click()

    @staticmethod
    def auto_textbox():
        driver = webdriver.Chrome()
        driver.get("http://magnus.jalaacademy.com/Account/Login")
        driver.find_element_by_id("UserName").send_keys("training@jalaacademy.com")
        driver.find_element_by_id("Password").send_keys("jobprogram")
        driver.find_element_by_class_name("checkmark").click()
        driver.find_element_by_id("btnLogin").click()
        driver.get("http://magnus.jalaacademy.com/Home/Index")
        driver.find_element_by_link_text("More").click()
        driver.find_element_by_link_text("Autocomplete")
        driver.find_element_by_link_text("Autocomplete").get_attribute("type")
        driver.get("http://magnus.jalaacademy.com/Home/AutoComplete")
        driver.find_element_by_id("txtSingleAutoComplete").send_keys("This is selenium automating")
        driver.find_element_by_id("txtSingleAutoComplete").clear()
        driver.find_element_by_id("txtSingleAutoComplete").is_enabled()
        driver.find_element_by_id("txtSingleAutoComplete").get_property("value")
        driver.find_element_by_id("txtSingleAutoComplete").get_attribute("value")

    @staticmethod
    def auto_radio_button():
        driver = webdriver.Chrome()
        driver.get("http://magnus.jalaacademy.com/Account/Login")

        # check all elements of radio button group.
        number = driver.find_element_by_id("RememberMe").click()
        print(number)
        driver.find_element_by_id("RememberMe").is_enabled()
        driver.find_element_by_id("RememberMe").is_selected()

    @staticmethod
    def auto_dropdown():
        driver = webdriver.Chrome()
        driver.get("http://magnus.jalaacademy.com/Account/Login")
        driver.find_element_by_id("UserName").send_keys("training@jalaacademy.com")
        driver.find_element_by_id("Password").send_keys("jobprogram")
        driver.find_element_by_id("btnLogin").click()
        driver.get("http://magnus.jalaacademy.com/Home/Index")
        Ulist = driver.find_element_by_link_text("More")
        options = [x for x in Ulist.find_elements_by_tag_name("option")]
        for element in options:
            print(element.get_attribute("value"))

            # select first item in dropdown
        options = driver.find_element_by_link_text("More")
        select = Select(options)
        select.select_by_index(0)
        select.select_by_value("value")
        select.select_by_visible_text("Visible-text")
        print(select.first_selected_option.text)

    @staticmethod
    def automate_link():
        driver = webdriver.Chrome()
        driver.implicitly_wait(20)
        driver.maximize_window()
        driver.get("http://magnus.jalaacademy.com/Account/Login")
        driver.find_element_by_partial_link_text("Forgot Password").click()
        links = []
        links = driver.find_element_by_xpath('//*[@href]')
        for link in links:
            print(link.get_attribute('href'))
        try:
            driver.find_element_by_partial_link_text("Forgot").click()
            print("Partial link text was found")
        except Exception as e:
            print("Exception:", format(e))
        # Click on a image link.    
        driver.find_element_by_css_selector("input[src='path to img.png'][type='image']").click()

    @staticmethod
    def automate_xpath():
        driver = webdriver.Chrome()
        driver.implicitly_wait(20)
        driver.maximize_window()
        driver.get("http://magnus.jalaacademy.com/Account/Login")
        get_text = driver.find_element_by_xpath("//button[@id='btnLogin']").text
        print(get_text)
        # Xpath for ID.
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[3]/input")
        # Xpath for name.
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[2]/input")
        # Xpath for className.
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[4]/div[1]/label")
        driver.find_element_by_id("UserName").send_keys("training@jalaacademy.com")
        driver.find_element_by_id("Password").send_keys("jobprogram")
        driver.find_element_by_id("btnLogin").click()
        try:
            start = driver.find_element_by_xpath("//*[starts-with(text(), 'JALA')]")
            print("YEEEAAAAAAHHH!")
            print(start.text)
        except Exception as e:
            print(e)
        try:
            contain = driver.find_element_by_xpath("//*[contains(text(), 'JALA Technologies')]")
            print("I was found!")
            print(contain.text)
        except Exception as e:
            print(e)
        content = driver.find_element_by_xpath("/html/body/div[2]/footer/strong/a")
        col = driver.find_element_by_xpath("/html/body/div[2]/footer/strong/a").value_of_css_property(
            'background-color')
        print(content.text)
        print(col)
        driver.get("http://magnus.jalaacademy.com/Home/Index")
        driver.find_element_by_xpath("//a[normalize-space()='More']")
        driver.get("http://magnus.jalaacademy.com/Home/CssProperty")
        driver.find_element_by_xpath("//a[normalize-space()='Buttons']").click()
        parent = driver.find_element_by_xpath("//button[normalize-space()='Success']")
        check = parent.find_element_by_xpath("..")
        print(check.text)
        print("I am the parent class: ", parent.get_attribute("frmCssProperties"))
        following_sibling = driver.find_element_by_xpath("//button/following-sibling::button")
        print(following_sibling.text)
        preceding_sibling = driver.find_element_by_xpath("//button/preceding-sibling::button")        
        print(preceding_sibling.text)
        ancestor = driver.find_element_by_xpath(".//ancestor::button")
        print(ancestor.text)
        child = driver.find_element_by_xpath( ".//*")
        print(child.text)
        time.sleep(5)


def main():
    web_element = WebElements()
    # web_element.test_setup()
    web_element.automate_xpath()



if __name__ == "__main__":
    main()
