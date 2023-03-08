from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from Test_locaters import locaters
from Test_data import data
import pytest

class TEST_PRATIK:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    
    def __init__(self):
         self.driver.get(data.Pratik_Data().url)
    
    def login(self):
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locaters.Pratik_locaters().username_Inputbox).send_keys(data.Pratik_Data().username)
        self.driver.find_element(by=By.NAME, value=locaters.Pratik_locaters().password_Inputbox).send_keys(data.Pratik_Data().password)
        self.driver.find_element(by=By.XPATH, value=locaters.Pratik_locaters.Login_button).click()
        sleep(2)
        if self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index':
            print("User Logged In sucessfully!")#sucessfull Login
        else :
            print("Invalid User ID/Password")#invalid Login
        self.driver.find_element(by=By.XPATH, value=locaters.Pratik_locaters.pim_selector).click()#pim selector
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locaters.Pratik_locaters().search_ep).send_keys(data.Pratik_Data().src_employee)
        self.driver.find_element(by=By.XPATH, value=locaters.Pratik_locaters.search_button).click()
        sleep(2)
        print('Employee Found!')
        self.driver.find_element(by=By.XPATH, value=locaters.Pratik_locaters.edit_employee).click()#edit ep
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locaters.Pratik_locaters().nickname_input).send_keys(data.Pratik_Data().new_nickname)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locaters.Pratik_locaters.con_button).click()
        print("Changes Saves Sucessfully")   
TEST_PRATIK().login()
