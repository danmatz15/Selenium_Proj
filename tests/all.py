import time
from tabnanny import check
from xmlrpc.client import boolean

import allure
import pytest

from  selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from tests.base_test import BaseTest

@pytest.mark.usefixtures("setup_class")

class TestAll(BaseTest):
    EXPECTED_URL="http://localhost:3000/in/myInfo"
    DATA=[("YOVAL@gmail.com",1234,"Red")]
    @pytest.mark.parametrize("email,password,color", DATA)
    @allure.title("fill info")
    @allure.description("fill unvaild info")

    def test_01_demo(self,email,password,color):
        time.sleep(6)
        self.page1.fill_info( email,password,color)
        assert self.page1.errorMsg(), "Expected error popup not found or text did not match"

    @allure.title("fill info")
    @allure.description("fill vaild info")

    def test_02_demo(self):
        self.page1.fill_info("danmatz15@gmail.com","123","Green")
        time.sleep(2)

    @allure.title("news check")
    @allure.description("check if read more button send me to the article")
    def test_03_demo(self):
        work=self.page2.check_news("Goldman cuts ratings on auto suppliers amid tariff, demand risks")
        assert work,"link not working"
    @allure.title("check if stop loss work.and have data")
    @allure.description("should be more then 2 tr.stop loss need to be lower then correct price")
    def test_04_demo(self):
        t=self.page3.check_data()
        assert t,"no found data"
        t2=self.page3.check_pop_up()
        assert t2,"error value should be lower the curent"
    @allure.title("check amount")
    @allure.description("Verify that the user cannot buy beyond their balance")
    def test_05_demo(self):
        assert self.page3.check_amount(), "User is able to buy stocks without sufficient funds"

    @allure.title("check input work")
    @allure.description("Check using a valid symbol from my list in the input field")
    def test_06_demo(self):
        time.sleep(2)
        assert self.page4.check_my_stock_input(),"no data found"

    @allure.title("Check if selling is available")
    @allure.description("Verify that the user is able to perform a sell action")
    def test_07_demo(self):
        time.sleep(2)
        assert self.page4.check_sell(), "no data found"

    @allure.title("Check if total profit/loss Exist ")
    @allure.description("Verify that there is an indicator showing the user how much profit or loss they made")
    def test_08_demo(self):
        time.sleep(2)
        assert self.page5.Existing_number_in_TOTAL()
    @allure.title("Check if buy form work ")
    def test_09_demo(self):
        assert self.page6.check_graph_headers()
        time.sleep(2)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_10_demo(self):
        assert self.page6.check_buy()

    @allure.title("Text Checking")
    @allure.description("Check if 'S&P 500' and 'Personal Portfolio' are shown")
    def test_11_demo(self):
        assert self.page7.check_parameters(), "One or more parameters were not found"
    @allure.title("wrong input check")
    @allure.description("entering unvalid input to see if error msg seen")
    def test_12_demo(self):
        assert self.page7.check_wrong_parameter_input(),"error msg not catch"

    @allure.title("Check if card is visible")
    @allure.description("Verify that the card is visible by locating an element inside it")
    def test_13_demo(self):
        assert  self.page7.check_function_of_analyze_work(),"card isn't visible "
        self.page7.back()
        time.sleep(2)
    @allure.title("check bars")
    @allure.description("check if have data for the bars")
    def test_14_demo(self):
        assert  self.page7.check_MOST_ACTIVE_DAY(),"problem with the bars"
        self.page7.next_page()

    @allure.title("check drag")
    @allure.description("Check if dragging the page to the right navigates to the next page")
    def test_15demo(self):
        self.page8.drag_to_buy()
    @allure.title("check if pop up shown")
    def test_16_demo(self):
       assert self.page8.pop_up_show(), "Pop-up not shown or missing"

    @allure.title("check if balance update")
    @allure.description("check if balance update after a buy")
    def test_17_demo(self):
       assert self.page8.balance_update()

    @allure.title("check url after buy")
    @allure.description(f"expected url={EXPECTED_URL}")
    def test_18_demo(self):
        assert self.page8.check_url(),"url wrong"
    @allure.title("check balance")
    @allure.description("check balance after refresh")
    def test_19_demo(self):
       assert self.page8.balance_refresh(),"balance not shown"
    @allure.title("check logout")
    @allure.title("check when i log out i move to the correct url")
    def test_20_demo(self):
        assert self.page8.check_log_out(),f"THE URL IS NOT {self.page8.EXPECTED_URL_LOG_OUT}"







