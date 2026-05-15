from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):#Constructor ejecuta la clase cuando sea llamada
        self.driver = driver #le asigna driver a la clase LoginPage. driver abre la pagina en modo incognito.

        #selectores
        self.username_input= (By. ID, "user-name")
        self.password_input= (By. ID, "password")
        self.login_button = (By. ID, "login-button")
    def open(self):
        self.driver.get("https://www.saucedemo.com/")
     
    def ingresar_usuario(self, usuario):
        self.driver.find_element(*self.username_input).send_keys(usuario) 

    def ingresar_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_in_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, usuario, password):
        self.open()
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        self.click_in_login()