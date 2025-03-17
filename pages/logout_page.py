import time
from appium.webdriver.common.appiumby import AppiumBy

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        """Cierra la sesión en la aplicación"""
        try:
            el1 = self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeApplication[@name=\"NinjaSDET\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeButton")
            el1.click()
            time.sleep(1)

            el2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Cerrar sesión")
            el2.click()
            time.sleep(2)

            print("✅ Sesión cerrada exitosamente")
        except Exception as e:
            print(f"⚠ No se pudo cerrar sesión: {e}")
