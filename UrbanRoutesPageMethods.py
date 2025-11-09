from selenium.common import TimeoutException
from UrbanRoutesPageLocators import UrbanRoutesPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class UrbanRoutesPageMethods:

    def __init__(self, driver):
        self.driver = driver
        self.locators = UrbanRoutesPageLocators
        self.wait = WebDriverWait(driver, 10)

    # ──────────────── MÉTODOS DE SETUP ────────────────
    # Métodos individuales
    def set_from(self, from_address):
        self.driver.find_element(*self.locators.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.locators.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.locators.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.locators.to_field).get_property('value')

    def wait_for_home_page(self):
        return self.wait.until(
            EC.presence_of_element_located(self.locators.home_page)
        )

    # ──────────────── MÉTODOS DE SETUP ────────────────
    # Método compuesto
    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    # ──────────────── TEST CASE 2 ────────────────
    # Métodos individuales
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
        element = self.wait.until(
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

    # Métodos compuestos
    # Encapsula los métodos para seleccionar tarifa comfort
    def select_comfort_tariff(self):
        # Hace clic en el botón pedir taxi
        self.call_taxi()
        # Espera a que se muestren las tarifas
        self.wait_for_tariff_cards()
        # Selecciona la tarifa comfort
        self.set_comfort_tariff()

    # ──────────────── TEST CASE 3 ────────────────
    # Métodos individuales
    def select_phone_number_field(self):
        self.driver.find_element(*self.locators.phone_number_field).click()

    def wait_modal_phone_number(self):
        # Esperar a que el campo en el modal, esté visible
        self.wait.until(
            EC.visibility_of_element_located(self.locators.modal_phone_number_field)
        )

    def insert_phone_number(self, phone_number):
        self.driver.find_element(*self.locators.modal_phone_number_field).send_keys(phone_number)

    def clic_next(self):
        self.driver.find_element(*self.locators.modal_next_button).click()

    def wait_insert_sms_code(self):
        self.wait.until(
            EC.visibility_of_element_located(self.locators.modal_sms_code)
        )

    def insert_sms_code(self, sms_code):
        self.driver.find_element(*self.locators.modal_sms_code).send_keys(sms_code)

    def clic_confirm(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.modal_sms_confirm)).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.locators.phone_number_registered).text.strip()

    # Métodos compuestos
    # Encapsula los métodos para insertar el número de teléfono
    def fill_phone_number (self, phone_number) :
        # Selecciona el campo Número de teléfono
        self.select_phone_number_field()
        # Espera a que se abra el modal del número de teléfono
        self.wait_modal_phone_number()
        # Escribe el número de teléfono
        self.insert_phone_number(phone_number)
        # Oprime botón siguiente
        self.clic_next()
        # Espera a que el campo "Introduce el código" esté visible
        self.wait_insert_sms_code()

    def confirm_sms_code(self, sms_code):
        # Inserta el código SMS
        self.insert_sms_code(sms_code)
        # Oprime botón confirmar
        self.clic_confirm()

    # ──────────────── TEST CASE 4 ────────────────
    # Métodos individuales
    def select_pay_method(self):
        self.driver.find_element(*self.locators.pay_method_field).click()

    def select_pay_method_modal(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.locators.pay_method_modal)
        )
        element.click()

    def insert_card_number(self, tc_number):
        self.driver.find_element(*self.locators.input_card_number).send_keys(tc_number)

    def insert_code(self, card_code):
        self.driver.find_element(*self.locators.input_cvv).send_keys(card_code)

    def change_focus(self):
        self.driver.find_element(*self.locators.plc_foco).click()

    def click_add_button(self):
        self.driver.find_element(*self.locators.add_btn).click()

    def close_pay_method_modal(self):
        self.driver.find_element(*self.locators.close_modal_btn).click()

    def pay_method(self):
        pay_method = self.driver.find_element(*self.locators.pay_method)
        return pay_method.text.strip()

# Métodos compuestos
    def activate_pay_method_modal(self):
        modal_trigger = self.driver.find_element(*self.locators.activate_modal)

        # Forzar clic con JavaScript si no está utilizable
        if not modal_trigger.is_displayed() or not modal_trigger.is_enabled():
            #print("⚠️ Elemento no está utilizable, usando JavaScript para forzar clic.")
            self.driver.execute_script("arguments[0].click();", modal_trigger)
        else:
            modal_trigger.click()

        elements = self.driver.find_elements(*self.locators.card_checkmark)
        if elements:
            print("✅ La tarjeta está presente en el DOM")
        else:
            print("❌ La tarjeta no está en el DOM")

    def insert_credit_card(self, tc_number, cvv_code):
        # Selecciona el campo forma de pago
        self.select_pay_method()
        # Clic en agregar tarjeta de crédito
        self.select_pay_method_modal()
        # Ingresa el número de tarjeta de crédito
        self.insert_card_number(tc_number)
        # Inserta el número de código de la tarjeta
        self.insert_code(cvv_code)
        # Cambia el foco
        self.change_focus()
        # Click en Agregar
        self.click_add_button()
        # Activa el modal
        self.activate_pay_method_modal()
        # Cierra el modal y regresa a la página principal
        self.close_pay_method_modal()

    # ──────────────── TEST CASE 5 ────────────────
    # Métodos individuales
    def insert_message(self, message):
        driver_message = self.wait.until(
            EC.element_to_be_clickable(self.locators.message_for_driver_field)
        )
        # Envía el número de tarjeta
        driver_message.send_keys(message)
    def get_message(self):
        message_registered = self.driver.find_element(*self.locators.message_for_driver_field).get_attribute("value")
        return message_registered

    # ──────────────── TEST CASE 6 ────────────────
    # Métodos individuales
    def ask_for_a_blanket_and_tissues(self):
        checkbox = self.driver.find_element(*self.locators.blanket_and_tissues_switch)

        # Cambiar el estado del checkbox manualmente
        self.driver.execute_script("""
            const el = arguments[0];
            el.checked = !el.checked;

            // Disparar evento 'change' para que el frontend actualice la UI
            el.dispatchEvent(new Event('change', { bubbles: true }));
        """, checkbox)

    def is_blanket_tissue_switch_on(self):
        toggle_switch = self.driver.find_element(*self.locators.blanket_and_tissues_switch)
        return toggle_switch.is_selected()

    # ──────────────── TEST CASE 7 ────────────────
    # Métodos individuales
    def ask_for_ice_creams(self, quantity):
        for _ in range (quantity):
            self.driver.find_element(*self.locators.increment_ice_cream).click()

    def get_ice_cream_quantity(self):
        ice_cream_counter = self.driver.find_element(*self.locators.ice_cream_counter)
        return int(ice_cream_counter.text)

    # ──────────────── TEST CASE 8 ────────────────
    # Métodos individuales
    def order_taxi_button(self):
        taxi_button = self.wait.until(
            EC.element_to_be_clickable(self.locators.order_taxi_button)
        )
        taxi_button.click()

    def is_taxi_modal_visible(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.locators.search_taxi_modal)
            )
            return True
        except TimeoutException:
            return False