import time
from appium.webdriver.common.appiumby import AppiumBy

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def open_register_screen(self):
        """Accede a la pantalla de registro"""
        el1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Registra tu usuario aquí")
        el1.click()
        time.sleep(1)

    def enter_username(self, username):
        """Ingresa el nombre de usuario"""
        el2 = self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeTextField")
        el2.send_keys(username)

    def enter_password(self, password):
        """Ingresa la contraseña"""
        el4 = self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeApplication[@name=\"NinjaSDET\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]")
        el4.send_keys(password)

    def confirm_password(self, password):
        """Confirma la contraseña"""
        el5 = self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeApplication[@name=\"NinjaSDET\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[4]")
        el5.send_keys(password)

    def activate_switches(self):
        """Activa las opciones necesarias"""
        el8 = self.driver.find_element(AppiumBy.XPATH, "(//XCUIElementTypeSwitch[@value=\"0\"])[1]")
        el8.click()
        el9 = self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSwitch[@value=\"0\"]")
        el9.click()

    def click_create_user(self):
        """Presiona el botón de crear usuario"""
        el10 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Crear user")
        el10.click()
        time.sleep(2)

    def enter_login_username(self, username):
        """Ingresa el usuario en el login"""
        el11 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Usuario")
        el11.send_keys(username)
        time.sleep(2)

    def enter_login_password(self, password):
        """Ingresa la contraseña en el login"""
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Contraseña").send_keys(password)
        time.sleep(2)

    def click_login(self):
        """Presiona el botón de ingresar"""
        el13 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Ingresar")
        el13.click()
        time.sleep(2)
