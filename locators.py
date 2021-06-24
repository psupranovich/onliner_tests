from selenium.webdriver.common.by import By


class MainPageLocators():
    CATALOG = (By.LINK_TEXT, "Каталог")


class CatalogLocators():
    DOM = (By.CSS_SELECTOR, ".g-middle-i .catalog-navigation-classifier:nth-child(4) [data-id='5']")
    DACHA = (By.CSS_SELECTOR, "div:nth-of-type(5) > .catalog-navigation-list__aside > div > div:nth-of-type(7) > "
                              ".catalog-navigation-list__aside-title")
    POOL = (By.PARTIAL_LINK_TEXT, "Бассейны")
    SEARCH = (By.CSS_SELECTOR, "input.fast-search__input")


class PoolsLocators():
    POOL_NAME = (By.PARTIAL_LINK_TEXT, "Надувной бассейн Bestway Солнечный 54321 (305x274x46)")
    PRICE = (By.XPATH, '//*[@id="schema-products"]/div[1]/div/div[3]/div[1]/div/div/div[1]/div[1]/a/span')


class FrameLocators():
    FRAME_PRICE = (By.XPATH,
                   '//*[@id="search-page"]/div[2]/ul/li/div/div/div[1]/div/div/a/span')

    FRAME = (By.CLASS_NAME, 'modal-iframe')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input.fast-search__input')