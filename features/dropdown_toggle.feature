@dropdown_toggle
# behave -t @dropdown_toggle

Feature: Login en la app y acceso a dropdown toggle

  Scenario Outline: Login exitoso con usuario y acceso a funcionalidad específica
    Given que el usuario abre la aplicación
    When ingresa "<usuario>" en el campo usuario
    And ingresa "<contraseña>" en el campo contraseña
    And presiona el botón de ingresar
    And accede a la funcionalidad de selección

    Examples:
      | usuario  | contraseña |
      | admin    | admin     |
