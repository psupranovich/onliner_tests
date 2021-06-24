
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://onliner.by/"

    def find_element(self, locator, time=16):
        sleep(1)
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")


    def go_to_site(self):
        return self.driver.get(self.base_url)

    def click_element(self, locator):
        return self.find_element(locator).click()

    def send_key(self, key, locator):
        return self.find_element(locator).send_keys(key)

