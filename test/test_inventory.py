from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture

def driver_logged(login_in_driver):
    driver = login_in_driver
    return driver

""" Navegación y Verificación del Catálogo """

def test_inventory_title(driver_logged):
    """ Verifica título de página de inventario sea correcto.  """
    title = driver_logged.title
    assert title == "Swag Labs", "Titulo no coincide"

def test_products_visibles(driver_logged):
    """ Comprueba existan productos visibles en la página (al menos verifica la presencia de uno)."""
    products = driver_logged.find_elements(By.CLASS_NAME,"inventory_item")
    assert len(products) > 0

def test_ui_elements(driver_logged):
    """ Valida elementos importantes de la interfaz presentes (menú, filtros, etc.)."""
    menu = driver_logged.find_element(By.ID,"react-burger-menu-btn")
    filter = driver_logged.find_element(By.CLASS_NAME,"product_sort_container")
    
    assert menu.is_displayed(), "Icono del menu no esta presente en la pagina."
    assert filter.is_displayed(), "El filtro del catalogo no esta presente en la pagina."