import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="C:/Users/NewUser/Desktop/New folder/webdriver/chromedriver.exe")
    yield driver
    driver.quit()