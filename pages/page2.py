from selenium.webdriver.chrome.webdriver import WebDriver

from pages.base_page import BasePage
import time
from symtable import Class
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Page2(BasePage):
    MORE=(By.CSS_SELECTOR,".expand-btn")
    READ_MORE=(By.CSS_SELECTOR,".news-button")



    def check_news(self,title):
        main_window = self.driver.current_window_handle
        area_list=self.driver.find_elements(By.CSS_SELECTOR,".news-card")
        for area in area_list:
            header=area.find_element(By.CSS_SELECTOR,".news-heading")
            if header.text==title:

                link=area.find_element(By.CSS_SELECTOR,".news-button")
                self.click(link)
                time.sleep(2)
                self.driver.switch_to.window(main_window)
                time.sleep(2)
                self.click(self.MARKETS)
                return True


        return  False



