from UrbanRoutesPageLocators import UrbanRoutesPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPageMethods:

    def __init__(self, driver):
        self.driver = driver
        self.locators = UrbanRoutesPageLocators
        self.wait = WebDriverWait(driver, 10)

    def set_from(self, from_address):
        self.driver.find_element(*self.locators.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.locators.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.locators.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.locators.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def wait_for_home_page(self):
        return self.wait.until(EC.presence_of_element_located(self.locators.home_page))

    def wait_for_call_taxi(self):
        return self.wait.until(EC.visibility_of_element_located(self.locators.call_taxi))

    def wait_for_tariff_cards(self):
        return self.wait.until(EC.visibility_of_element_located(self.locators.tariff_cards))