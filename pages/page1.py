import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.base_page import BasePage
import time
from symtable import Class
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Page1(BasePage):
    FIRST_NAME=(By.CSS_SELECTOR,"#firstname")
    LAST_NAME=(By.CSS_SELECTOR,"#lastname")
    EMAIL=(By.CSS_SELECTOR,"#email")
    BTN_NEXT=(By.CSS_SELECTOR,".btn.btn-next")
    error_msg=(By.CSS_SELECTOR,"#email-error")
    def __init__(self,driver):
        super().__init__(driver)
    @pytest.mark.parametrize("first_name, last_name, email, color",)
    def fill_info(self,first_name,last_name,email,color):
        self.fill_text(self.FIRST_NAME,first_name)
        self.fill_text(self.LAST_NAME,last_name)
        element = self.driver.find_element(*self.LAST_NAME)
        time.sleep(3)
        self.driver.execute_script(f"arguments[0].style.background='{color}'", element)
        self.fill_text(self.EMAIL,email)
        self.click(self.BTN_NEXT)
    def errorMsg(self):
        return  self.get_text(self.error_msg) =="Please enter a valid email address."