# appium_driver.py
from appium import webdriver
from appium.options.ios import XCUITestOptions
from requests import get as request_get, delete, exceptions
from utils.config import *

def get_appium_version():
    try:
        response = request_get(f'http://{APPIUM_HOST}:{APPIUM_PORT}/status', timeout=TIME_OUT)
        return int(response.json().get('value', {}).get('build', {}).get('version', '1').split('.')[0])
    except exceptions.RequestException:
        return 1

def delete_previous_sessions(url):
    try:
        delete(f'{url}/session')
    except exceptions.RequestException:
        pass

def get_driver():
    options = XCUITestOptions()
    options.platform_name = PLATFORM_NAME
    options.platform_version = PLATFORM_VERSION
    options.device_name = DEVICE_NAME
    options.udid = UDID
    options.bundle_id = BUNDLE_ID
    options.automation_name = 'XCUITest'
    options.wda_local_port = 8100
    options.set_capability('autoGrantPermissions', True)
    
    appium_path = '' if get_appium_version() >= 2 else '/wd/hub'
    url = f'http://{APPIUM_HOST}:{APPIUM_PORT}{appium_path}'
    delete_previous_sessions(url)
    driver = webdriver.Remote(url, options=options)
    driver.implicitly_wait(TIME_OUT)
    return driver
