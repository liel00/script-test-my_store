from selenium.webdriver.common.by import By

from PageObjects.SingInPage import SinginPage
from PageObjects.TshirtsPage import TshirtsPage


class HomePage ():

    def __init__(self,driver):
        self.driver = driver


    search = (By.XPATH,"//input[@id='search_query_top']")
    clicksearch =(By.XPATH,"//*[name()='button'][1]")
    women = (By.XPATH,"//*[name()='li'][1]")
    womenthirts = (By.XPATH,"//header/div[3]/div[1]/div[1]/div[6]/ul[1]/li[1]/ul[1]/li[1]/ul[1]/li[1]/a[1]")
    womensummer = (By.XPATH,"//a[text()= 'Summer Dresses']")
    singin = (By.XPATH,"//a[contains(text(),'Sign in')]")

    def get_search(self,text):
        """ This function writes in search """
        return self.driver.find_element(*HomePage.search).send_keys(text)

    def get_clicksearch(self):
        """ This function presses the magnifying saucer and instantly activates TshirtsPage"""
        self.driver.find_element(*HomePage.clicksearch).click()
        tshirtspage = TshirtsPage(self.driver)
        return tshirtspage


    def get_women(self):
        """This function indicates the women button in the menu"""
        return self.driver.find_element(*HomePage.women)

    def get_women_shirts(self):
        """This function indicates the shirt button found in women"""
        return self.driver.find_element(*HomePage.womenthirts)

    def get_women_summer(self):
        """This function indicates the summer button found in women"""
        return self.driver.find_element(*HomePage.womensummer)

    def get_singin(self):
        """This function presses singin and instantly activates SinginPage"""
        self.driver.find_element(*HomePage.singin).click()
        singinpage = SinginPage(self.driver)
        return singinpage

