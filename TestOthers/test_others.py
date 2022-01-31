import pytest
from selenium import webdriver


class TestMagnus:
    @pytest.fixture(scope="class")
    def test_setup(self):
        global DRIVER
        DRIVER = webdriver.Chrome()
        DRIVER.implicitly_wait(20)
        DRIVER.maximize_window()
        DRIVER.get("http://magnus.jalaacademy.com/Account/Login")
        yield
        DRIVER.close()
        DRIVER.quit()

    @staticmethod
    def test_more_menu(test_setup):
        DRIVER.get("http://magnus.jalaacademy.com/Home/Index")
        DRIVER.find_element_by_id("UserName").send_keys("training@jalaacademy.com")
        DRIVER.find_element_by_id("Password").send_keys("jobprogram")
        DRIVER.find_element_by_id("btnLogin").click()
        welcome_msg = DRIVER.find_element_by_xpath("//h1[normalize-space()='Welcome to Magnus']").text
        assert welcome_msg == "Welcome to Magnus"

    @pytest.mark.parametrize("Login_logo, expected", [
        ("Magnus", "Magnus")
    ])
    def test_page_link(self, test_setup, Login_logo, expected):
        DRIVER.get("http://magnus.jalaacademy.com/Account/Login")
        expected = DRIVER.find_element_by_xpath("/html/body/div[2]/div[1]/a/b").text
        assert Login_logo == expected
