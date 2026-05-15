import pytest
from selenium import webdriver



@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()

# @pytest.fixture
# def login_in_driver(driver):
#     login(driver)
#     return driver

