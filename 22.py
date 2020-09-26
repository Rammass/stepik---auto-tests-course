from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os


try:

    # link = 'http://suninjuly.github.io/selects1.html'
    # browser = webdriver.Chrome()
    # browser.get(link)
    # val = int(browser.find_element_by_id('num1').text) + int(browser.find_element_by_id('num2').text)
    # select = Select(browser.find_element_by_tag_name("select"))
    # select.select_by_value(str(val)) # ищем элемент с текстом "Python"
    #
    # browser.find_element_by_tag_name('Button').click()
    #
    # time.sleep(3)

    # link = 'http://SunInJuly.github.io/execute_script.html'
    # browser = webdriver.Chrome()
    # browser.get(link)
    # val = int(browser.find_element_by_id('input_value').text)
    # browser.find_element_by_id('answer').send_keys(
    #      str(math.log(abs(12*math.sin(val)))))
    # browser.execute_script("window.scrollBy(0, 100);")
    # browser.find_element_by_id('robotCheckbox').click()
    # browser.find_element_by_id('robotsRule').click()
    # browser.find_element_by_tag_name('button').click()
    #
    # time.sleep(3)

    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_name('firstname').send_keys('ivan')
    browser.find_element_by_name('lastname').send_keys('ivan')
    browser.find_element_by_name('email').send_keys('ivan')
    browser.find_element_by_name('file').send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'y.txt'))
    browser.find_element_by_tag_name('button').click()

    time.sleep(3)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()