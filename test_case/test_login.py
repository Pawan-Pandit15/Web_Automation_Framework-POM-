from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.login_page import Login_Page
from page_objects.dashboard_page import Dashboard_Page


# def test_valid_data(setup):
#     driver = setup
#     login_page = Login_Page(driver)
#     login_page.test_login_page("Admin", "admin123")
#
#     assert "dashboard" in driver.current_url, "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
#
#
# def test_invalid_username(setup):
#     driver = setup
#     login_page = Login_Page(driver)
#     login_page.test_login_page("Amin", "admin123")
#
#     WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(login_page.invalid_message, "Invalid credentials"))
#
#     if login_page.invalid_input() in "Invalid credentials":
#         assert True
#     else:
#         assert False
#
#
# def test_invalid_password(setup):
#     driver = setup
#     login_page = Login_Page(driver)
#     login_page.test_login_page("Admin", "admin12")
#
#     WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(login_page.invalid_message, "Invalid credentials"))
#
#     if login_page.invalid_input() in "Invalid credentials":
#         assert True
#     else:
#         assert False


def test_add_new_details(setup):
    driver = setup
    login_page = Login_Page(driver)
    login_page.test_login_page("Admin", "admin123")
    time.sleep(5)

    dashboard_page = Dashboard_Page(driver)
    dashboard_page.test_dashboard_page("Pawan", "Pandit", "007")
    time.sleep(5)




