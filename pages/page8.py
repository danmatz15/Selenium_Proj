import time
from operator import truediv
import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
class Page8(BasePage):
    BALANCE=(By.CSS_SELECTOR,"nav div:nth-child(3)")
    EXPECTED_URL = "http://localhost:3000/in/myInfo"
    question_mark=(By.CSS_SELECTOR,"div>div> span")
    POP_UP=(By.CSS_SELECTOR,".popup-alert span")
    INPUT=(By.CSS_SELECTOR,"label .buy-input")
    CONFIRM_BTN=(By.CSS_SELECTOR,".buy-container button:nth-of-type(1)")
    EXPECTED_URL_LOG_OUT="http://localhost:3000/login"
    def drag_to_buy(self):
        actions = ActionChains(self.driver)
        source = self.driver.find_element(By.CSS_SELECTOR, ".lala.me-1")  # האלמנט שגוררים
        actions.click_and_hold(source).move_by_offset(100, 0).release().perform()
        time.sleep(4)
    def pop_up_show(self):
        with allure.step("click on question mark"):
            self.click(self.question_mark)
        pop_up=WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(self.POP_UP)
        )
        return "סטופ-לוס הוא מנגנון שמוכר מניה אוטומטית אם. המחיר יורד מתחת לרמה מסוימת כדי למנוע הפסדים" in pop_up.text

    def balance_update(self):
        before=self.balance()
        with allure.step("entering a num"):
            self.fill_text(self.INPUT,"10")
        time.sleep(2)
        with allure.step("click on confirm"):
            self.click(self.CONFIRM_BTN)
        time.sleep(1)
        after=self.balance()
        return before != after
    def check_url(self):
        time.sleep(3)
        return self.driver.current_url==self.EXPECTED_URL
    def balance_refresh(self):
        time.sleep(1)
        allure.step("page refresh")
        self.driver.refresh()
        element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.BALANCE))
        return element.is_displayed()





