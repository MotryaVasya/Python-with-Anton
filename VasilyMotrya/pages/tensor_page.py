from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators

class TensorPage(BasePage):
    def go_to_about(self):
        if self.is_element_present(*MainPageLocators.POWER_IN_PEOPLE):
            about = self.browser.find_element(*MainPageLocators.ABOUT)
            about.click()

    def check_images(self):
        images = self.browser.find_elements(*MainPageLocators.IMAGES)
        width = images[0].size['width']
        height = images[0].size['height']
        index = 0
        for item in images:
            if item.size['width'] is width and item.size['height'] is height:
                index += 1
            if index == len(images):
                return True
        return False