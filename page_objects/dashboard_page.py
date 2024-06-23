from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


class Dashboard_Page:
    def __init__(self, driver):
        self.driver = driver

    # Locator
    PIM_element = (By.XPATH, "//a[@class='oxd-main-menu-item active']")
    add_new_PIM = (By.XPATH, "//button[normalize-space()='Add']")
    first_name = (By.XPATH, "//input[@placeholder='First Name']")
    last_name = (By.XPATH, "//input[@placeholder='Last Name']")
    emp_id = (By.XPATH, "//input[@class='oxd-input oxd-input--focus']")
    save_button = (By.XPATH, "//button[@type='submit']")

    def pim_option(self):
        return self.driver.find_element(*Dashboard_Page.PIM_element)

    def add_new_details(self):
        return self.driver.find_element(*Dashboard_Page.add_new_PIM)

    def add_first_name(self):
        return self.driver.find_element(*Dashboard_Page.first_name)

    def add_last_name(self):
        return self.driver.find_element(*Dashboard_Page.last_name)

    def add_emp_id(self):
        return self.driver.find_element(*Dashboard_Page.emp_id)

    def save_details(self):
        return self.driver.find_element(*Dashboard_Page.save_button)

    def test_dashboard_page(self, first_name, last_name, emp_id):
        self.pim_option().click()
        self.add_new_details().click()
        self.add_first_name().send_keys(first_name)
        self.add_last_name().send_keys(last_name)
        self.add_emp_id().send_keys(emp_id)
        self.save_details().click()
