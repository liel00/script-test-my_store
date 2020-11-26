import inspect
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class Base:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger


    def move_Mouse_To_Element(self,text):
        action = ActionChains(self.driver)
        action.move_to_element(text).perform()

    def move_Mouse_To_Element_click(self,text):
        action = ActionChains(self.driver)
        action.move_to_element(text).click().perform()


    def verify_Link_Presence(self, text):
        element = WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))
