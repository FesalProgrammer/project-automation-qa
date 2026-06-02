from pages.login_page import LoginPage

def test_login_ok(driver):
    """ Valida login exitoso verificando que se haya redirigido a la página de inventario """
    login_page = LoginPage(driver)
    
    login_page.login("standard_user", "secret_sauce")

    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"

def test_login_invalid_password(driver):
    """ Valida login exitoso verificando que se haya redirigido a la página de inventario """
    
    login_page = LoginPage(driver)
    
    login_page.login("standard_user", "12345")

    error = login_page.get_error_message()

    assert "Epic sadface: Username and password do not match any user in this service" in error