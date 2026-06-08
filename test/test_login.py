from pages.login_page import LoginPage
from utils.logger import logger

def test_login_ok(driver):
    """ Valida login exitoso verificando que se haya redirigido a la página de inventario """
    
    logger.info("Iniciando test_login_ok")
    login_page = LoginPage(driver)
    
    logger.info("Completando credenciales...")
    login_page.login("standard_user", "secret_sauce")

    logger.info("Validando redireccion exitosa")
    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
    if "/inventory.html" in driver.current_url:
        logger.info("Redireccion exitosa")
        logger.info("Test del login_ok completado exitosamente")
    else:
        logger.info(f"Redireccion fallida. URL:{ driver.current_url}" )

def test_login_invalid_password(driver):
    """ Valida manejo adecuado del error ante un intento de login usando password invalido """
    logger.info("Iniciando test_login_invalid_password")
    
    
    login_page = LoginPage(driver)
    
    logger.info("Completando credenciales con password invalido...")
    login_page.login("standard_user", "12345")

    error = login_page.get_error_message()

    #assert "Epic sadface: Username and password do not match any user in this service" in error
    # Aqui se fuerza al assert a fallar para generar un screenshot en el reporte..
    logger.info("Validando falla forzada con mensaje de error == 'hola'")
    assert  error == "hola"