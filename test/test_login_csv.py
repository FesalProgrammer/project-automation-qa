from pages.login_page import LoginPage
from utils.data_reader import read_users_csv
import pytest

# El archivo .csv se usara exclusivamnte para el test del login.

#Aqui vamos a realizar varias pruebas (combinaciones de usuario y passwords) usando para ello la misma funcion de prueba, por esto conviene parametrizar.

@pytest.mark.parametrize("user", read_users_csv())
def test_login(driver, user):
    
    login_page = LoginPage(driver)

    login_page.login(user["username"], user["password"])

    if user["valid"] == "true":
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
    else:
        error = login_page.get_error_message()
        assert "Epic sadface" in error