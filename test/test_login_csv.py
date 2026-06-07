from pages.login_page import LoginPage
from utils.data_reader import read_users_csv
from utils.logger import logger
import pytest

# El archivo .csv se usara exclusivamnte para el test del login.

#Aqui vamos a realizar varias pruebas (combinaciones de usuario y passwords) usando para ello la misma funcion de prueba, por esto conviene parametrizar.


@pytest.mark.parametrize("user", read_users_csv())
def test_login(driver, user):
    logger.info("Iniciando test_login_csv")
    logger.info("Inicializando el driver para test_login")
    login_page = LoginPage(driver)

    logger.info("Ingresando datos de entrada para el login")
    login_page.login(user["username"], user["password"])

    logger.info("Verificando redireccion exitosa")
    if user["valid"] == "true":
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
    else:
        error = login_page.get_error_message()
        assert "Epic sadface" in error

    if "/inventory.html" in driver.current_url:
        logger.info("redireccion exitosa")
        logger.info("Test del login completado exitosamente")
    else:
        logger.info(f"Redireccion fallida. URL:{ driver.current_url}" )