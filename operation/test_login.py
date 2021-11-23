import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(100)
    driver.maximize_window()
    yield
    driver.quit()


@allure.description('valid login')
@allure.severity(severity_level='critical')
def test_validLogin(test_setup):
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.find_element(By.ID, 'txtUsername').clear()
    enter_username('admin')
    driver.find_element(By.ID, 'txtPassword').clear()
    enter_password('admin123')

    driver.find_element(By.ID, 'btnLogin').click()
    assert 'dashboard' in driver.current_url


@allure.description('invalid login')
@allure.severity(severity_level='normal')
def test_invalidLogin(test_setup):
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.find_element(By.ID, 'txtUsername').clear()
    enter_username('Admin')
    driver.find_element(By.ID, 'txtPassword').clear()
    enter_password('admin1234')

    driver.find_element(By.ID, 'btnLogin').click()
    try:
        assert 'dashboard' in driver.current_url
    finally:
        if AssertionError:
            allure.attach(driver.get_screenshot_as_png(), name="invalid case",
                          attachment_type=allure.attachment_type.PNG)


@allure.step('entering username as {0}')
def enter_username(username):
    driver.find_element(By.ID, 'txtUsername').send_keys(username)


@allure.step('entering password as {0}')
def enter_password(password):
    driver.find_element(By.ID, 'txtPassword').send_keys(password)
