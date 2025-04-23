import time

import allure
import pytest
from  selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

from tests.all import TestAll
from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup_class")

class Test_page_01(BaseTest):

        DATA = [("YOVAL@gmail.com", 1234, "lightblue")]
        @pytest.mark.parametrize("email,password,color", DATA)
        @allure.title("check hhfd123")
        @allure.description("work")
        def test_01_demo(self, email, password, color):
            self.page1.fill_info(email, password, color)
            assert self.page1.errorMsg(), "Expected error popup not found or text did not match"

        def test_02_demo(self):
            assert 1 == 2

        def test_03_demo(self):
            assert 1 == 2