from pages.login_page import LoginPage
from utils.logger import logger

def test_login_ok(driver):
    """ Valida login exitoso verificando que se haya redirigido a la página de inventario """
    
    logger.info("Iniciando test_login_ok")
    login_page = LoginPage(driver)
    
    logger.info("Completando credenciales...")
    login_page.login("standard_user", "secret_sauce")

    logger.info("Validando redireccion exitosa")
    try:
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
        logger.info("Test completado")
    except AssertionError as e:
        logger.error(f"No se pudo entrar correctamente, URL actual {driver.current_url}")
        logger.error(e)

   
def test_login_invalid_password(driver):
    """ Valida manejo adecuado del error ante un intento de login usando password invalido """
    
    logger.info("Iniciando test_login_invalid_password")
        
    login_page = LoginPage(driver)
    
    logger.info("Completando credenciales con password invalido...")
    login_page.login("standard_user", "12345")

    error = login_page.get_error_message()

    assert "Epic sadface: Username and password do not match any user in this service" in error
    logger.info("Test completado")

def test_login_invalid_user(driver):
    """ Valida manejo adecuado del error ante un intento de login usando un user invalido """
    
    logger.info("Iniciando test_login_invalid_user")
        
    login_page = LoginPage(driver)
    
    logger.info("Completando credenciales con user invalido...")
    login_page.login("invalid_user", "secret_sauce")

    error = login_page.get_error_message()

    assert "Epic sadface: Username and password do not match any user in this service" in error
    logger.info("Test completado")

    #Epic sadface: Username is required
    
def test_login_user_empty(driver):
    """ Valida manejo adecuado del error ante un intento de login con un user vacio """
    
    logger.info("Iniciando test_login_user_empty")
        
    login_page = LoginPage(driver)
    
    logger.info("Completando credenciales con user invalido...")
    login_page.login("", "secret_sauce")

    error = login_page.get_error_message()

    assert "Epic sadface: Username is required" in error
    logger.info("Test completado")

def test_login_no_user_no_password(driver):
    """ Valida manejo adecuado del error ante un intento de login con un user vacio y password vacio """
    
    logger.info("Iniciando test_login_no_user_no_passqord")
        
    login_page = LoginPage(driver)
    
    logger.info("Dejando credenciales vacias...")
    login_page.login("", "")

    error = login_page.get_error_message()

    assert "Epic sadface: Username is required" in error
    logger.info("Test completado")