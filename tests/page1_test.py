import time

import pytest
from  selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

from tests.base_test import BaseTest

pytest.mark.parametrize
@pytest.mark.usefixtures("setup_class")
class Test_page_01(BaseTest):
    def test_01_demo(self):
        print("test 01")