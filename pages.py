from unittest import expectedFailure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from helpers import retrieve_phone_code


class UrbanRoutesPage:
    # Seção De e Para
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Selecionar tarifa e botão de chamar taxi
    taxi_option_locator = (By.XPATH, '//button[contains(text(),"Chamar")]')
    comfort_icon_locator = (By.XPATH, '//img[@src="/static/media/kids.075fd8d4.svg"]')
    comfort_active = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')

    # Numero de telefone e codigo
    number_text_locator = (By.CSS_SELECTOR, '.np-button')
    number_enter = (By.ID, 'phone')
    number_confirm = (By.CSS_SELECTOR, '.button.full')
    number_code = (By.ID, 'code')
    code_confirm = (By.XPATH, '//button[contains(text(),"Confirmar")]')
    number_finish = (By.CSS_SELECTOR, '.np-text')

    # METODO DE PAGAMENTO
    add_metodo_pagamento = (By.CSS_SELECTOR, '.pp-button.filled')
    add_card = (By.CSS_SELECTOR, '.pp-plus')
    number_card = (By.ID, 'number')
    code_card = (By.CSS_SELECTOR, 'input.card-input#code')
    add_finish_card = (By.XPATH, '//button[contains(text(),"Adicionar")]')
    close_button_card = (By.CSS_SELECTOR, '.payment-picker.open .close-button')
    comfirm_card = (By.CSS_SELECTOR, '.pp-value-text')

    # ADICIONAR COMENTARIO
    add_comment = (By.ID, 'comment')

    # Pedir lenções e cobertor
    switch_blanket = (By.CSS_SELECTOR, '.switch')
    switch_blanket_active = (By.CSS_SELECTOR,
                             '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > input')

    # Pedir Sorvete
    add_icecream = (By.CSS_SELECTOR, '.counter-plus')
    qnt_icecream = (By.CSS_SELECTOR, '.counter-value')

    # Pedir Taxi
    call_taxi_button = (By.CSS_SELECTOR, '.smart-button')
    pop_up = (By.CSS_SELECTOR, '.order-header-title')

    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        WebDriverWait(self.driver, timeout=3).until(
            EC.visibility_of_element_located(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(from_text)

    def enter_to_location(self, to_text):
        WebDriverWait(self.driver, timeout=3).until(
           EC.visibility_of_element_located(self.to_field)
       )
        self.driver.find_element(*self.to_field).send_keys(to_text)

    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def get_from_location_value(self):
        return WebDriverWait(self.driver, timeout=3).until(
            EC.visibility_of_element_located(self.from_field)
        ).get_attribute('value')

    def get_to_location_value(self):
        return WebDriverWait(self.driver, timeout=3).until(
            EC.visibility_of_element_located(self.to_field)
        ).get_attribute('value')

    def click_taxi_buttom(self):
        self.driver.find_element(*self.taxi_option_locator).click()

    def click_comfort_buttom(self):
        self.driver.find_element(*self.comfort_icon_locator).click()

    def click_comfort_active(self):
        try:
            self.driver.find_element(*self.comfort_active).click()
            return True
        except Exception:
            return False

    def click_phone_field(self, telefone):
        self.driver.find_element(*self.number_text_locator).click()
        self.driver.find_element(*self.number_enter).send_keys(telefone)
        self.driver.find_element(*self.number_confirm).click()
        code = retrieve_phone_code(self.driver)
        put_code = WebDriverWait(self.driver, timeout=3).until(
            EC.visibility_of_element_located(self.number_code)
        )
        put_code.clear()
        put_code.send_keys(code)
        self.driver.find_element(*self.code_confirm).click()


    def config_number(self):
        number = WebDriverWait(self.driver, timeout=3).until(
            EC.visibility_of_element_located(self.number_finish)
        )
        return number.text

    def add_click_card(self,number,code):
        self.driver.find_element(*self.add_metodo_pagamento).click()
        self.driver.find_element(*self.add_card).click()
        time.sleep(1)
        self.driver.find_element(*self.number_card).send_keys(number)
        time.sleep(1)
        self.driver.find_element(*self.code_card).send_keys(code)
        time.sleep(1)
        self.driver.find_element(*self.add_finish_card).click()
        self.driver.find_element(*self.close_button_card).click()

    def confirm_card_number(self):
        return self.driver.find_element(*self.comfirm_card).text

    def add_comment_driver(self, comentario):
        self.driver.find_element(*self.add_comment).send_keys(comentario)

    def check_comment(self):
        return self.driver.find_element(*self.add_comment).get_attribute('value')

    def select_blankets(self):
        blankets_active = self.driver.find_element(*self.switch_blanket)
        blankets_active.click()

    def blankets_active(self):
        switch = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.switch_blanket_active))
        return switch.is_selected()

    def add_ice(self):
        self.driver.find_element(*self.add_icecream).click()

    def quantity_icecream(self):
        return self.driver.find_element(*self.qnt_icecream).text

    def call_taxi(self):
        self.driver.find_element(*self.call_taxi_button).click()

    def show_popup(self):
        pop_up = self.driver.find_element(*self.pop_up)
        return pop_up.text









