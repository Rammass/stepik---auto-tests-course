import math
import time
import pytest

from selenium import webdriver


LINK_LIST = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]


@pytest.fixture(autouse=True)
def browser():
    br = webdriver.Chrome()
    yield br
    br.quit()


@pytest.mark.parametrize('link', LINK_LIST)
def test_ufo(browser, link):
    browser.get(link)
    browser.find_element_by_tag_name('textarea').sendtext()