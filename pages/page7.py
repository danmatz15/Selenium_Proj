import time
from operator import truediv
import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page7(BasePage):
    PARAMETERS=(By.CSS_SELECTOR,".recharts-legend-item-text")
    ANALYZE_STOCK=(By.CSS_SELECTOR,".p-4.justify-content-center.align-items-center.text-center >button.btn.btn-danger:nth-of-type(1)")
    MOST_TRADED_DATE_TITLE =(By.CSS_SELECTOR,".p-4.justify-content-center.align-items-center.text-center >button.btn.btn-danger:nth-of-type(2)")
    INPUT_ANALYZE=(By.CSS_SELECTOR,'[placeholder="הכנס סימבול של מניה (למשל NVDA)"]')
    SEARCH_BTN=(By.CSS_SELECTOR,".search-container>button")
    ERROR_MSG=(By.CSS_SELECTOR,".analayze-container p")
    DATE=(By.TAG_NAME,"h4")
    CURRENT_PRICE=(By.CSS_SELECTOR,".sale-card.justify-content-center.align-items-center p:nth-child(2) strong")
    NUM_OF_STOCKS=(By.CSS_SELECTOR,"p:nth-child(3)")
    ROW=(By.CSS_SELECTOR,"table tbody")
    GRAPH_TITLE_MOST_ACTIVE_DAY =(By.CSS_SELECTOR,"button:nth-of-type(2)")
    ELEMENT=(By.CSS_SELECTOR,"g.recharts-bar-rectangle path")
    STATIC_INPUT=(By.CSS_SELECTOR,'[placeholder="Search financial instruments..."]')
    SEARCH_RESULTS=(By.XPATH, '//*[@id="root"]/div/header/nav/div[1]/div/div[1]')
    def check_parameters(self):
        with allure.step("click info to move to info"):
            self.click(self.INFO)

        stock_portfolio = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.PARAMETERS)
        )
        sp = self.driver.find_element(By.CSS_SELECTOR,
                                           ".recharts-legend-item:nth-child(2) .recharts-legend-item-text")
        return "תיק אישי" in   stock_portfolio.text and "S&P 500" in sp.text

    def check_wrong_parameter_input(self):
        with allure.step("click on analyze stocks"):
             self.click(self.ANALYZE_STOCK)
        time.sleep(1)
        with allure.step("entering worng input"):
            self.fill_text(self.INPUT_ANALYZE,"worng_sybmol")
        self.set_background_color(self.INPUT_ANALYZE,"Red")
        time.sleep(1)
        self.click(self.SEARCH_BTN)
        try:
            error=WebDriverWait(self.driver,2).until(
                EC.visibility_of_element_located(self.ERROR_MSG)
            )
            return "שגיאה או לא נמצאו תוצאות למניה הזו" in error.text
        except Exception as e:
            print("Error",e)
            return  False

    def check_function_of_analyze_work(self):
        try:
            time.sleep(2)
            with allure.step("Entering valid info"):
                self.fill_text(self.INPUT_ANALYZE, "NVDA")
            self.set_background_color(self.INPUT_ANALYZE, "Green")

            with allure.step("Click on search button"):
                self.click(self.SEARCH_BTN)

            # ממתין לכותרת שתופיע
            date = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.TAG_NAME, "h4"))
            )

            # ממתין למחיר הנוכחי ומספר המניות
            current_price = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, ".sale-card.justify-content-center.align-items-center p:nth-child(2) strong"))
            )

            num_of_stocks = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "p:nth-child(3)"))
            )

            # מוצא את כל התאים בטבלה
            row_list = self.driver.find_elements(By.CSS_SELECTOR, "table tbody td")
            if not any(td.text.strip() for td in row_list):
                print("❌ כל התאים בטבלה ריקים.")
                return False

            # הדפסות debug
            print(f"✔️ Date text: {date.text}")
            print(f"✔️ Current Price: {current_price.text}")
            print(f"✔️ Num of Stocks: {num_of_stocks.text}")
            print(f"✔️ Found {len(row_list)} table cells.")

            result = (
                    len(date.text.strip()) > 1 and
                    len(current_price.text.strip()) > 1 and
                    len(num_of_stocks.text.strip()) > 1
            )

            time.sleep(2)
            return result

        except Exception as e:
            print(f"❗ שגיאה באימות הכרטיס: {e}")
            return False
    def check_MOST_ACTIVE_DAY(self):
        most_active_btn=WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(self.GRAPH_TITLE_MOST_ACTIVE_DAY)
        )
        allure.step("click on _MOST_ACTIVE_DAY btn ")
        self.click(self.GRAPH_TITLE_MOST_ACTIVE_DAY)
        wait_bar=WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(self.ELEMENT)
        )
        bar_list=self.driver.find_elements(By.CSS_SELECTOR,"g.recharts-bar-rectangle path")
        for bar in bar_list:
            path_x=float(bar.get_attribute("x"))
            path_y=float(bar.get_attribute("y"))
            if path_x<1 or path_y<1:
                return False
        return True
    def next_page(self):
        self.fill_text(self.STATIC_INPUT,"NVDA")
        time.sleep(2)
        self.click(self.SEARCH_RESULTS)
        time.sleep(5)

    def back(self):
        self.driver.back()