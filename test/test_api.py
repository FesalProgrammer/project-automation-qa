import requests

headers = {
    
  "x-api-key":"pub_0c467ebc212bdc0fc96774a8af22442e253722fef14060fe1fd499f4b3c96284"
}

def test_login_valido():
    body={
        "email":"eve.holt@reqres.in",
        "password":"cityslicka"
    }
    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)

    assert response.status_code == 200

def test_login_sin_password():
    body={
        "email":"eve.holt@reqres.in",
        
    }
    response = requests.post("https://reqres.in/api/login", headers=headers, json=body)

    assert response.status_code == 400

def test_create_user():
    body={
        "name":"Fesal",
        "email":"fesal@gmail.com",
        "password":"123456"
    }
    response = requests.post("https://reqres.in/api/users", headers=headers, json=body)

    data =response.json()
    #print(data)

    assert response.status_code == 201

    assert data["name"] == body["name"]
    assert data["email"] == body["email"]

    assert response.elapsed.total_seconds() < 1, "El tiempo de ejecucion para crear un usuario superó el tiempo estimado (1 seg)"

def test_delete_user():
    
    response = requests.delete("https://reqres.in/api/users/2", headers=headers)
    assert response.status_code == 204

def test_get_user():
    
    response = requests.get("https://reqres.in/api/users/2", headers=headers)
    assert response.status_code == 200

    print(response.elapsed.total_seconds())
    assert response.elapsed.total_seconds() < 1,"El tiempo de ejecucion para obtener un usuario superó el tiempo estimado (1 seg)"