import allure
import pytest
from selenium import webdriver
from pages.page1 import Page1
from pages.page2 import Page2
from pages.page3 import Page3

def pytest_exception_interact(report):
    if report.faild:
        allure.attach(body=driver.get_screenshot_as_png(),name="screenshot",attachment_type=allure.attachment_type.PNG)
# מופעל פעם אחת לכל קלאס
@pytest.fixture(scope="class")
def setup_class(request):
    global  driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automation.co.il/tutorials/selenium/demo1/indexNoID.html")
    request.cls.driver = driver
    request.cls.page1 = Page1(driver)
    request.cls.page2 = Page2(driver)
    request.cls.page3 = Page3(driver)
#pages
    yield
    driver.quit()

# מופעל לפני כל טסט
@pytest.fixture(scope="function")
def setup_function(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automation.co.il/tutorials/selenium/demo1/indexNoID.html")
    request.cls.driver = driver
    request.cls.page1 = Page1(driver)
    request.cls.page2 = Page2(driver)
    request.cls.page3 = Page3(driver)
    yield
    driver.quit()

# מופעל פעם אחת לכל הסשן
@pytest.fixture(scope="session")
def setup_session(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automation.co.il/tutorials/selenium/demo1/indexNoID.html")
    request.cls.driver = driver
    request.cls.page1 = Page1(driver)
    request.cls.page2 = Page2(driver)
    request.cls.page3 = Page3(driver)

    yield
    driver.quit()
def pytest_sessionfinish() -> None:
    environment_properties = {
     'browser': driver.name,
     'driver_version': driver.capabilities['browserVersion']
    }
    allure_env_path = os.path.join("allure-results", 'environment.properties')
    with open(allure_env_path, 'w') as f:
        data = '\n'.join([f'{variable}={value}' for variable, value in environment_properties.items()])
        f.write(data)