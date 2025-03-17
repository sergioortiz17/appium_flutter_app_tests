import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

class ScrollSwipePage:
    def __init__(self, driver):
        self.driver = driver

    def find_and_click(self, text):
        try:
            element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, text)
            element.click()
            return
        except NoSuchElementException:
            pass

        try:
            element = self.driver.find_element(AppiumBy.XPATH, f'//XCUIElementTypeStaticText[@name="{text}"]')
            element.click()
            return
        except NoSuchElementException:
            pass

        try:
            element = self.driver.find_element(AppiumBy.XPATH, f'//*[contains(@name, "{text}")]')
            element.click()
            return
        except NoSuchElementException:
            pass

        raise NoSuchElementException(f"No se encontró el elemento con texto: {text}")

    def access_scroll_swipe(self):
        # time.sleep(2)
        self.find_and_click("Scrool & Swipe & Grid")
        time.sleep(1)

    def perform_swipe(self):
        finger = PointerInput(PointerInput.KIND_TOUCH, "finger")
        action = ActionBuilder(self.driver, mouse=finger)

        start_x, start_y = 324, 225
        end_x, end_y = 116, 225

        action.pointer_action.move_to_location(start_x, start_y)
        action.pointer_action.pointer_down()
        action.pointer_action.move_to_location(end_x, end_y)
        action.pointer_action.pointer_up()
        action.perform()

        time.sleep(1)

    def select_middle_option(self):
        middle_option = self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@value=\"50%\"]")
        middle_option.click()
        time.sleep(1)

    def enter_store(self):
        store_section = self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeApplication[@name=\"NinjaSDET\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeScrollView")
        store_section.click()
        store_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Tienda")
        store_button.click()
        time.sleep(2)

    def go_back_twice(self):
        back_button_first = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Back")
        back_button_first.click()
        time.sleep(1)
        back_button_second = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Back")
        back_button_second.click()
        time.sleep(1)

    def logout(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            menu_button = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//XCUIElementTypeApplication[@name=\"NinjaSDET\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeButton")))
            menu_button.click()
            time.sleep(1)
            logout_button = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Cerrar sesión")))
            logout_button.click()
            time.sleep(2)
        except TimeoutException:
            print("❌ No se pudo cerrar sesión")
        except NoSuchElementException:
            print("❌ Elemento no encontrado")
