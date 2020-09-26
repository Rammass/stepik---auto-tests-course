from selenium import webdriver
import time
import math

try:
    # link = "http://suninjuly.github.io/math.html"
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)
    # browser.find_element_by_id('answer').send_keys(
    #     str(math.log(abs(12*math.sin(int(browser.find_element_by_id('input_value').text))))))
    browser.find_element_by_id('answer').send_keys(
         str(math.log(abs(12*math.sin(int(browser.find_element_by_id('treasure').get_attribute('valuex')))))))
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_tag_name('Button').click()

    time.sleep(3)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()