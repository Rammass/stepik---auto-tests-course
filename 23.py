from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os


try:


    # link = 'http://suninjuly.github.io/alert_accept.html'
    # browser = webdriver.Chrome()
    # browser.get(link)
    # browser.find_element_by_tag_name('button').click()
    # browser.switch_to.alert.accept()
    # val = int(browser.find_element_by_id('input_value').text)
    # browser.find_element_by_id('answer').send_keys(
    #      str(math.log(abs(12*math.sin(val)))))
    # browser.find_element_by_tag_name('button').click()
    # time.sleep(3)

    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_tag_name('button').click()
    browser.switch_to.window(browser.window_handles[1])
    val = int(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(
         str(math.log(abs(12*math.sin(val)))))
    browser.find_element_by_tag_name('button').click()
    time.sleep(3)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()