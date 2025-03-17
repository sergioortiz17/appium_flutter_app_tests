from behave import given, when
from pages.register_page import RegisterPage
from utils.appium_driver import get_driver

@given('que el usuario abre la aplicación3')
def step_open_app(context):
    """Inicializa el driver y la página de registro"""
    context.driver = get_driver()
    context.register_page = RegisterPage(context.driver)

@when('accede a la opción de registro')
def step_access_register(context):
    context.register_page.open_register_screen()

@when('ingresa "{username}" en el campo de usuario')
def step_enter_username(context, username):
    context.register_page.enter_username(username)

@when('ingresa "{password}" en el campo de contraseña')
def step_enter_password(context, password):
    context.register_page.enter_password(password)

@when('confirma "{password}" en el campo de confirmación de contraseña')
def step_confirm_password(context, password):
    context.register_page.confirm_password(password)
    context.driver.hide_keyboard()


@when('activa las opciones necesarias')
def step_activate_options(context):
    context.register_page.activate_switches()

@when('presiona el botón "Crear user"')
def step_click_create_user(context):
    context.register_page.click_create_user()

@when('ingresa "{username}" en el campo de usuario en login')
def step_login_username(context, username):
    context.register_page.enter_login_username(username)

@when('ingresa "{password}" en el campo de contraseña en login')
def step_login_password(context, password):
    context.register_page.enter_login_password(password)

@when('presiona el botón "Ingresar"')
def step_click_login(context):
    context.register_page.click_login()
    context.driver.quit()
