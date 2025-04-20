import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
class BasePage:

    def __init__(self,driver):
        self.driver:WebDriver=driver

    def fill_color(self, locator, text,color):
        self.highlight_element(locator, color)
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)
    def fill_text(self,locator,text):
        time.sleep(0.5)
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)

    def click(self,locator):
        time.sleep(1)
        self.driver.find_element(*locator).click()

    def get_text(self,locator):
        time.sleep(1)
        return self.driver.find_element(*locator).text


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