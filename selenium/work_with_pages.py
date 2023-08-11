from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    def count_test(x):
        res = math.log(abs(12 * math.sin(x)))
        return res

    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(3)
    cl1 = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    cl1.click()
    browser.implicitly_wait(4)
    current_window = browser.current_window_handle
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    input1 = browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value').text
    input1 = int(input1)
    res1 = count_test(input1)
    browser.implicitly_wait(4)
    input2 = browser.find_element(By.ID, 'answer')
    input2.send_keys(res1)
    browser.implicitly_wait(4)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
