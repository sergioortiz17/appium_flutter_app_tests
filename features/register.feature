@register
Feature: Registro de usuario en la aplicación

  Scenario Outline: Registro exitoso de un nuevo usuario
    Given que el usuario abre la aplicación3
    When accede a la opción de registro
    And activa las opciones necesarias
    And ingresa "<nombre_usuario>" en el campo de usuario
    And ingresa "<password>" en el campo de contraseña
    And confirma "<password>" en el campo de confirmación de contraseña
    And presiona el botón "Crear user"
    And ingresa "<nombre_usuario>" en el campo de usuario en login
    And ingresa "<password>" en el campo de contraseña en login
    And presiona el botón "Ingresar"

    Examples:
      | nombre_usuario | password    |
      | test1         | Holamundo1  |
    #   | test2         | Contraseña2 |
    #   | usuario123    | Pass12345   |
