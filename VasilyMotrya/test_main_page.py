import time

from pages.main_page import MainPage
from pages.tensor_page import TensorPage


def test_guest_can_go_to_login_page(browser):
    link = 'https://saby.ru/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_contacts_page()
    time.sleep(2)
    page.go_to_next_site()
    time.sleep(1)
    windows = browser.window_handles
    browser.switch_to.window(windows[-1])
    page = TensorPage(browser, browser.current_url)
    page.go_to_about()
    time.sleep(2)
    page.check_images()
    time.sleep(2)