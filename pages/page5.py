import time
import re
from operator import truediv

import allure
from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page5(BasePage):


    TOTAL_PROFIT_LOSS=(By.CSS_SELECTOR,".historic-report-profit-loss-total span ")
    GRAPH_BTN=(By.CSS_SELECTOR,".ms-1.btn.btn-primary ")
    BUY_BTN=(By.CSS_SELECTOR,".btn.btn-danger")
    BUY_INPUT=(By.CSS_SELECTOR,".ai-input")
    CONFIRM_BUY=(By.CSS_SELECTOR,".popup-btn.confirm-btn")
    POP_TEXT=(By.CSS_SELECTOR,".popup-alert span")

    def Existing_number_in_TOTAL(self):
        actions = ActionChains(self.driver)

        with allure.step("Waiting for pop-up to disappear (if exists)"):
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.invisibility_of_element_located((By.CSS_SELECTOR, ".lucide-x"))
                )
            except:
                pass  # אם לא קיים, נמשיך כרגיל

        with allure.step("click to move to historic"):
            self.click(self.HISTORIC)

        time.sleep(3)
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TOTAL_PROFIT_LOSS)
        )
        actions.move_to_element(element).perform()
        text = element.text
        print(text)

        with allure.step("Check if the element contains both a number and a percentage"):
            match = re.search(r'-?\d+(\.\d+)?', text)
        return match and "%" in text
    def check_graph_headers (self):
        with allure.step("click on btn graph"):
            self.click(self.GRAPH_BTN)
        x_y=self.driver.find_elements(By.TAG_NAME,"tspan")
        return len(x_y) >12

    def check_buy(self):
        with allure.step("click on buy btn"):
            self.click(self.BUY_BTN)

        with allure.step("Entering the value 12"):
            self.fill_text(self.BUY_INPUT,12)

        with allure.step("click on buy confirm"):
            self.click(self.CONFIRM_BUY)
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.POP_TEXT)
        )
        return  "בוצע בהצלחה" in element.text








