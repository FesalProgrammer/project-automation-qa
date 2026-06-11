import requests
from utils.logger import logger


LOGIN_URL = "https://reqres.in/api/login"
CREATE_URL = "https://reqres.in/api/users"
URL = "https://reqres.in/api/users/2"

JSON_PLACEHOLDER_URL = "https://jsonplaceholder.typicode.com/posts/1"

headers = {
    
  "x-api-key":"pub_0c467ebc212bdc0fc96774a8af22442e253722fef14060fe1fd499f4b3c96284"
}

def test_login_valido():
    """
    Interactua con la Api a traves del metodo POST para logear un usuario valido y devuelve el status_code 200 si la accion es exitosa
    """
    logger.info("Iniciando test_login_valido")
    body={
        "email":"eve.holt@reqres.in",
        "password":"cityslicka"
    }
    
    response = requests.post(LOGIN_URL, headers=headers, json=body)
    
    logger.info("Se valida respuesta exitosa: status_code == 200")
    assert response.status_code == 200
    logger.info(f"Test completado en {response.elapsed.total_seconds():.3f}s\n")

def test_login_sin_password():
    """
    Interactua con la Api a traves del metodo POST para logear un usuario sin info del password y devuelve el status_code 400 si la accion es exitosa
    """
    logger.info("Iniciando test_login_sin_password")
    
    logger.info("Se preparan datos de entrada")
    body={
        "email":"eve.holt@reqres.in",
        
    }
    response = requests.post(LOGIN_URL, headers=headers, json=body)
    
    logger.info("Se valida respuesta exitosa: status_code == 400")
    assert response.status_code == 400
    logger.info(f"Test completado en {response.elapsed.total_seconds():.3f}s\n")

def test_create_user():
    """
    Interactua con la Api a traves del metodo POST para crear un usuario y devuelve el status_code 201 si la accion es exitosa, tambien valida la correspondencia entre valores del json enviado como body y el json devuelto. Mide el tiempo de respuesta, lo compara contra un tiempo estimado establecido (1 sec) y devuelve True si es menor (Test passed)
    """
    logger.info("Iniciando test_create_user")
    logger.info("Preparando datos de entrada...")
    body={
        "name":"Fesal",
        "email":"fesal@gmail.com",
        "password":"123456"
    }
    
    response = requests.post(CREATE_URL, headers=headers, json=body)
    
    data =response.json()
    
    logger.info("Validando respuesta exitosa: status_code == 201")
    assert response.status_code == 201

    logger.info("Validando campos creados")
    assert data["name"] == body["name"]
    assert data["email"] == body["email"]

    assert response.elapsed.total_seconds() < 1, "API muy lenta"
    logger.info(f"Test completado en {response.elapsed.total_seconds():.3f}s\n")

def test_get_user():
    """Interactua con la Api a traves del metodo GET (la api devuelve status_code == 200). Valida que al menos haya un usuario. Verifica performance del test midiendo el tiempo de respuesta, lo compara contra un tiempo estimado establecido en 1 seg y devuelve True si es menor (Test passed) """
    
    logger.info("Iniciando test_get_user")
    
    response = requests.get(URL, headers=headers)
    
    logger.info(f"Se valida respuesta exitosa")
    assert response.status_code == 200

    data = response.json()
    
    logger.info("Se valida que al menos haya un usuario")
    assert len(data["data"]) > 0 # al menos un usuario
    logger.info(f"Usuarios encontrados: {len(data['data'])} ")

    logger.info("Se valida performance: tiempo de prueba < 1 segundo")
    assert response.elapsed.total_seconds() < 1, "API muy lenta"
    
    if response.elapsed.total_seconds() < 1:
        logger.info("Validacion exitosa.")
        logger.info(f"GET completado en {response.elapsed.total_seconds():.3f}s\n")
    else:
        logger.info(f"API muy lenta: {response.elapsed.total_seconds():.3f} s.\n")
        
def test_update_user():
    logger.info("Iniciando test_update_user")
    logger.info("Preparando datos de entragda...")
    payload={
        "userId": 1,
        "id"    : 1,
        "title" : "Automation Testing Guide",
        "body"  : "Guía completa de testing automatizado"
    }
     
    response = requests.put(JSON_PLACEHOLDER_URL, json=payload)
    
    logger.info("Se valida respuesta exitosa: status_code == 200")
    assert response.status_code == 200
    data = response.json()

    logger.info("Se validan campos actualizados")
    assert data['title'] == 'Automation Testing Guide'
    assert data['body'] == 'Guía completa de testing automatizado'
    assert data['id'] == 1 

    logger.info("Se verifica performance")
    assert response.elapsed.total_seconds() < 1

    logger.info(f"Test completado en {response.elapsed.total_seconds():.3f} s.\n")

def test_update_created_post(created_post):
    post_id = created_post['id']
    
    logger.info("Iniciando test_update_created_post")
    logger.info("Preparando datos de entrada...")
    
    patch_payload={
        "title" : "Titulo actualizado"        
    }
        
    logger.info("Se envia solicitud patch a la Api")
    
    response = requests.patch(f'https://jsonplaceholder.typicode.com/posts/{post_id}', json=patch_payload)
    
    logger.info("Se valida respuesta exitosa: status_code == 200")
        
    assert response.status_code == 200

    logger.info("Se valida que solo title se haya actualizado")

    assert response.json()['title'] == 'Titulo actualizado', 'PATCH no actualizó el campo enviado'

    logger.info("Se verifica performance")
    assert response.elapsed.total_seconds() < 1

    logger.info(f"Test completado - solo title actualizado. Tiempo alcanzado: {response.elapsed.total_seconds():.3f} s.\n")

def test_delete_created_post(created_post):
    """Elimina el post creado en la fixture"""
    
    post_id = created_post['id']
    
    logger.info("Iniciando test_delete_created_post")
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')

    logger.info("Se valida respuesta exitosa: status_code == 200")
    assert response.status_code == 200 

    data = response.json()  

    logger.info("Se valida recurso eliminado")
    assert data == {}

    logger.info(f"Test completado - Recurso eliminado - Tiempo alcanzado: {response.elapsed.total_seconds():.3f} s.\n")

    