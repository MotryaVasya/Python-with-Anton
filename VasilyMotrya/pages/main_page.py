from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators
class MainPage(BasePage):

    def go_to_contacts_page(self):
        contacts = self.browser.find_element(*MainPageLocators.CONTACTS)
        contacts.click()
        go_to = self.browser.find_element(*MainPageLocators.CONTACT_PAGE)
        go_to.click()

    def go_to_next_site(self):
        img = self.browser.find_elements(*MainPageLocators.IMG_CONTACT_PAGE)
        img[0].click()