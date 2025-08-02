import pytest
from selenium import webdriver


@pytest.fixture
def selenium_driver():
    driver = webdriver.Chrome()
    driver.get('http://localhost:8000/dz.html')
    yield driver
    driver.quit()