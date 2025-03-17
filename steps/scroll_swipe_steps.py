from behave import given, when
from pages.scroll_swipe_page import ScrollSwipePage
from pages.login_page import LoginPage
from utils.appium_driver import get_driver

@when('accede a la funcionalidad de scroll y swipe')
def step_access_scroll_swipe(context):
    """Ejecuta los pasos de scroll, swipe y navegación a la tienda"""
    

    if not hasattr(context, "scroll_swipe_page"):
        context.scroll_swipe_page = ScrollSwipePage(context.driver)  

    context.scroll_swipe_page.access_scroll_swipe()
    context.scroll_swipe_page.enter_store()
    context.scroll_swipe_page.go_back_twice()

    context.driver.quit()
