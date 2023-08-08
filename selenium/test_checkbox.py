import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'https://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    print(x)
    y = calc(x)
    result = browser.find_element(By.CSS_SELECTOR, '#answer')
    result.send_keys(y)
    checkbox_Im_Robot = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    checkbox_Im_Robot.click()
    radio_RobotsRule = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radio_RobotsRule.click()
    sub_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    sub_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
