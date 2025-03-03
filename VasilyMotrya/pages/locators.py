from selenium.webdriver.common.by import By
class MainPageLocators:
    CONTACTS = (By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu>div:nth-child(1)')
    CONTACT_PAGE = (By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu__items .sbisru-link>span')
    IMG_CONTACT_PAGE = (By.CSS_SELECTOR, '.sbisru-Contacts__border-left>a>img')
    POWER_IN_PEOPLE = (By.CSS_SELECTOR, '.s-Grid-col .tensor_ru-Index__block4-content')
    ABOUT = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-content > p > a')
    IMAGES = (By.CSS_SELECTOR, '.tensor_ru-container .s-Grid-container .s-Grid-col > a > div > img')