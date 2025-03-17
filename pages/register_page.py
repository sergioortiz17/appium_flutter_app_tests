import time
from appium.webdriver.common.appiumby import AppiumBy

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def open_register_screen(self):
        """Accede a la pantalla de registro"""
        register_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Registra tu usuario aquí")
        register_button.click()
        time.sleep(1)

    def enter_username(self, username):
        """Ingresa el nombre de usuario"""
        username_field = self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeTextField")
        username_field.send_keys(username)

    def enter_password(self, password):
        """Ingresa la contraseña"""
        password_field = self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeApplication[@name=\"NinjaSDET\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]")
        password_field.send_keys(password)

    def confirm_password(self, password):
        """Confirma la contraseña"""
        confirm_password_field = self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeApplication[@name=\"NinjaSDET\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[4]")
        confirm_password_field.send_keys(password)

    def activate_switches(self):
        """Activa las opciones necesarias"""
        human_verification_switch = self.driver.find_element(AppiumBy.XPATH, "(//XCUIElementTypeSwitch[@value=\"0\"])[1]")
        human_verification_switch.click()
        
        terms_conditions_switch = self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSwitch[@value=\"0\"]")
        terms_conditions_switch.click()

    def click_create_user(self):
        """Presiona el botón de crear usuario"""
        create_user_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Crear user")
        create_user_button.click()
        time.sleep(2)

    def enter_login_username(self, username):
        """Ingresa el usuario en el login"""
        login_username_field = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Usuario")
        login_username_field.send_keys(username)
        time.sleep(2)

    def enter_login_password(self, password):
        """Ingresa la contraseña en el login"""
        login_password_field = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Contraseña")
        login_password_field.send_keys(password)
        time.sleep(2)

    def click_login(self):
        """Presiona el botón de ingresar"""
        login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Ingresar")
        login_button.click()
        time.sleep(2)
