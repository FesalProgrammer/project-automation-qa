from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.logger import logger
import pytest


def test_cart(driver_logged):
    """ 
    Agrega un producto al carrito haciendo clic en el botón correspondiente.
    Verifica que el contador del carrito se incremente correctamente.
    Navega al carrito de compras. Comprueba que el producto añadido se carga correctamente en el carrito.

    """
    logger.info("Iniciando sesion en test_cart")
    driver = driver_logged
    
    logger.info("Agregando un producto al carrito")
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()

    logger.info("Validando incremento del contador")
    contador_cart = driver.find_element(By.CLASS_NAME,"shopping_cart_badge")
    assert contador_cart.text == "1", "La cantidad de productos no se agregaron correctamente"
    
    logger.info("Obteniendo el nombre del primer producto cargado")
    product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text

    driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

    logger.info("Obteniendo el nombre del producto subido al carrito")
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    logger.info("Validando que el producto agregado al carrito sea el correcto ")
    assert cart_item == product_name, "El producto agregado no coincide"
    logger.info("test_cart completado\n")
    