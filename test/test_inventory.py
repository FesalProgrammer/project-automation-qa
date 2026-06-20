from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.logger import logger


def test_inventory_title(driver_logged):
    """ Verifica título de página de inventario sea correcto.  """
    
    logger.info("Iniciando sesion en test_inventory_title")
    inventory_page = InventoryPage(driver_logged)

    logger.info("Validando titulo de la pagina")
    titulo = inventory_page.obtener_titulo()
    assert titulo == "Swag Labs", "Titulo no coincide"
    
    logger.info("test_inventory_title completado exitosamente\n")

@pytest.mark.smoke
def test_products_visibles(driver_logged):
    """ Comprueba existan productos visibles en la página (al menos verifica la presencia de uno)."""
    
    logger.info("Iniciando sesion en test_products_visible")
    inventory_page = InventoryPage(driver_logged)

    logger.info("Validandp la presencia de al menos un producto")
    productos = inventory_page.obtener_productos()
    assert len(productos) > 0, "Ausencia de productos"
    
    logger.info("Test completado exitosamente\n")

def test_ui_elements(driver_logged):
    """ Valida elementos importantes de la interfaz presentes (menú, filtros, etc.)."""
    logger.info("Iniciando test_ui_elements")
    inventory_page = InventoryPage(driver_logged) 

    logger.info("Validando presencia del icono del menu")
    productos = inventory_page.obtener_productos()
    assert inventory_page.menu_visible(), "Icono del menu no esta presente en la pagina."
    
    logger.info("Validando presencia del filtro")
    assert inventory_page.filtro_visible(), "El filtro del catalogo no esta presente en la pagina."

    logger.info("Test completado exitosamente\n")