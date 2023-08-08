from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = 'https://SunInJuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)


    def count_test(x):
        res = math.log(abs(12 * math.sin(x)))
        return res


    input1 = browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value').text
    input1 = int(input1)
    res1 = count_test(input1)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("window.scrollBy(0, 100);")
    input2 = browser.find_element(By.ID, 'answer')
    input2.send_keys(res1)
    checkbox_Im_Robot = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    checkbox_Im_Robot.click()
    radio_RobotsRule = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radio_RobotsRule.click()
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
