@scroll_swipe
# behave -t @scroll_swipe

Feature: Ingresa al modulo Scroll, Swipe y Grid,  navega a la Tienda y prueba los backbuttons

  Scenario Outline: Login exitoso y navega dentro de la app
    Given que el usuario abre la aplicación
    When ingresa "<usuario>" en el campo usuario
    And ingresa "<contraseña>" en el campo contraseña
    And presiona el botón de ingresar
    When accede a la funcionalidad de scroll y swipe

    Examples:
      | usuario  | contraseña |
      | admin    | admin     |
