import time

import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page4(BasePage):
    INPUT_STOCKS = (By.CSS_SELECTOR, ".search-bar input")
    SEARCH_BTN=(By.CSS_SELECTOR, ".search-bar button")
    SELL_BTN=(By.CSS_SELECTOR,"td button")
    SELL_CONFIRM=(By.CSS_SELECTOR,".me-2.modern-button")
    POP_UP=(By.CSS_SELECTOR,".popup-alert span")
    def check_my_stock_input(self):
        item=self.driver.find_element(By.CSS_SELECTOR,"tr td")
        print(item.text)
        with allure.step("fill the text with Existing stock"):
            self.fill_text(self.INPUT_STOCKS,item.text)
        time.sleep(1)
        with allure.step("click on search button"):
            self.click(self.SEARCH_BTN)
        time.sleep(2)
        rows=self.driver.find_elements(By.TAG_NAME,"tr")
        return len(rows)>1

    @allure.severity(severity_level="high")
    def check_sell(self):
        with allure.step("לחיצה על כפתור המכירה"):
            self.click(self.SELL_BTN)
            time.sleep(1)
        with allure.step("לחציה על אישור מכירה"):
            self.click(self.SELL_CONFIRM)

        # המתן שהפופאפ יופיע
        try:
            popup = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".popup-alert"))
            )
            msg = popup.text


            if "נמכר בהצלחה" in msg:
                return True
            else:
                return False
        except Exception as e:
            print("שגיאה בזיהוי הפופאפ:", e)
            return False



