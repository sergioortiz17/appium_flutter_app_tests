#  Appium Flutter App Tests - Pruebas Automatizadas 📱

Este repositorio contiene pruebas automatizadas de una App que desarrolle en Flutter.
Este repo de tests automatizado para Mobile utiliza **Appium**, **Behave (Cucumber/Gherkin)** y **Allure** para los reportes.

---
Esta es la app en flutter para automatizar en iOS y en Android
![image](https://github.com/user-attachments/assets/dec0c8ee-d04f-4cad-8365-461a37e48bc3)

Aca les dejo el repo de la app https://github.com/sergioortiz17/NinjaSDET
- Este es uno de los 4 features que tiene por el momento
#### Feature: Login en la app y acceso a dropdown toggle (La accion en el video empieza a los 5 segundos jeje perdon el delay)


https://github.com/user-attachments/assets/33217c67-4e07-4295-8d46-bbabe271c41e


####Aca dejo el link del drive con video evidencias de las pruebas automatizadas que hay hasta ahora
https://drive.google.com/drive/folders/1xfstL6r2t2DEIujrrV8yLzV5_jT3DlAZ?usp=sharing 

---
####Genera reporte correctamente
![image](https://github.com/user-attachments/assets/1a7139bc-e0e2-4e66-bf32-138db88e12c0)


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

🔥 Ejecutar las Pruebas
1️⃣ Ejecutar pruebas con Behave
```bash
behave --format allure_behave.formatter:AllureFormatter -o reportes/
```
Tambien podes correr individualmente cada test
behave -t @scroll_swipe
behave -t @register
behave -t @dropdown_toggle
behave -t @login

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
