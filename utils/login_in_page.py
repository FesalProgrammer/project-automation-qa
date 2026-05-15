from selenium import webdriver
from selenium.webdriver.common.by import By

def login(driver):
    """ Automatización de Login:
        •	Navegar a la página de login de saucedemo.com
        •	Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")
        •	Validar login exitoso verificando que se haya redirigido a la página de inventario
    """

    # 1. Navegar a la página de login de saucedemo.com
    driver.get("https://www.saucedemo.com/")

    # 2. Ingresar credenciales válidas 
    usuario = driver.find_element(By.ID,"user-name")
    usuario.send_keys("standard_user")
    
    # 3. Ingresar contraseña
    password = driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")

    # 4. hacer click en el boton.
    boton_login = driver.find_element(By.ID,"login-button")
    boton_login.click()
