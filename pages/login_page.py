# login_page.py
from appium.webdriver.common.appiumby import AppiumBy
from utils.appium_driver import get_driver

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Usuario").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Contraseña").send_keys(password)

    def click_login(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Ingresar").click()
    
    def get_welcome_message(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "¡Hola, bienvenido!").text
