from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    def count_test(x):
        res = math.log(abs(12 * math.sin(x)))
        return res

    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    cl1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    cl1.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    input1 = browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value').text
    input1 = int(input1)
    res1 = count_test(input1)
    input2 = browser.find_element(By.ID, 'answer')
    input2.send_keys(res1)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
