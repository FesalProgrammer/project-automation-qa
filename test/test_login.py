from pages.login_page import LoginPage
from utils.logger import logger

def test_login_ok(driver):
    """ Valida login exitoso verificando que se haya redirigido a la página de inventario """
    logger.info("Iniciando test_login_ok")
    logger.info("Inicializando el driver para test_login_ok")
    login_page = LoginPage(driver)
    
    logger.info("Ingresando datos de entrada para el usuario del login: %s", "standar_user")
    logger.info("Ingresando datos de entrada para el password del login: %s", "secret_sauce")
    login_page.login("standard_user", "secret_sauce")

    logger.info("Verificando redireccion exitosa")
    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
    if "/inventory.html" in driver.current_url:
        logger.info("Redireccion exitosa")
        logger.info("Test del login_ok completado exitosamente")
    else:
        logger.info(f"Redireccion fallida. URL:{ driver.current_url}" )

def test_login_invalid_password(driver):
    """ Valida manejo adecuado del error ante un intento de login usando password invalido """
    logger.info("Iniciando test_login_invalid_password")
    
    logger.info("Inicializando el driver")
    login_page = LoginPage(driver)
    
    logger.info("Ingresando datos de entrada para el usuario del login: %s", "standar_user")
    logger.info("Ingresando datos de entrada para el password del login: %s", "12345")
    login_page.login("standard_user", "12345")

    error = login_page.get_error_message()

    #assert "Epic sadface: Username and password do not match any user in this service" in error
    # Aqui se fuerza al assert a fallar para generar un screenshot en el reporte..
    logger.info("Se obliga al assert a fallar hardcodeando el texto de comparacion del mensaje de error con 'hola'")
    assert  error == "hola"