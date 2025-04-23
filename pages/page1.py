import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time
from symtable import Class
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Page1(BasePage):
    START_TRANDING=(By.CSS_SELECTOR,"#root > div > header > div:nth-child(2) > a:nth-child(2)")
    EMAIL=(By.CSS_SELECTOR,"[name='email']")
    PASSWORD=(By.CSS_SELECTOR,"[name='password']")
    SUBMIT=(By.CSS_SELECTOR,"#root > div > div > div > form > button")
    error_msg=(By.CSS_SELECTOR, ".popup-alert  span")
    def __init__(self,driver):
        super().__init__(driver)

    def fill_info(self,email,password,color=None):
        self.fill_text(self.EMAIL,email)
        self.set_background_color(self.EMAIL,color)
        self.fill_text(self.PASSWORD,password)
        self.set_background_color(self.PASSWORD,color)
        time.sleep(1)
        element = self.driver.find_element(*self.EMAIL)

        self.click(self.SUBMIT)


    def errorMsg(self):
        try:
            wait = WebDriverWait(self.driver, 10)  # הארכנו ל-10 שניות

            # נבדוק כל שנייה אם הפופאפ קיים
            for _ in range(10):
                elements = self.driver.find_elements(*self.error_msg)
                if elements:
                    popup_text = elements[0].text.strip()
                    print(f"🎯 תפסנו את הפופאפ: '{popup_text}'")
                    return popup_text == "Email or password is incorrect"
                time.sleep(1)

            print("❌ הפופאפ לא הופיע כלל במהלך הזמן שהוקצב")
            return False

        except Exception as e:
            print(f"❌ שגיאה בזמן ניסיון לתפוס את הפופאפ: {e}")
            self.driver.save_screenshot("popup_debug.png")
            return False
