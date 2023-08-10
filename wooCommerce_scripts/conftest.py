import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def init_driver(request):

     driver = webdriver.Chrome()

     request.cls.driver = driver

     yield

     request.cls.driver.quit()
