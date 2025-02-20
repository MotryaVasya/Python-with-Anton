import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/redirect_accept.html')
    time.sleep(1)

    button = driver.find_element(By.CSS_SELECTOR, "button")
    button.click()

    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    input_value = driver.find_element(By.CSS_SELECTOR, "#input_value")
    x = math.log(abs(12 * math.sin(int(input_value.text))))

    answer = driver.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(str(x))

    button = driver.find_element(By.CSS_SELECTOR, "button")
    button.click()
finally:
    time.sleep(3)
    driver.quit()