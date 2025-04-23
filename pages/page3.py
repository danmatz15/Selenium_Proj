import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Page3(BasePage):
    FIRST_BTN=(By.CSS_SELECTOR,"td button")
    STOP_LOSS_CHECKBOX=(By.CSS_SELECTOR,"#stop-loss-checkbox")
    STOP_LOSS_INPUT=(By.CSS_SELECTOR,"#stop-loss-checkbox")
    REAL_TIME_PRICE=(By.CSS_SELECTOR,".buy-price strong")
    POP_UP_DIV=(By.CSS_SELECTOR,".buy-form")
    CURRENT_AMOUNT=(By.CSS_SELECTOR,"header div:nth-child(3)")
    CANCEL_BTN=(By.CSS_SELECTOR,".cancel-btn")
    BUY_INPUT = (By.CSS_SELECTOR, ".buy-input")
    CONFIRM_BTN=(By.CSS_SELECTOR,".confirm-buy-btn")

    @allure.severity(severity_level="high")
    def check_data(self):
        time.sleep(2)  # ← אם אתה באמת צריך לחכות, שים פעם אחת בהתחלה
        area_list=self.driver.find_elements(By.TAG_NAME,"tr")
        with allure.step("בדיקה שיש יותר מנתון אחד בטבלה"):
            if len(area_list)>1:


                return  True
            else:
                time.sleep(2)
                return False

    def check_pop_up(self):
        allure.step("לחיצה על הכפתור קנייה")
        self.click(self.FIRST_BTN)

        allure.step("ממתין שהמחיר יופיע באופן מלא")
        price_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".buy-price strong"))
        )
        price = price_element.text

        if not price.strip():
            raise ValueError("The price element is empty after waiting.")

        price2 = float(price.replace(",", "").replace("$", "").strip())
        price = price2 + 10

        allure.step("לחיצה על הצ'קבוקס stop loss")
        self.click(self.STOP_LOSS_CHECKBOX)

        allure.step("ממתין עד שהשדה stop-loss אינטראקטיבי")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.STOP_LOSS_INPUT)
        )

        allure.step("מזין את הערך בשדה stop-loss באמצעות JavaScript")
        element = self.driver.find_element(*self.STOP_LOSS_INPUT)
        self.driver.execute_script("arguments[0].value = arguments[1];", element, str(price))

        time.sleep(1)
        self.click(self.POP_UP_DIV)

        time.sleep(1)
        value = self.driver.find_element(By.CLASS_NAME, "buy-input")
        value = float(value.get_attribute("value"))

        allure.step("בדיקה האם הנתון התאפס או נשאר")
        print("here dan value 1 value 2")
        print(value,price2)
        self.click(self.CANCEL_BTN)
        return value <= price2

    def check_amount(self):
        try:
            # שליפת balance מהכותרת
            element = self.driver.find_element(By.CSS_SELECTOR, "header div:nth-child(3)")
            text = element.text
            number_float = float(text.replace("Balance: $", "").strip())

            with allure.step("לחיצה על כפתור קנייה"):
                self.click(self.FIRST_BTN)

            # המתנה להופעת שדה קנייה
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.BUY_INPUT)
            )

            # קבלת ערך קיים בשדה
            value = self.driver.find_element(*self.BUY_INPUT).get_attribute("value") or "0"
            value_float = float(value)

            with allure.step("ניסיון למלא עם סכום גדול מדי"):
                total = value_float + number_float
                self.fill_text(self.BUY_INPUT, f"{total:.2f}")

            time.sleep(1)

            allure.step("לחיצה על כפתור אישור")
            self.click(self.CONFIRM_BTN)

            # חיפוש פופאפ עם שגיאת insufficient funds
            for _ in range(10):
                elements = self.driver.find_elements(By.CSS_SELECTOR, ".popup-alert span")
                if elements:
                    popup_text = elements[0].text.strip()
                    print(f"🎯 תפסנו את הפופאפ: '{popup_text}'")
                    return "not enough funds" in popup_text.lower()
                time.sleep(1)

            print("❌ הפופאפ לא הופיע בזמן")
            return False

        except Exception as e:
            print(f"❌ שגיאה במהלך בדיקת קנייה עם חוסר כספים: {e}")
            self.driver.save_screenshot("check_amount_error.png")
            return False

        finally:
            # תמיד לסגור את הפופאפ בסוף
            try:
                self.click(self.CANCEL_BTN)
                time.sleep(1)
                self.click(self.MYINFO)
                print("here dan")
            except Exception as e:
                print(f"⚠️ לא הצלחנו ללחוץ על CANCEL_BTN: {e}")
