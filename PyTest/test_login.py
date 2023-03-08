from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

def test_setup():
    global driver
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()

def test_login():
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    driver.get(url)

    username_Inputbox = 'username'
    password_Inputbox = 'password'
    Login_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

    driver.find_element(by=By.NAME, value=username_Inputbox).send_keys('Admin')
    driver.find_element(by=By.NAME, value=password_Inputbox).send_keys('admin123')
    driver.find_element(by=By.XPATH, value=Login_button).click()

    assert driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
    print('login successfull')
def teardown():
    driver.close()
    driver.quit()
    print('Test completed')