# Proyecto de Automatizacion QA - Fesal La Rosa.

# Proposito del proyecto:

Validar la funcionalidad de los módulos principales de la aplicación Swag Labs (`www.saucedemo.com`), asegurando que los usuarios puedan autenticarse, visualizar el catálogo de productos y gestionar el carrito de compras de manera correcta.

## Tecnologias usadas:

- Lenguaje principal: Python 3.13
- Estructura de testing: Pytest
- Automatización Web: Selenium WebDriver
- Control de Versiones: Git & GitHub
- Reportes: Pytest-HTML

## Instalación del repositorio

`https://github.com/FesalProgrammer/pre-entrega-final-test_saucedemo`

## Instalación de las dependencias

`pip install -r requiremnts.txt`

## Ejecucion de las pruebas

- Comando para ejecutar las pruebas: `py -m pytest -v`

## Escenerarios Cubiertos

- Autenticación (test_login): Verifica que el usuario sea redirigido correctamente a la página de inventario tras un login exitoso.

- Validación de Inventario (test_inventory):

- Verificación de títulos de página.

- Confirmación de visibilidad de productos.

- Validación de elementos de UI (menú hamburguesa y filtro).

- Gestión del Carrito (test_cart): Flujo completo de agregar un producto, verificar el incremento en el contador y validar que el ítem correcto aparezca en la vista del carrito.

- Se configura `pytest.ini` para que genere de forma automatica un reporte HTML con los resultados de la ejecución de pruebas.
