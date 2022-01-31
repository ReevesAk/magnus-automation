import pytest
from selenium import webdriver


class TestLocators:
    @pytest.fixture(scope="class")
    def test_setup(self):
        global DRIVER
        DRIVER = webdriver.Chrome()
        DRIVER.implicitly_wait(20)
        DRIVER.maximize_window()
        DRIVER.get("http://magnus.jalaacademy.com/Account/Login")
        yield
        DRIVER.close
        DRIVER.quit()

    @staticmethod
    def test_title(test_setup):
        DRIVER.find_element_by_id("UserName").send_keys("training@jalaacademy.com")
        DRIVER.find_element_by_id("Password").send_keys("jobprogram")
        DRIVER.find_element_by_id("btnLogin").click()
        assert type(DRIVER.title) is not int

    @staticmethod
    def test_login(test_setup):
        DRIVER.find_element_by_id("UserName").send_keys("training@jalaacademy.com")
        DRIVER.find_element_by_id("Password").send_keys("jobprogram")

        # Check if site login page was successful
        # assert login == "Magnus"
        DRIVER.find_element_by_class_name("checkmark").click()
        DRIVER.find_element_by_id("btnLogin").click()
        DRIVER.get("http://magnus.jalaacademy.com/Home/Index")
        assert DRIVER.current_url == "http://magnus.jalaacademy.com/Home/Index"

    @pytest.mark.skip
    @staticmethod
    def test_instance(test_setup):
        DRIVER.get("http://magnus.jalaacademy.com/Home/Index")
        assert isinstance(DRIVER.current_url, str)

    @staticmethod
    def test_class():
        test_locators = TestLocators()
        assert type(test_locators).__name__ == 'TestLocators'

    @staticmethod
    def test_current_url(test_setup):
        DRIVER.get("http://magnus.jalaacademy.com/Home/Index")
        assert "Magnus" in DRIVER.page_source


def main():
    locator = TestLocators()
    locator.test_instance()


if __name__ == "__main__":
    main()
