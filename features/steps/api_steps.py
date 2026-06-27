from behave import given,when,then
import requests

headers = {
    
  "x-api-key":"pub_0c467ebc212bdc0fc96774a8af22442e253722fef14060fe1fd499f4b3c96284"
}
# Sceneario 1
@given("la API de Reqres esta disponible")
def step_connecting_api_reqres(context):
    context.base_url =("https://reqres.in/api")
 
@when("realizar un login valido")
def step_login(context):
    body={
        "email":"eve.holt@reqres.in",
        "password":"cityslicka"
    }

    context.response = requests.post(f"{context.base_url}/login",
                         headers=headers,
                         json=body
    )

@then("el status code debe ser {status_code:d}")
def step_validation_status(context, status_code):
    print(f"status: {context.response.status_code}")
    assert context.response.status_code == status_code

# Sceneario 2

@when("realizar un login sin contraseña")
def step_login_no_password(context):
    body={
        "email":"eve.holt@reqres.in"
    }

    context.response = requests.post(f"{context.base_url}/login",
                         headers=headers,
                         json=body
    )



@then("el mensaje de error debe ser '{mensaje}'")
def step_validation_msj(context, mensaje):
    body = context.response.json()
    assert body["error"] == mensaje
    