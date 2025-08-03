import pytest
from selenium import webdriver
from lesson_27.page_objects.nova_post_page_object import NovaPostPageObject

@pytest.fixture(scope="session")
def nova_post_track_page():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()

    yield NovaPostPageObject(chrome_driver)
    chrome_driver.quit()