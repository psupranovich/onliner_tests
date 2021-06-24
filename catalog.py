from .base_page import BasePage
from locators import MainPageLocators, CatalogLocators


class Catalog(BasePage):

    def open_page_button(self):
        return self.click_element(MainPageLocators.CATALOG)

    def click_dom_page(self):
        return  self.click_element(CatalogLocators.DOM)

    def click_dacha_element(self):
        return self.click_element(CatalogLocators.DACHA)

    def click_pool_link(self):
        return self.click_element(CatalogLocators.POOL)

