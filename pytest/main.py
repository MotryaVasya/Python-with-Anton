import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()

browser.get(link)
num1 = browser.find_element(By.CSS_SELECTOR, '#num1').text
num2 = browser.find_element(By.CSS_SELECTOR, '#num2').text
for item in browser.find_elements(By.CSS_SELECTOR, 'option'):
    print(item.text)
    if item.text == num1 + num2:
        item.click()

@pytest.fixture()
def browser():
    yield browser
    browser.quit()

@pytest.fixture(autouse=True)
def prepare_data():
    print('\nprepare data...')

class TestMainPage1:
    @pytest.mark.mytest
    def test_quest_should_see_login_link(self, browser):
        pass
