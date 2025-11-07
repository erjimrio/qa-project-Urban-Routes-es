from selenium.common import TimeoutException

import data
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
        return self.wait.until(
            EC.presence_of_element_located(self.locators.home_page)
        )

    def wait_for_call_taxi(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.locators.call_taxi)
        )

    def call_taxi(self):
        self.driver.find_element(*self.locators.call_taxi).click()

    def wait_for_tariff_cards(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.locators.tariff_cards)
        )

    def set_comfort_tariff(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.comfort_tariff_icon))
        element.click()

    def is_comfort_tariff_selected(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.locators.comfort_tariff_active)
            )
            return element.is_displayed()
        except TimeoutException:
            return False

    # Paso que encapsula los métodos para seleccionar tarifa comfort

    def select_comfort_tariff(self):
        # Hace clic en el botón pedir taxi
        self.call_taxi()
        # Espera a que se muestren las tarifas
        self.wait_for_tariff_cards()
        # Selecciona la tarifa comfort
        self.set_comfort_tariff()

    def select_phone_number_field(self):
        self.driver.find_element(*self.locators.phone_number_field).click()

    def wait_modal_phone_number(self):
        # Esperar a que el campo en el modal, esté visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.modal_phone_number_field)
        )

    def insert_phone_number(self):
        self.driver.find_element(*self.locators.modal_phone_number_field).send_keys(data.phone_number)

    def clic_next(self):
        self.driver.find_element(*self.locators.modal_next_button).click()