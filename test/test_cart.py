from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.logger import logger
import pytest

""" Interaccion con Productos"""

def test_cart(login_in_driver):
    """ 
    Agrega un producto al carrito haciendo clic en el botón correspondiente.
    Verificar que el contador del carrito se incremente correctamente.
    Navega al carrito de compras.
    Compruba que el producto añadido aparezca correctamente en el carrito.

    """
    logger.info("test_cart inicia sesion")
    driver = login_in_driver
    
    logger.info("Se agrega un producto al carrito")
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()

    logger.info("Se valida incremento del contador")
    contador_cart = driver.find_element(By.CLASS_NAME,"shopping_cart_badge")
    assert contador_cart.text == "1", "La cantidad de productos no se agregaron correctamente"
    
    logger.info("Se obtiene el nombre del primer producto")
    product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text

    logger.info("Navega al carrito de compra")
    driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

    logger.info("Obtiene el nombre del producto en el carrito")
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    logger.info("Valida que el producto agregado al carrito sea el correcto ")
    assert cart_item == product_name, "El producto agregado no coincide"
    logger.info("test_cart completado\n")
    