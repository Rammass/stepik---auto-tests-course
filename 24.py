from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:

    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    browser.find_element_by_id('book').click()
    val = int(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(
         str(math.log(abs(12*math.sin(val)))))
    browser.find_element_by_id('solve').click()
    time.sleep(3)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()