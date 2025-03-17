@scroll_swipe
# behave -t @scroll_swipe

Feature: Scroll, Swipe y navegación a la Tienda

  Scenario Outline: Login exitoso y navegación con Scroll y Swipe
    Given que el usuario abre la aplicación
    When ingresa "<usuario>" en el campo usuario
    And ingresa "<contraseña>" en el campo contraseña
    And presiona el botón de ingresar
    When accede a la funcionalidad de scroll y swipe

    Examples:
      | usuario  | contraseña |
      | admin    | admin     |
    #   | tester1  | test123   |
    #   | qauser   | pass456   |
