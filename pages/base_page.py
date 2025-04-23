import time
import re
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
class BasePage:
    MARKETS=(By.CSS_SELECTOR,"div nav li:nth-child(1) a")
    MYINFO=(By.CSS_SELECTOR,"div nav li:nth-child(2) a")
    NEWS=(By.CSS_SELECTOR,"div nav li:nth-child(3) a")
    HISTORIC=(By.CSS_SELECTOR,"div nav li:nth-child(4) a")
    AI=(By.CSS_SELECTOR,"div nav li:nth-child(5) a")
    INFO=(By.CSS_SELECTOR,"div nav li:nth-child(6) a")
    LOG_OUT_BTN=(By.CSS_SELECTOR,"header button")
    EXPECTED_URL="http://localhost:3000/login"
    def __init__(self,driver):
        self.driver:WebDriver=driver

    def balance(self):
        element=self.driver.find_element(By.CSS_SELECTOR,"nav div:nth-child(3)")
        number=element.text
        match=re.search(r"\d[\d,]*\.?\d*", number)
        return float(match.group().replace(",", ""))

    def check_log_out(self):
        self.click(self.LOG_OUT_BTN)
        time.sleep(3)
        print(self.EXPECTED_URL_LOG_OUT, self.driver.current_url)
        return self.EXPECTED_URL_LOG_OUT == self.driver.current_url

    def fill_color(self, locator, text,color):
        self.highlight_element(locator, color)
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)
    def fill_text(self,locator,text):
        time.sleep(0.5)
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)

    def click(self, locator):
        time.sleep(1)
        if isinstance(locator, tuple):
            self.driver.find_element(*locator).click()
        else:
            locator.click()

    def get_text(self,locator):
        time.sleep(1)
        return self.driver.find_element(*locator).text
    def set_background_color(self, locator, color):
        element = self.driver.find_element(*locator)
        self.driver.execute_script(f"arguments[0].style.background='{color}'", element)

    def highlight_element(self, locator, color: str):
        """
        Highlights (briefly) a web element by changing its background color.

        :param driver: The Selenium WebDriver instance.
        :param locator: The locator for the element to be highlighted.
        :param color: The color to highlight the element with (e.g., 'red', 'green').
        """
        # Find the element
        element = self.driver.find_element(*locator)
        # Store the original style (to revert after 300 mills)
        original_style = element.get_attribute("style")

        # Create the new style with the given color
        new_style = f"background-color: {color}; {original_style}"

        # Apply the new style
        self.driver.execute_script("""
                      var element = arguments[0];
                      var new_style = arguments[1];
                      setTimeout(function() {
                          element.setAttribute('style', new_style);
                      }, 0);
                  """, element, new_style)

        # Revert to the original style after a short 300 mills
        self.driver.execute_script("""
              var element = arguments[0];
              var originalStyle = arguments[1];
              setTimeout(function() {
                  element.setAttribute('style', originalStyle);
              },  100);
          """, element, original_style)
        element.clear()