from selenium import webdriver
import pytest

from time import sleep

@pytest.fixture(scope='class')
def oneTimeSetUp(request):
    driver=webdriver.Chrome(executable_path="E:\\AutomationTesting\driver\chromedriver.exe")
    driver.get("http://jt-dev.azurewebsites.net/#/SignUp ")
    sleep(4)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    #print('drive close')
    driver.close()
    #print('driver quit')
    driver.quit()
