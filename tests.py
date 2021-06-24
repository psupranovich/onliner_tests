import time
import unittest
from  onliner_pages.catalog import Catalog

from selenium import webdriver


class Setup(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()


class TestSampleApp(Setup):

    def test_users_can_open_the_catalog_page(self):
        self.page = Catalog(self.driver)
        self.page.go_to_site()
        self.page.open_page_button()
        self.assertEqual(self.driver.title, 'Каталог Onliner')
        self.page.click_dom_page()
        self.page.click_dacha_element()
        self.page.click_pool_link()
        time.sleep(10)


