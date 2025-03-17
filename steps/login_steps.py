from behave import given, when, then
from pages.login_page import LoginPage
from pages.dropdown_toggle_page import DropdownTogglePage
from utils.appium_driver import get_driver

@given('que el usuario abre la aplicación')
def step_open_app(context):
    context.driver = get_driver()
    context.login_page = LoginPage(context.driver)
    context.dropdown_toggle_page = DropdownTogglePage(context.driver)

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

@when('accede a la funcionalidad de selección')
def step_access_functionality(context):
    context.dropdown_toggle_page.access_dropdown_toggle()
    context.dropdown_toggle_page.select_easy_option()
    context.dropdown_toggle_page.click_option_three()
    context.dropdown_toggle_page.confirm_selection()
    context.dropdown_toggle_page.click_ok()
    context.dropdown_toggle_page.navigate_to_checkmarks_tab()
    context.dropdown_toggle_page.select_all()
