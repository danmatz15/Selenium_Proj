import allure
import pytest
import os
from selenium import webdriver
from pages.page1 import Page1
from pages.page2 import Page2
from pages.page3 import Page3
from pages.page4 import Page4
from pages.page5 import Page5
from pages.page6 import Page6
from pages.page7 import Page7
from pages.page8 import Page8


def pytest_exception_interact(report):
    try:
        allure.attach(body=driver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)
    except NameError:
        print("Driver not defined, skipping screenshot.")


# מופעל פעם אחת לכל קלאס
@pytest.fixture(scope="class")
def setup_class(request):
    global  driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:3000/login")
    request.cls.driver = driver
    request.cls.page1 = Page1(driver)
    request.cls.page2 = Page2(driver)
    request.cls.page3 = Page3(driver)
    request.cls.page4=Page4(driver)
    request.cls.page5 = Page5(driver)
    request.cls.page6 = Page6(driver)
    request.cls.page7 = Page7(driver)
    request.cls.page8 = Page8(driver)
#pages
    yield
    driver.quit()

# מופעל לפני כל טסט
@pytest.fixture(scope="function")
def setup_function(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:3000/login")
    request.cls.driver = driver
    request.cls.page1 = Page1(driver)
    request.cls.page2 = Page2(driver)
    request.cls.page3 = Page3(driver)
    request.cls.page4 = Page4(driver)
    request.cls.page5 = Page5(driver)
    request.cls.page6 = Page6(driver)
    request.cls.page7 = Page7(driver)
    request.cls.page8 = Page8(driver)
    yield
    driver.quit()

# מופעל פעם אחת לכל הסשן
@pytest.fixture(scope="session")
def setup_session(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:3000/login")
    request.cls.driver = driver
    request.cls.page1 = Page1(driver)
    request.cls.page2 = Page2(driver)
    request.cls.page3 = Page3(driver)
    request.cls.page4 = Page4(driver)
    request.cls.page5 = Page5(driver)
    request.cls.page6 = Page6(driver)
    request.cls.page7 = Page7(driver)
    request.cls.page8 = Page8(driver)

    yield
    driver.quit()
import os


def pytest_sessionfinish(session, exitstatus):
    global driver
    environment_properties = {
        'browser': driver.name,
        'driver_version': driver.capabilities['browserVersion']
    }

    # 🟢 שנה ל-allure-results2
    allure_env_path = os.path.join("allure-results", 'environment.properties')
    os.makedirs(os.path.dirname(allure_env_path), exist_ok=True)

    with open(allure_env_path, 'w') as f:
        data = '\n'.join([f'{k}={v}' for k, v in environment_properties.items()])
        f.write(data)