import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.data_reader import read_users_csv

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()

@pytest.fixture
def driver_logged(driver):
    login_page = LoginPage(driver)

    user = read_users_csv()[0]

    login_page.login(user["username"], user["password"])
    
    return driver

