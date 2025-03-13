# login_steps.py
from behave import given, when, then
from pages.login_page import LoginPage
from utils.appium_driver import get_driver

@given('que el usuario abre la aplicación')
def step_open_app(context):
    context.driver = get_driver()
    context.login_page = LoginPage(context.driver)

@when('ingresa "{username}" en el campo usuario')
def step_enter_username(context, username):
    context.login_page.enter_username(username)

@when('ingresa "{password}" en el campo contraseña')
def step_enter_password(context, password):
    context.login_page.enter_password(password)

@when('presiona el botón de ingresar')
def step_click_login(context):
    context.login_page.click_login()

@then('ve el mensaje "{message}"')
def step_verify_message(context, message):
    assert context.login_page.get_welcome_message() == message, "El mensaje de bienvenida no coincide"
    context.driver.quit()
