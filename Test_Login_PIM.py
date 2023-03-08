from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from Test_locaters import locaters
from Test_data import data
from time import sleep
import pytest
class TEST_PRATIK:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    def __init__(self):
         self.driver.get(data.Pratik_Data().url)
    def test_login(self):
        self.driver.find_element(by=By.NAME, value=locaters.Pratik_locaters().username_Inputbox).send_keys(data.Pratik_Data().username)
        self.driver.find_element(by=By.NAME, value=locaters.Pratik_locaters().password_Inputbox).send_keys(data.Pratik_Data().password)
        self.driver.find_element(by=By.XPATH, value=locaters.Pratik_locaters().Login_button).click()
        sleep(2)
        if self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index':
            print("User Logged In sucessfully!")#sucessfull Login
        else :
         print("Invalid User ID/Password")#invalid Login
         assert self.driver.title == 'OrangeHRM'
         yield
         print("login failed")
        print("SUCCESS : Logged in with Username {a} and Password {b}". format(a=data.Pratik_Data.username, b=data.Pratik_Data.password))
        #pim selector
        self.driver.find_element(by=By.XPATH, value=locaters.Pratik_locaters.pim_selector).click()
        self.driver.find_element(by=By.XPATH, value=locaters.Pratik_locaters.pim_button).click()#add profile
        sleep(5) 
        self.driver.find_element(by=By.XPATH,value=locaters.Pratik_locaters().ep_namebox).send_keys(data.Pratik_Data().ep_name)#add employee data
        self.driver.find_element(by=By.XPATH, value=locaters.Pratik_locaters().ep_mdnamebox).send_keys(data.Pratik_Data().ep_mdname)
        self.driver.find_element(by=By.XPATH, value=locaters.Pratik_locaters().ep_lstnamebox).send_keys(data.Pratik_Data().ep_lstname)
        sleep(2)
        #Pim editor
        self.driver.find_element(by=By.XPATH,value=locaters.Pratik_locaters.save_button).click()#save data
        print("Employee Created sucessfully")
        self.driver.minimize_window()         
TEST_PRATIK().test_login()
