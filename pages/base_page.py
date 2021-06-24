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
        sleep(1)
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def switch_to_frame(self, locator, time=10):
        WebDriverWait(self.driver, time).until(EC.frame_to_be_available_and_switch_to_it(locator),
                                               message=f"Can't find frame by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def click_element(self, locator):
        return self.find_element(locator).click()

    def send_key(self, locator, key):
        input_box = self.find_element(locator)
        self.driver.execute_script('arguments[0].value=arguments[1]', input_box, key)
        input_box.click()



