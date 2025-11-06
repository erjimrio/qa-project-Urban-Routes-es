from selenium.webdriver.common.by import By

class UrbanRoutesPageLocators:
    from_field = (By.ID, "from")
    to_field = (By.ID, "to")
    home_page = (By.CLASS_NAME, "dst-picker-row")
    call_taxi = (By.XPATH, "//button[contains(text(), 'Pedir un taxi')]")
    tariff_cards = (By.CSS_SELECTOR, ".tariff-cards")

