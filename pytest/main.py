import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/'


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture(autouse=True)
def prepare_data():
    print('\nprepare data...')

class TestMainPage1:
    @pytest.mark.mytest
    def test_quest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')


    @pytest.mark.mytest
    def test_quest_should_see_find_buttin(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.navbar-right .btn')