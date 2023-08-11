from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    def count_test(x):
        res = math.log(abs(12 * math.sin(x)))
        return res


    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    input1 = browser.find_element(By.ID,'book')
    input1.click()
    button = browser.find_element(By.ID, "solve")
    browser.execute_script("window.scrollBy(0, 100);")
    input2 = browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value').text
    input2 = int(input2)
    res1 = count_test(input2)
    input3 = browser.find_element(By.ID, 'answer')
    input3.send_keys(res1)
    button.click()
finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()



