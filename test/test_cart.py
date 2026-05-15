from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

""" Interaccion con Productos"""

def test_cart(login_in_driver):
    """ 
    Agrega un producto al carrito haciendo clic en el botón correspondiente.
    Verificar que el contador del carrito se incremente correctamente.
    Navegar al carrito de compras.
    Compruba que el producto añadido aparezca correctamente en el carrito.

    """
    driver = login_in_driver
    
    # Agrega un producto al carrito.
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()

    # Verifica incremento del contador
    contador_cart = driver.find_element(By.CLASS_NAME,"shopping_cart_badge")
    assert contador_cart.text == "1", "La cantidad de productos no se agregaron correctamente"
    
    # Obtener nombre del primer producto.
    product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text

    # navegar al carrito de compra
    driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

    #Obtener nombre del producto en el carrito.
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    # Verificar que el producto agregado en el carrito aparezca correctamente
    assert cart_item == product_name, "El producto agregado no coincide"