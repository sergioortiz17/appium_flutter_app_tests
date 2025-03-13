# login.feature
Feature: Login en la aplicación Flutter

  Scenario: Login exitoso con usuario admin
    Given que el usuario abre la aplicación
    When ingresa "admin" en el campo usuario
    And ingresa "admin" en el campo contraseña
    And presiona el botón de ingresar
    # Then ve el mensaje "¡Hola, bienvenido!"
    Then ve el mensaje "Bienvenido"
