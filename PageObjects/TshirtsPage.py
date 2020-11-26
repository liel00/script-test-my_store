from selenium.webdriver.common.by import By


class TshirtsPage():

    def __init__(self, driver):
        self.driver = driver

    checktshirts = (By.XPATH, "//span[contains(text(),'1 result has been found.')]")
    checktie = (By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/div[2]/p[1]")
    tshirtstitel = (By.XPATH,"//body/div[@id='page']/div[2]/div[1]/div[3]/div[2]/h1[1]/span[1]")


    def get_check_tshirts(self):
        """ This function indicates the search result of the product T-shirts and turns it into text """
        return self.driver.find_element(*TshirtsPage.checktshirts).text

    def get_check_tie(self):
        """ This function indicates an incorrect search result """
        return self.driver.find_element(*TshirtsPage.checktie).text

    def get_tshirts_titel(self):
        """ This function points to a page title and turns it into text """
        return self.driver.find_element(*TshirtsPage.tshirtstitel).text
