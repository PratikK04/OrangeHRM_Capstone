from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from Test_locaters import locaters
from Test_data import data
from time import sleep

class TEST_PRATIK:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    sleep(5)
    driver.maximize_window()
    def __init__(self):
         self.driver.get(data.Pratik_Data().url)
    def login(self):
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locaters.Pratik_locaters().username_Inputbox).send_keys(data.Pratik_Data().username)
        self.driver.find_element(by=By.NAME, value=locaters.Pratik_locaters().password_Inputbox).send_keys(data.Pratik_Data().new_password)
        self.driver.find_element(by=By.XPATH, value=locaters.Pratik_locaters.Login_button).click()
        sleep(2)
        if self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index':
            print("User Logged In sucessfully!")#sucessfull Login
        else :
         print("Invalid User Password")#invalid Login
         assert self.driver.title == 'OrangeHRM'
        print("SUCCESS : Logged in with Username {a} and Password {b}". format(a=data.Pratik_Data.username, b=data.Pratik_Data.new_password))
TEST_PRATIK().login()
