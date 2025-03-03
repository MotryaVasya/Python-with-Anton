import pytest
from selenium import webdriver

@pytest.fixture(scope='calss')
def browser():
    print('\nstart browser...')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser...')
    browser.quit()