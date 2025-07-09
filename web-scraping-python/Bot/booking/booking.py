
import booking.constants as const 
import os 
from selenium.webdriver.common.by import By 
from selenium import webdriver

class Booking(webdriver.Chrome):
    def __init__(self,driver_path=r"C:\proyectos\python\web-scraping-python\chromedriver-win64", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
       

    def land_first_page(self):
        self.get(const.BASE_URL)
        self.implicitly_wait(10)

    def change_currency(self, currency: str):  #clickea el primer boton de moneda
        currency_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]'
        )
        currency_element.click()

        self.implicitly_wait(10)

        selected_currency_element = self.find_element(
            By.CLASS_NAME, "CurrencyPicker_currency") #cambio a la moneda que le paso como parámetro en run
        if selected_currency_element.text.strip() == currency:   #busco en el div el texto "USD" y si coincide con el parámetro que le paso, entonces click
            selected_currency_element.click()
            return
        raise Exception(f"Currency '{currency}' not found.")


        