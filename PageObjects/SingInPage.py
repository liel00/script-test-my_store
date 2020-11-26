from selenium.webdriver.common.by import By


class SinginPage():

    def __init__(self,driver):
        self.driver = driver


    email = (By.XPATH,"//input[@id='email']")
    password = (By.XPATH,"//input[@id='passwd']")
    submit = (By.XPATH,"//body/div[@id='page']/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[1]/p[2]/button[1]/span[1]")
    massagefail = (By.XPATH,"//p[contains(text(),'There is 1 error')]")
    massagesucceed = (By.XPATH, "//p[contains(text(),'Welcome to your account. Here you can manage all o')]")
    singout = (By.XPATH,"//a[contains(text(),'Sign out')]")


    def get_email(self,text):
        """ This function can be written in a text box of the email in singin """
        return self.driver.find_element(*SinginPage.email).send_keys(text)

    def get_password(self,text):
        """ This function can be written in a text box of the password in singin """
        return self.driver.find_element(*SinginPage.password).send_keys(text)

    def get_submit(self):
        """ This function clicks submit """
        return self.driver.find_element(*SinginPage.submit).click()


    def get_massage_fail(self):
        """ This function indicates an error when entering a wrong password and email and turns it into text """
        return self.driver.find_element(*SinginPage.massagefail).text


    def get_massage_succeed(self):
        """ This function indicates a positive message when you enter the correct password and email and turns it into text """
        return self.driver.find_element(*SinginPage.massagesucceed).text

    def get_singout(self):
        """This function presses singout"""
        return self.driver.find_element(*SinginPage.singout).click()