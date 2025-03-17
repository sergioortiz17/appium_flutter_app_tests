Feature: Login en la aplicación Flutter y navegación

  Scenario: Login exitoso con usuario admin y acceso a funcionalidad específica
    Given que el usuario abre la aplicación
    When ingresa "admin" en el campo usuario
    And ingresa "admin" en el campo contraseña
    And presiona el botón de ingresar
    And accede a la funcionalidad de selección

