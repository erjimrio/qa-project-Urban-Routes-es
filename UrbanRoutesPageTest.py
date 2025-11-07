import data
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
        homePage = cls.routes_page.wait_for_home_page()
        # Se establece la ruta en la instancia routes_page
        cls.routes_page.set_route(address_from, address_to)
        # Esperar a que el botón "Pedir taxi" sea visible
        taxi = cls.routes_page.wait_for_call_taxi()

# Prueba 1 - Configurar la direccón

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
        # Selecciona el campo Número de teléfono
        self.routes_page.select_phone_number_field()
        # Espera a que se abra el modal del número de teléfono
        self.routes_page.wait_modal_phone_number()
        # Escribe el número de teléfono
        self.routes_page.insert_phone_number()
        # Oprime botón siguiente
        self.routes_page.clic_next()


    @classmethod
    def teardown_class(cls):
        # borrar cookies
        cls.driver.delete_all_cookies()
        # Cierra el navegador
        cls.driver.quit()
