from selenium.webdriver.common.by import By
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
    pay_method_field = (
        By.CLASS_NAME,
        "pp-button"
    )

    pay_method_modal = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]'
    )

    input_card_number = (
        By.XPATH,
        "//input[@placeholder='1234 4321 1408']"
    )

    input_cvv = (
        By.XPATH,
        "//input[@placeholder='12']"
    )

    plc_foco = (
        By.CLASS_NAME,
        "plc"
    )

    add_btn = (
        By.XPATH,
        "//button[text()='Agregar']"
    )

    activate_modal = (
        By.CLASS_NAME,
        "head"
    )

    card_checkmark = (
        By.ID,
        "card-1"
    )

    close_modal_btn = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/div[1]/button'
    )

    pay_method =(
        By.XPATH, "//div[@class='pp-value-text']"
    )

# ──────────────── LOCALIZADORES TEST CASE 5 ────────────────
    message_for_driver_field = (
        By.ID,
        "comment"
    )

# ──────────────── LOCALIZADORES TEST CASE 6 ────────────────
    blanket_and_tissues_switch = (
        By.CSS_SELECTOR,
        "input.switch-input"
    )

    blanket_class = (
        By.CSS_SELECTOR,
        "div.switch > span.slider.round")

# ──────────────── LOCALIZADORES TEST CASE 7 ────────────────
    ice_cream_container = (
        By.CSS_SELECTOR,
        '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div'
    )
    increment_ice_cream = (
        By.XPATH,
        '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]'
    )

    ice_cream_counter = (
        By.XPATH,
        '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]'
    )

# ──────────────── LOCALIZADORES TEST CASE 8 ────────────────
    order_taxi_button = (
        By.XPATH,
        '//*[@id="root"]/div/div[3]/div[4]/button/span[1]'
    )

    search_taxi_modal = (
        By.XPATH,
        '//*[@id="root"]/div/div[5]/div[2]/div[1]/div/div[2]'
    )

# ──────────────── LOCALIZADORES TEST CASE 9 ────────────────
    driver_modal = (
        By.CLASS_NAME,
        "order-body"
    )

    arrival_time = (
        By.CSS_SELECTOR,
        "div.order-header-title"
    )

    driver_name = (
        By.CLASS_NAME, "order-button"
    )

    vehicle_plate = (
        By.CLASS_NAME,
        "order-number"
    )

    cancel_button = (
        By.XPATH,
        "//div[contains(text(), 'Cancelar')]/preceding-sibling::button"
    )

    details_button = (
        By.XPATH,
        "//div[contains(text(), 'Detalles')]/preceding-sibling::button"
    )





