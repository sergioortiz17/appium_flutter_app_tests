@login
# behave -t @login

Feature: Login en la aplicación Ninja SDET

  Scenario Outline: Login exitoso con diferentes usuarios
    Given que el usuario abre la aplicación
    When ingresa "<usuario>" en el campo usuario
    And ingresa "<contraseña>" en el campo contraseña
    And presiona el botón de ingresar

    Examples:
      | usuario  | contraseña |
      | admin    | admin     |
