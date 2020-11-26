from selenium.webdriver.common.by import By


class SummerPage():

    def __init__(self,driver):
        self.driver = driver

    allcard = (By.XPATH,"//span[contains(text(),'There are 3 products.')]")
    blue = (By.XPATH,"//a[text()= 'Blue']")


    def get_blue(self):
        """ This function presses the filter blue """
        return self.driver.find_element(*SummerPage.blue).click()

    def get_blue_text(self):
         """ This function converts the blue filter to text """
         return self.driver.find_element(*SummerPage.blue).text

    def get_allcard(self):
        """ This function indicates how many cards are on the page """
        return self.driver.find_element(*SummerPage.allcard).text

