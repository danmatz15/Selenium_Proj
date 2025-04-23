import time
from operator import truediv
import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page6(BasePage):
    PARAMETERS=(By.CSS_SELECTOR,".recharts-legend-item-text")
    GRAPH_BTN=(By.CSS_SELECTOR,".ms-1.btn.btn-primary ")
    BUY_BTN=(By.CSS_SELECTOR,".btn.btn-danger")
    BUY_INPUT=(By.CSS_SELECTOR,".ai-input")
    CONFIRM_BUY=(By.CSS_SELECTOR,".popup-btn.confirm-btn")
    POP_TEXT=(By.CSS_SELECTOR,".popup-alert span")
    CLOSE_BTN=(By.CSS_SELECTOR,"[aria-label='Stock Chart Modal'] button")
    def check_graph_headers(self):
        with allure.step("Click on AI button to show graph"):
            self.click(self.AI)

        with allure.step("Click on graph button"):
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.GRAPH_BTN)
            )
            self.click(self.GRAPH_BTN)

        with allure.step("Wait for the graph to fully load"):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, "tspan"))
            )

        x_y = self.driver.find_elements(By.TAG_NAME, "tspan")
        print("TSPAN COUNT:", len(x_y))
        self.click(self.CLOSE_BTN)
        time.sleep(2)
        return len(x_y) > 12
    @allure.severity(allure.severity_level.CRITICAL)
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







