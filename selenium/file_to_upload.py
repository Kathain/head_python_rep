from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys('lilo')
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys('lil')
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys('lil@nn.ii')
    input4 = browser.find_element(By.CSS_SELECTOR, "[name='file']")
    # что бы узнать путь к файлу, зажми option во время того как будешь нажимать Скопировать файл
    input4.send_keys('/Users/katha/Desktop/work/file.txt')
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
