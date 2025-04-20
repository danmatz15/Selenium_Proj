import time

import pytest
from  selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from tests.base_test import BaseTest

@pytest.mark.usefixtures("setup_class")
class TestAll(BaseTest):
    DATA=[("dan", "dwqqwd", "dansadasd","Black"),("YOVAL","YOVA","YOVAL@gmail.com","lightblue")]
    @pytest.mark.parametrize("first_name, last_name, email, color", DATA)
    def test_01_demo(self, first_name, last_name, email, color):
        self.page1.fill_info(first_name, last_name, email, color)

    def test_03_demo(self):
        self.page2.change_btn()
    def test_04_demo(self):
        self.page3.fill_info("dadv","12","roshhayin","Argentina")
        assert self.page3.success_message()



