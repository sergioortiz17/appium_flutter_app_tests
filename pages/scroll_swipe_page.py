from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.actions.interaction import Interaction
import time

class ScrollSwipePage:
    def __init__(self, driver):
        self.driver = driver


class ScrollSwipePage:
    def __init__(self, driver):
        self.driver = driver

    def find_and_click(self, text):
        """Intenta encontrar un elemento con el texto dado y hacer click"""
        try:
            # 🔹 Intento 1: Buscar con ACCESSIBILITY_ID
            el = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, text)
            el.click()
            print(f"✅ Click en elemento con ACCESSIBILITY_ID: {text}")
            return
        except NoSuchElementException:
            print(f"⚠ No encontrado con ACCESSIBILITY_ID: {text}")

        try:
            # 🔹 Intento 2: Buscar con XPATH por nombre exacto
            el = self.driver.find_element(AppiumBy.XPATH, f'//XCUIElementTypeStaticText[@name="{text}"]')
            el.click()
            print(f"✅ Click en elemento con XPATH: {text}")
            return
        except NoSuchElementException:
            print(f"⚠ No encontrado con XPATH: {text}")

        try:
            # 🔹 Intento 3: Buscar cualquier elemento que contenga el texto (versión flexible)
            el = self.driver.find_element(AppiumBy.XPATH, f'//*[contains(@name, "{text}")]')
            el.click()
            print(f"✅ Click en elemento que contiene texto: {text}")
            return
        except NoSuchElementException:
            print(f"❌ No se encontró el elemento con texto: {text}")

        raise NoSuchElementException(f"No se encontró el elemento con texto: {text}")

    def access_scroll_swipe(self):
        """Accede a la funcionalidad 'Scroll & Swipe & Grid' con detección automática"""
        time.sleep(2)  # Esperar un poco para que la pantalla cargue
        self.find_and_click("Scrool & Swipe & Grid")


        time.sleep(1)  # Espera corta para estabilidad

    def perform_swipe(self):
        """Realiza un swipe lateral en la pantalla"""
        finger = PointerInput(PointerInput.KIND_TOUCH, "finger")
        action = ActionBuilder(self.driver, mouse=finger)

        start_x, start_y = 324, 225
        end_x, end_y = 116, 225

        action.pointer_action.move_to_location(start_x, start_y)
        action.pointer_action.pointer_down()
        action.pointer_action.move_to_location(end_x, end_y)
        action.pointer_action.pointer_up()
        action.perform()

        time.sleep(1)  # Espera corta para estabilidad

    def select_middle_option(self):
        """Selecciona la opción del 50%"""
        el2 = self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@value=\"50%\"]")
        el2.click()
        time.sleep(1)

    def enter_store(self):
        """Accede a la tienda"""
        el3 = self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeApplication[@name=\"NinjaSDET\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeScrollView")
        el3.click()
        el4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Tienda")
        el4.click()
        time.sleep(2)

    def go_back_twice(self):
        """Presiona el botón Back dos veces para salir"""
        el5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Back")
        el5.click()
        time.sleep(1)
        el6 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Back")
        el6.click()
        time.sleep(1)
