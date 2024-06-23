import pytest
from selenium import webdriver
import time


@pytest.fixture()
def setup():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)
    return driver

# @pytest.fixture(scope="class")
# def setup(request):
#     driver = webdriver.Edge()
#     driver.maximize_window()
#     driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     request.cls.driver = driver
#     yield
#     driver.quit()
