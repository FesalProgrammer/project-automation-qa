import requests

headers = {
    
  "x-api-key":"pub_0c467ebc212bdc0fc96774a8af22442e253722fef14060fe1fd499f4b3c96284"
}

def test_login_valido():
    """
    Interactua con la Api a traves del metodo POST para logear un usuario valido y devuelve el status_code 200 si la accion es exitosa
    """
    body={
        "email":"eve.holt@reqres.in",
        "password":"cityslicka"
    }
    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)
    
    assert response.status_code == 200

def test_login_sin_password():
    """
    Interactua con la Api a traves del metodo POST para logear un usuario sin info del password y devuelve el status_code 400 si la accion es exitosa
    """
    body={
        "email":"eve.holt@reqres.in",
        
    }
    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)
    
    assert response.status_code == 400

def test_create_user():
    """
    Interactua con la Api a traves del metodo POST para crear un usuario y devuelve el status_code 201 si la accion es exitosa, tambien valida la correspondencia entre valores del json enviado como body y el json devuelto. Mide el tiempo de respuesta, lo compara contra un tiempo estimado establecido (1 sec) y devuelve True si es menor (Test passed)
    """
    body={
        "name":"Fesal",
        "email":"fesal@gmail.com",
        "password":"123456"
    }
    response = requests.post("https://reqres.in/api/users", headers=headers, json=body)
    
    data =response.json()
    
    assert response.status_code == 201

    assert data["name"] == body["name"]
    assert data["email"] == body["email"]

    assert response.elapsed.total_seconds() < 1, "El tiempo de ejecucion para crear un usuario superó el tiempo estimado (1 seg)"

def test_delete_user():
    """Interactua con la Api a traves del metodo DELETE para eliminar un usuario y devuelve el status_code 204 si la accion es exitosa"""
    
    response = requests.delete("https://reqres.in/api/users/2", headers=headers)
    
    assert response.status_code == 204

def test_get_user():
    """Interactua con la Api a traves del metodo GET (la api devuelve status_code == 200). Mide el tiempo de respuesta, lo compara contra un tiempo estimado establecido (1 sec) y devuelve True si es menor (Test passed) """
    
    response = requests.get("https://reqres.in/api/users/2", headers=headers)
    
    assert response.status_code == 200

    assert response.elapsed.total_seconds() < 1,"El tiempo de ejecucion para obtener un usuario superó el tiempo estimado (1 seg)"
