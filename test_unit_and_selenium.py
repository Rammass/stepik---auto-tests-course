import time
import unittest

from selenium import webdriver

class TestPage(unittest.TestCase):

    def test_fst_page(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element_by_xpath('//input[@placeholder="Input your first name"]').send_keys('Ivan')
        browser.find_element_by_xpath('//input[@placeholder="Input your last name"]').send_keys('Ivan')
        browser.find_element_by_xpath('//input[@placeholder="Input your address:"]').send_keys('Ivan')
        browser.find_element_by_xpath('//input[@placeholder="Input your phone:"]').send_keys('Ivan')
        browser.find_element_by_xpath('//input[@placeholder="Input your email"]').send_keys('Ivan')
        browser.find_element_by_tag_name('button').click()

        self.assertEqual(
            browser.find_element_by_tag_name('h1').text,
            'Congratulations! You have successfully registered!',
            'Ooops!'
        )

    def test_snd_page(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element_by_xpath('//input[@placeholder="Input your first name"]').send_keys('Ivan')
        browser.find_element_by_xpath('//input[@placeholder="Input your last name"]').send_keys('Ivan')
        browser.find_element_by_xpath('//input[@placeholder="Input your address:"]').send_keys('Ivan')
        browser.find_element_by_xpath('//input[@placeholder="Input your phone:"]').send_keys('Ivan')
        browser.find_element_by_xpath('//input[@placeholder="Input your email"]').send_keys('Ivan')
        browser.find_element_by_tag_name('button').click()

        self.assertEqual(
            browser.find_element_by_tag_name('h1').text,
            'Congratulations! You have successfully registered!',
            'Ooops!'
        )


if __name__ == "__main__":
    unittest.main()