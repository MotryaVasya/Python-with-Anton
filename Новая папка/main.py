import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



try:
    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/selects1.html')
    time.sleep(1)

    num1 = driver.find_element(By.CSS_SELECTOR, '#num1').text
    num2 = driver.find_element(By.CSS_SELECTOR, '#num2').text
    res = int(num1) + int(num2)
    dropdown = driver.find_element(By.CSS_SELECTOR, '#dropdown')
    options = driver.find_elements(By.TAG_NAME, 'option')
    for i in options:
        if i.text == str(res):
            i.click()



    button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    time.sleep(1)
finally:
    time.sleep(5)
    driver.quit()


# TODO поиск элементов в Selenium
'''
1) find_element(By.ID, value) - поиск по уникальному атрибуду id элемента 
2) find_element(By.CSS_SELECTOR, value) - поиск на основе CSS
3) find_element(By.XPATH, value) - поиск на основе PATH
4) find_element(By.NAME, value) - поиск по name
5) find_element(By.CLASS_NAME, value) - поиск по названию класса 
6) find_element(By.TAG_NAME, value) - поиск по названию тега
7) find_element(By.LINK_TEXT, value) - поиск ссылки на странице по полному совпадению
8) find_element(By.PARTIAL_LINK_TEXT, value) - поиск ссылки на странице если текст селектора совпадает с любой частью текста ссылки
'''