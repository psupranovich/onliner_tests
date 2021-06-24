from selenium.webdriver.common.by import By


class MainPageLocators():
    CATALOG = (By.LINK_TEXT, "Каталог")

class CatalogLocators():
    DOM = (By.CSS_SELECTOR, ".g-middle-i .catalog-navigation-classifier:nth-child(4) [data-id='5']")
    DACHA = (By.CSS_SELECTOR, "div:nth-of-type(5) > .catalog-navigation-list__aside > div > div:nth-of-type(7) > .catalog-navigation-list__aside-title")
    POOL = (By.LINK_TEXT, "Бассейны")