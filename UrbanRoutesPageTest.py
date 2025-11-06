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

    def test_set_route(self):
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    @classmethod
    def teardown_class(cls):
        # borrar cookies
        cls.driver.delete_all_cookies()
        # Cierra el navegador
        cls.driver.quit()
