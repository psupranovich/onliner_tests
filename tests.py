import time
import unittest

import allure
from selenium import webdriver

from onliner_tests.pages.catalog import Catalog

class Setup(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.get_window_size('current')

    def tearDown(self) -> None:
        self.driver.quit()


class TestSampleApp(Setup):
    @allure.feature('UI_PlayGround')
    @allure.story('Sample app test')
    def test_ptrice_on_the_page_and_on_the_frame_is_the_same(self):
        self.page = Catalog(self.driver)
        with allure.step('Open site'):
            self.page.go_to_site()

        with allure.step('Open catalog'):
            self.page.open_page_button()
            self.assertEqual(self.driver.title, 'Каталог Onliner')
        with allure.step('Find category pool'):
            self.page.click_dom_page()
            self.page.click_dacha_element()
            self.page.click_pool_link()
        with allure.step('Find and save prise of the first item'):
            product = str(self.page.find_product().text)
            product_price = self.page.find_poduct_price().text
            product_price = product_price.partition(',')[0]
        with allure.step('Search on frame'):
            self.page.find_item(product)
            self.page.go_to_frame()
            new_price = self.page.find_frame_price().text
            new_price = new_price.partition(',')[0]
            assert product_price == new_price



