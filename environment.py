# environment.py
import allure
import os

def before_scenario(context, scenario):
    print(f"Iniciando escenario: {scenario.name}")

def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
    print(f"Finalizando escenario: {scenario.name}")

def after_step(context, step):
    """
    Captura un screenshot automáticamente si un paso falla y lo adjunta a Allure,
    además de guardarlo en una carpeta 'screenshots/'.
    """
    if step.status == "failed":
        # Asegurar que la carpeta 'screenshots' existe
        os.makedirs("screenshots", exist_ok=True)
        
        # Guardar el screenshot en la carpeta
        screenshot_path = f"screenshots/error_{step.name}.png"
        context.driver.save_screenshot(screenshot_path)
        
        # Adjuntar el screenshot en el reporte de Allure
        with open(screenshot_path, "rb") as image:
            allure.attach(image.read(), name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
