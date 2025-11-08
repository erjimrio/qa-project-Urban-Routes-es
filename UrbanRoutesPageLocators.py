from selenium.webdriver.common.by import By

from data import message_for_driver


class UrbanRoutesPageLocators:

# ──────────────── LOCALIZADORES SETUP ────────────────
    from_field = (
        By.ID,
        "from"
    )

    to_field = (
        By.ID,
        "to"
    )

    home_page = (
        By.CLASS_NAME,
        "dst-picker-row"
    )

# ──────────────── LOCALIZADORES TEST CASE 2 ────────────────
    call_taxi = (
        By.XPATH,
        "//button[contains(text(), 'Pedir un taxi')]"
    )

    tariff_cards = (
        By.CSS_SELECTOR,
        ".tariff-cards"
    )

    comfort_tariff_icon = (
        By.XPATH,
        "//img[@alt='Comfort']"
    )

    comfort_tariff_active = (
        By.XPATH,
        "//button[@data-for='tariff-card-4' and contains(@class, 'active')]"
    )

# ──────────────── LOCALIZADORES TEST CASE 3 ────────────────
    phone_number_field = (
        By.XPATH,
        "//div[contains(@class, 'np-button') and .//div[text()='Número de teléfono']]"
    )

    modal_phone_number_field = (
        By.ID,
        "phone"
    )

    modal_next_button = (
        By.CSS_SELECTOR,
        "#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button"
    )

    modal_sms_code = (
        By.ID,
        "code"
    )

    modal_sms_confirm = (
        By.XPATH,
        '//button[text()="Confirmar" and not(@disabled)]'
    )

    phone_number_registered = (
        By.XPATH,
        '//div[@class="np-button filled"]//div[@class="np-text"]'
    )

# ──────────────── LOCALIZADORES TEST CASE 4 ────────────────
    pay_method_field = (By.CLASS_NAME, "pp-button")
    pay_method_modal = (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]')
    tc_number_field = (By.ID, 'number')
    tc_code_field = (By.ID, "code")

# ──────────────── LOCALIZADORES TEST CASE 5 ────────────────
    message_for_driver_field = (
        By.ID,
        "comment"
    )

    blanket_and_tissues_switch = (
        By.CSS_SELECTOR,
        "input.switch-input"
    )

    increment_ice_cream = (
        By.XPATH,
        '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]'
    )

    ice_cream_counter = (
        By.XPATH,
        '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]'
    )

    order_taxi_button = (
        By.XPATH,
        '//*[@id="root"]/div/div[3]/div[4]/button/span[1]'
    )

    search_taxi_modal = (
        By.XPATH,
        '//*[@id="root"]/div/div[5]/div[2]/div[1]/div/div[2]'
    )




"""
    # Modal que contiene el campo CVV
    modal_container = (
        By.XPATH,
        "//div[contains(@class, 'modal') and .//input[@id='code']]"
    )

    # Botón Agregar (ajústalo si el selector es diferente)
    add_button = (By.XPATH, "//button[contains(text(), 'Agregar')]")

    # Overlay (si existe)
    overlay_blocker = (By.CLASS_NAME, "overlay")
"""

