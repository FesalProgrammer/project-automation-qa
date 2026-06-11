from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.data_reader import read_products_json
from utils.logger import logger

def test_cart_json(driver_logged):
    logger.info("Iniciando prueba de test_cart_json")
    
    inventory_page = InventoryPage(driver_logged)
    cart_page = CartPage(driver_logged)
    productos = read_products_json()

    logger.info("Agregando productos al carrito")
    
    for producto in productos:
        inventory_page.agregar_producto_por_nombre(producto["nombre"])

    inventory_page.ir_al_carrito()
    productos_carrito = cart_page.obtener_productos_carrito()

    logger.info("Validando que nombre producto y precio se cargan correctamnte en el carrito") 
    for producto_json in productos:
        encontrado = False
        for producto_carrito in productos_carrito:
            if ( (producto_carrito["nombre"] == producto_json["nombre"]) and (producto_carrito["precio"] == producto_json["precio"])):
                encontrado = True
                break
        
        assert encontrado, f"Producto incorrecto o faltante: {producto_json["nombre"]}"
    
    logger.info("test_cart_json completado exitosamente\n")