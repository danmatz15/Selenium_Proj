from selenium.webdriver.chrome.webdriver import WebDriver

from pages.base_page import BasePage
import time
from symtable import Class
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Page2(BasePage):
    BEGINNER=(By.CSS_SELECTOR,".fa.fa-blind")
    Advanced=(By.CSS_SELECTOR,".fa.fa-star")
    NEXT_BTN=(By.CSS_SELECTOR,".btn.btn-next")
    def __init__(self,driver):
        super().__init__(driver)

    def change_btn(self):
        self.click(self.BEGINNER)
        self.click(self.Advanced)
        time.sleep(2)
        self.click(self.NEXT_BTN)



