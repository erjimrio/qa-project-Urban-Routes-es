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

    # Paso que encapsula los métodos para insertar el número de teléfono
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

    def select_pay_method(self):
        self.driver.find_element(*self.locators.pay_method_field).click()

    def select_pay_method_modal(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.locators.pay_method_modal)
        )
        element.click()

    def insert_card_number(self, tc_number):
        tc = self.wait.until(
            EC.element_to_be_clickable(self.locators.tc_number_field)
        )
        # Envía el número de tarjeta
        tc.send_keys(tc_number)
        # Simula que el usuario presiona TAB para pasar al campo CVV
        tc.send_keys(Keys.TAB)
        # Verificar foco actual (debería estar en el campo CVV)
        active = self.driver.execute_script("return document.activeElement")
        print("Foco después de TAB desde número:", active.get_attribute("id"))

    def insert_code_debug(self, card_code):
        """
        Método de diagnóstico para insertar CVV en el campo 'code'.
        Usa JavaScript para imprimir en consola:
        - Visibilidad del campo
        - Valor insertado
        - Estado del botón 'Agregar'
        - Clic en el modal contenedor
        """
        overlay_elements = self.driver.find_elements(*self.locators.overlay_blocker)
        if overlay_elements:
            self.wait.until(EC.invisibility_of_element_located(self.locators.overlay_blocker))

        # Esperar el campo CVV
        code_field = self.wait.until(
            EC.presence_of_element_located(self.locators.tc_code_field)
        )

        # Scroll al campo
        self.driver.execute_script("arguments[0].scrollIntoView(true);", code_field)

        # Imprimir en consola si el campo está visible
        self.driver.execute_script("""
            const el = arguments[0];
            console.log("Campo CVV encontrado:", el);
            console.log("Display:", window.getComputedStyle(el).display);
            console.log("Visibility:", window.getComputedStyle(el).visibility);
            console.log("Opacity:", window.getComputedStyle(el).opacity);
        """, code_field)

        # Insertar el valor con JS (evita errores de interacción)
        self.driver.execute_script("arguments[0].value = arguments[1];", code_field, card_code)
        self.driver.execute_script("console.log('CVV insertado:', arguments[0].value);", code_field)

        # Clic en el modal contenedor usando JS
        modal_container = self.driver.find_element(*self.locators.modal_container)
        self.driver.execute_script("console.log('Modal contenedor:', arguments[0]);", modal_container)
        self.driver.execute_script("arguments[0].click();", modal_container)

        # Verificar si el botón Agregar está habilitado
        add_button = self.driver.find_element(*self.locators.add_button)
        is_enabled = add_button.is_enabled()
        self.driver.execute_script("console.log('Botón Agregar habilitado:', arguments[0]);", is_enabled)

    def insert_code(self, card_code):
        # Espera si hay overlay
        overlay_elements = self.driver.find_elements(*self.locators.overlay_blocker)
        if overlay_elements:
            self.wait.until(EC.invisibility_of_element_located(self.locators.overlay_blocker))

        # Espera la presencia del campo CVV
        code_field = self.wait.until(
            EC.presence_of_element_located(self.locators.tc_code_field)
        )

        # Scroll y foco
        self.driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].focus();", code_field)

        try:
            # Intentar con send_keys
            code_field.clear()
            code_field.send_keys(card_code)
        except Exception:
            # Fallback: usar JS si no es interactuable
            self.driver.execute_script("""
                const el = arguments[0];
                el.value = arguments[1];
                el.dispatchEvent(new Event('input', { bubbles: true }));
                el.dispatchEvent(new Event('change', { bubbles: true }));
                el.dispatchEvent(new Event('blur', { bubbles: true }));
            """, code_field, card_code)

        # Validar que el botón Agregar se habilitó
        add_button = self.driver.find_element(*self.locators.add_button)
        self.wait.until(lambda d: d.find_element(*self.locators.add_button).is_enabled())

    def insert_message(self, message):
        driver_message = self.wait.until(
            EC.element_to_be_clickable(self.locators.message_for_driver_field)
        )
        # Envía el número de tarjeta
        driver_message.send_keys(message)
    def get_message(self):
        message_registered = self.driver.find_element(*self.locators.message_for_driver_field).get_attribute("value")
        return message_registered

