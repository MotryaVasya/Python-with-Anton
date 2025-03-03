import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()

browser.get(link)
num1 = browser.find_element(By.CSS_SELECTOR, '#num1').text
num2 = browser.find_element(By.CSS_SELECTOR, '#num2').text
for item in browser.find_elements(By.CSS_SELECTOR, 'option'):
    if item.text == str((int)(num1) + (int)(num2)):
        item.click()
browser.find_element(By.CSS_SELECTOR, "button").click()

time.sleep(2)
browser.quit()