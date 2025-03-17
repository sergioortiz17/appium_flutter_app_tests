from appium.webdriver.common.appiumby import AppiumBy

class DropdownTogglePage:
    def __init__(self, driver):
        self.driver = driver

    def access_dropdown_toggle(self):
        el1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Dropdown & Toggle")
        el1.click()

    def select_easy_option(self):
        el2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Fácil")
        el2.click()

    def click_option_three(self):
        el3 = self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeApplication[@name=\"NinjaSDET\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]")
        el3.click()
        el4 = self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeApplication[@name=\"NinjaSDET\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeButton")
        el4.click()

    def confirm_selection(self):
        el5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Confirmar selección")
        el5.click()

    def click_ok(self):
        el6 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "OK")
        el6.click()

    def navigate_to_checkmarks_tab(self):
        el7 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Checkmarks\nTab 2 of 2")
        el7.click()

    def select_all(self):
        el8 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Seleccionar todas")
        el8.click()
