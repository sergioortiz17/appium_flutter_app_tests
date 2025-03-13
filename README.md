# 🏆 Basic Flutter App Tests - Pruebas Automatizadas 📱

Este repositorio contiene pruebas automatizadas de una aplicación Flutter utilizando **Appium**, **Behave (Cucumber/Gherkin)** y **Allure** para los reportes.

---

## 🚀 Instalación y Configuración

### 1️⃣ **Crear y Activar un Entorno Virtual**
Antes de instalar las dependencias, crea y activa un entorno virtual para evitar conflictos con otras librerías de Python.

#### En Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
Para Windows:

```bash
python3 -m venv venv
venv\Scripts\activate
```
2️⃣ Instalar Dependencias
Una vez activado el entorno virtual, instala todas las librerías necesarias con:

```bash
pip install -r requirements.txt
```
🏗️ Estructura del Proyecto

basic_flutter_app_tests/
│── features/
│   ├── login.feature   # Escenarios en Gherkin
│── steps/
│   ├── login_steps.py  # Implementación de los pasos en Python
│── pages/
│   ├── base_page.py     # Clase base para todas las páginas
│   ├── login_page.py    # Página de login (Page Object Model)
│── utils/
│   ├── appium_driver.py # Gestión del driver de Appium
│   ├── config.py        # Configuración de variables globales
│── reports/             # Carpeta para almacenar reportes de Allure
│── environment.py       # Setup/Teardown de pruebas
│── requirements.txt     # Librerías necesarias
│── behave.ini           # Configuración de Behave
│── README.md            # Explicación del proyecto

🔥 Ejecutar las Pruebas
1️⃣ Ejecutar pruebas con Behave
```bash
behave --format allure_behave.formatter:AllureFormatter -o reportes/
```
2️⃣ Generar Reporte con Allure
```bash
allure serve reportes/
```

📌 Notas Importantes
Asegúrate de tener Appium en ejecución antes de correr las pruebas.
La configuración del driver Appium está en utils/appium_driver.py, revisa si necesitas modificar capabilities.
Los reportes se generan en reportes/ y pueden visualizarse con Allure.
✨ Tecnologías Usadas
Appium 🚗 - Para pruebas en dispositivos móviles
Behave (Cucumber/Gherkin) 🍀 - Para definir escenarios de prueba en lenguaje natural
Selenium WebDriver 🕵️‍♂️ - Base para la automatización con Appium
Allure 📊 - Para generar reportes de ejecución
🤖 Contribución
Si deseas contribuir a este proyecto, ¡bienvenido! 🚀
Haz un fork del repositorio, crea una nueva rama y envía un pull request con tu mejora.

🛠️ Autor
Desarrollado por: Sergio Ortiz
📧 Contacto: sergioortiz170992@gmail.com
🚀 ¡Felices pruebas automatizadas!
