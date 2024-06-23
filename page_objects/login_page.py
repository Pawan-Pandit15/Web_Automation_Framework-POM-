from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


class Login_Page:
    def __init__(self, driver):
        self.driver = driver

    # Locator
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_Button = (By.XPATH, "//button[@type='submit']")
    invalid_message = (By.XPATH, "//p[text()='Invalid credentials']")

    def username_textbox(self):
        return self.driver.find_element(*Login_Page.username)

    def password_textbox(self):
        return self.driver.find_element(*Login_Page.password)

    def submit_button(self):
        return self.driver.find_element(*Login_Page.login_Button)

    def invalid_input(self):
        return self.driver.find_element(*Login_Page.invalid_message).text

    def test_login_page(self, usr, psd):
        self.username_textbox().send_keys(usr)
        self.password_textbox().send_keys(psd)
        self.submit_button().click()








