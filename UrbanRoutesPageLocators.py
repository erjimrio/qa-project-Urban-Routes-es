from selenium.webdriver.common.by import By

class UrbanRoutesPageLocators:
    from_field = (By.ID, "from")
    to_field = (By.ID, "to")
    home_page = (By.CLASS_NAME, "dst-picker-row")
    call_taxi = (By.XPATH, "//button[contains(text(), 'Pedir un taxi')]")
    tariff_cards = (By.CSS_SELECTOR, ".tariff-cards")
    comfort_tariff_icon = (By.XPATH, "//img[@alt='Comfort']")
    comfort_tariff_active = (By.XPATH, "//button[@data-for='tariff-card-4' and contains(@class, 'active')]")
    phone_number_field = (By.XPATH, "//div[contains(@class, 'np-button') and .//div[text()='Número de teléfono']]")
    modal_phone_number_field = (By.ID, "phone")
    modal_next_button = (By.CSS_SELECTOR, "#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button")

