from behave import given, when
from pages.scroll_swipe_page import ScrollSwipePage
from pages.login_page import LoginPage
from utils.appium_driver import get_driver

@given('que el usuario abre la aplicación2')
def step_open_app(context):
    """Inicializa el driver y las páginas necesarias"""
    context.driver = get_driver()
    context.login_page = LoginPage(context.driver)
    context.scroll_swipe_page = ScrollSwipePage(context.driver)  # 🔹 Se inicializa correctamente

@when('accede a la funcionalidad de scroll y swipe')
def step_access_scroll_swipe(context):
    """Ejecuta los pasos de scroll, swipe y navegación a la tienda"""
    
    # 🔹 Asegurar que `context.scroll_swipe_page` está inicializado antes de usarlo
    if not hasattr(context, "scroll_swipe_page"):
        context.scroll_swipe_page = ScrollSwipePage(context.driver)  

    # 🔹 Realizar acciones en la UI
    context.scroll_swipe_page.access_scroll_swipe()
    context.scroll_swipe_page.enter_store()
    context.scroll_swipe_page.go_back_twice()

    # 🔹 Cierre del driver solo al final de la prueba
    context.driver.quit()

@when('ahora cierro sesión')
def step_logout(context):
    """Ejecuta el cierre de sesión"""
    context.scroll_swipe_page.logout()
