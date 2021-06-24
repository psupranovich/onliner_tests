from onliner_tests.locators import MainPageLocators, CatalogLocators, PoolsLocators, FrameLocators
from onliner_tests.pages.base_page import BasePage



class Catalog(BasePage):

    def open_page_button(self):
        return self.click_element(MainPageLocators.CATALOG)

    def click_dom_page(self):
        return self.click_element(CatalogLocators.DOM)

    def click_dacha_element(self):
        return self.click_element(CatalogLocators.DACHA)

    def click_pool_link(self):
        return self.click_element(CatalogLocators.POOL)

    def find_product(self):
        return self.find_element(PoolsLocators.POOL_NAME)

    def find_poduct_price(self):
        return self.find_element(PoolsLocators.PRICE)

    def find_item_mini(self, product):
        return self.send_key(CatalogLocators.SEARCH, product)

    def find_item(self, product):
        return self.send_key(FrameLocators.SEARCH_INPUT, product)

    def go_to_frame(self):
        return self.switch_to_frame(FrameLocators.FRAME)

    def find_frame_price(self):
        return self.find_element(FrameLocators.FRAME_PRICE)



