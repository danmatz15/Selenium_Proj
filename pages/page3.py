from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Page3(BasePage):
    NAME=(By.CSS_SELECTOR,"[name='streetname']")
    NUMBER=(By.CSS_SELECTOR,"[name='streetnumber']")
    CITY=(By.CSS_SELECTOR,"[name='city']")
    COUNTRY=(By.CSS_SELECTOR,"#country")
    FINISH_BTN=(By.CSS_SELECTOR,"#finish")
    SUCCESS=(By.CSS_SELECTOR,".cta-title")
    def __init__(self,driver):
        super().__init__(driver)


    def fill_info(self,name,number,city,country):
        self.fill_text(self.NAME,name)
        self.fill_text(self.NUMBER,number)
        self.fill_text(self.CITY,city)
        country_select = self.driver.find_element(By.CSS_SELECTOR,"#country")
        select=Select(country_select)
        select.select_by_value(country)
        self.click(self.FINISH_BTN)
        time.sleep(2)
    def success_message(self):
        text=self.get_text(self.SUCCESS)
        return text== "Congratulations!"




