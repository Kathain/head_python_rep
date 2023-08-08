from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calculate(x, y):
    return x + y
try:

    link = 'https://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)
    id_num1 = browser.find_element(By.ID, 'num1').text
    id_num2 = browser.find_element(By.ID, 'num2').text
    for i in id_num1 and id_num2:
        id_num1 = int(id_num1)
        id_num2 = int(id_num2)
    res = calculate(id_num1, id_num2)
    res = str(res)
    sel = browser.find_element(By.CLASS_NAME, 'custom-select')
    sel.click()
    var1 = browser.find_elements(By.CSS_SELECTOR, "#dropdown option")
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(res)  # ищем элемент с текстом "Python"
    sub_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    sub_button.click()





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()