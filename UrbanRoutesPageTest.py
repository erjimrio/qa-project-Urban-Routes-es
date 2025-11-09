import data
from time import sleep
from sms_code import retrieve_phone_code
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from UrbanRoutesPageMethods import UrbanRoutesPageMethods

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):

        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        # Se adaptó esta sección debido a que hubo una actualización en Selenium 4
        options = Options()
        # Activar logs de rendimiento (performance logs)
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        # Inicializar Chrome con esas opciones
        cls.driver = webdriver.Chrome(options=options)

        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPageMethods(cls.driver)
        address_from = data.address_from
        address_to = data.address_to
        # Espera a que se cargue la pagina Urban Routes
        homepage = cls.routes_page.wait_for_home_page()
        # Se establece la ruta en la instancia routes_page
        cls.routes_page.set_route(address_from, address_to)
        # Esperar a que el botón "Pedir taxi" sea visible
        taxi = cls.routes_page.wait_for_call_taxi()

# Prueba 1 - Configurar la dirección

    def test_set_route(self):
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

# Prueba 2 - Seleccionar la tarifa comfort

    def test_select_comfort_tariff(self):
        self.routes_page.select_comfort_tariff()
        # Validación: ¿la tarifa Comfort quedó seleccionada?
        assert self.routes_page.is_comfort_tariff_selected(), "La tarifa Comfort no quedó seleccionada"

# Prueba 3 - Rellenar el número de teléfono

    def test_fill_phone_number(self):
        phone_number = data.phone_number
        self.routes_page.fill_phone_number(phone_number)
        # Obtiene el código SMS
        sms_code = retrieve_phone_code(self.routes_page.driver)
        # Inserta y confirma el código SMS
        self.routes_page.confirm_sms_code(sms_code)
        # Verifica que el número de teléfono en el archivo data coincida con el mostrado en el campo numero de teléfono
        numero_registrado = self.routes_page.get_phone_number()
        assert numero_registrado == phone_number

# Prueba 4 - Agregar una tarjeta de crédito
    def test_insert_credit_card(self):
        tc_number = data.card_number
        cvv_code = data.card_code
        self.routes_page.insert_credit_card(tc_number, cvv_code)
        # Verifica que el método de pago sea tarjeta
        pay_method = self.routes_page.pay_method()
        assert pay_method == "Tarjeta"

# Prueba 5 - Escribir un mensaje para el conductor
    def test_send_message(self):
        message = data.message_for_driver
        # Inserta el mensaje para el conductor
        self.routes_page.insert_message(message)
        # Obtiene el mensaje escrito en el campo Mensaje para el conductor
        message_displayed = self.routes_page.get_message()
        # Verifica que el mensaje escrito coincida con el mensaje que se importó del archivo data
        assert message_displayed == message

# Prueba 6 - Pedir una manta y pañuelos
    def test_ask_for_a_blanket_and_tissues(self):
        self.routes_page.ask_for_a_blanket_and_tissues()
        assert self.routes_page.is_blanket_tissue_switch_on()

# Prueba 7 - Pedir 2 helados
    def test_ask_for_ice_creams(self):
        ice_cream = data.ice_creams # 2 helados en este caso
        # Se piden los helados
        self.routes_page.ask_for_ice_creams(ice_cream)
        # Obtiene el valor del contador de helados en la página UrbanRoutes
        ice_cream_counter = self.routes_page.get_ice_cream_quantity()
        # Compara el número de helados del archivo data.py con los que marca la página de UrbanRoutes
        assert ice_cream_counter == ice_cream

# Prueba 8 - Aparece el modal para pedir un taxi
    def test_order_taxi_modal(self):
        self.routes_page.order_taxi_button()
        assert self.routes_page.wait_for_taxi_modal_and_transition()
        sleep(30)

# Prueba 9 - Esperar a que aparezca la información del conductor
    def test_driver_information_modal_appears(self):
        # Espera que termine el timer que busca conductor
        #self.routes_page.wait_for_driver_modal()

        resultado = self.routes_page.validate_driver_modal_information()
        assert resultado is None, resultado

    @classmethod
    def teardown_class(cls):
        # borrar cookies
        cls.driver.delete_all_cookies()
        # Cierra el navegador
        cls.driver.quit()