"""
    Para ver los print por terminal usar: py -m pytest -v -s test/test_cart_json.py
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.data_reader import read_products_json
from utils.logger import logger

def test_cart_json(driver_logged):
    logger.info("Inicia prueba de test_cart_json")
    logger.info("Inicia sesion / abre navegador en pagina de inventory") 
    inventory_page = InventoryPage(driver_logged)
    cart_page = CartPage(driver_logged)
    productos = read_products_json()

    logger.info("Looping a productos y los agrega por nombre")
    for producto in productos:
        inventory_page.agregar_producto_por_nombre(producto["nombre"])

    logger.info("vamos a carrito para ver que tiene cargado") 
    inventory_page.ir_al_carrito()
    productos_carrito = cart_page.obtener_productos_carrito()

    logger.info("Se valida nombre producto y precio se carga correctamnte en el carrito") 
    for producto_json in productos:
        encontrado = False
        for producto_carrito in productos_carrito:
            if ( (producto_carrito["nombre"] == producto_json["nombre"]) and (producto_carrito["precio"] == producto_json["precio"])):
                encontrado = True
                break
        
          

        assert encontrado, f"Producto incorrecto o faltante: {producto_json["nombre"]}"
    logger.info("test_cart_json completado\n")