# Framework de Automatización QA (UI & API) - Fesal La Rosa.

## Proposito del proyecto:

Este repositorio contiene el framework de pruebas automatizadas diseñadas para validar la aplicación Swag Labs (`www.saucedemo.com`) en la parte correspondiente a la interfaz de usuario (UI)y JsonPlaceHolder ( `https://jsonplaceholder.typicode.com`) para las capas de servicio (API) de forma eficiente, escalable y mantenible. El proyecto implementa el patrón Page Object Model (POM) para UI y un enfoque Data-Driven para las pruebas de API.

## Características Principales

• UI Testing (Page Object Model): Separación estricta de responsabilidades. Los selectores y la lógica de interacción están centralizados en la carpeta /pages, facilitando el mantenimiento ante cambios en la interfaz.
• API Testing (Data-Driven & CRUD): Cobertura completa de métodos HTTP (GET, POST, PATCH, DELETE) con validaciones profesionales de códigos de estado y tiempos de respuesta.
• Parametrización y Datos Externos: Uso de @pytest.mark.parametrize.
• Reportes y Logging Avanzados: Generación de reportes HTML detallados (pytest-html), hooks personalizados en conftest.py para la captura de evidencias y logs.
• CI/CD Ready: Estructura modular y marcadores (markers) que permiten la ejecución paralela y selectiva de suites, preparado para integración con GitHub Actions.

## Tecnologias usadas:

• Lenguaje principal: Python 3.13
• Estructura de testing: Pytest
• Automatización Web: Selenium WebDriver
• Control de Versiones: Git & GitHub
• Reportes: Pytest-HTML

## Configuración

El comportamiento del framework se gestiona a través de archivos de configuración centralizados:
• pytest.ini: Configurado con metadatos del proyecto (título, autor) y marcadores personalizados (smoke, api, e2e).
• conftest.py: Contiene el fixture driver() para la inicialización del navegador, fixture de encadenamiento de tests para simular el flujo real de una aplicación: crear → leer → actualizar → eliminar y hooks personalizados para la captura de logs y evidencias en caso de fallo.

## Instalación del repositorio

`https://github.com/FesalProgrammer/project-automation-qa.git`

## Instalación de las dependencias

`pip install -r requiremnts.txt`
`pip install selenium`
`pip install requests`
`pip install pathlib`
`pip install pytest_html`

## Ejecucion de las pruebas

• Comando para ejecutar las pruebas: `py -m pytest -v`

## Enfoque de Pruebas

• UI - Page Object Model
• Se han centralizado los locators en la carpeta /pages, permitiendo que cualquier cambio en la interfaz de la aplicación se gestione en un único punto, reduciendo el mantenimiento del código.

• Autenticación (test_login): Verifica que el usuario sea redirigido correctamente a la página de inventario tras un login exitoso.

• Validación de Inventario (test_inventory):

• Verificación de títulos de página.

• Confirmación de visibilidad de productos.

• Validación de elementos presentes en la UI (menú hamburguesa y filtro).

• Gestión del Carrito (test_cart): Flujo completo de agregar un producto, verificar el incremento en el contador y validar que el ítem correcto aparezca en la vista del carrito.

• Se configura `pytest.ini` para que genere de forma automatica un reporte HTML con los resultados de la ejecución de pruebas.

## API - Ciclo de Vida y CRUD

• Los tests de API cubren flujos críticos, incluyendo pruebas de ciclo de vida que aseguran la persistencia y manipulación correcta de datos mediante operaciones Create, Read, Update y Delete (CRUD), validadas con asserts profesionales.

• Framework desarrollado siguiendo estándares profesionales de automatización de QA. Última actualización: Junio 2026.
