import time


from PageObjects.Homepage import HomePage
from PageObjects.TshirtsPage import TshirtsPage
from utilities.Base import Base

# Test number three I check if I am moving to the correct page in my case to the T-SHIRTS page

class TestThree(Base):

    def test_Menu(self):
        log = self.getLogger()
        log.info("Test number three Menu ")
        homepage = HomePage(self.driver)
        self.move_Mouse_To_Element(homepage.get_women())
        self.move_Mouse_To_Element_click(homepage.get_women_shirts())
        tshirtspage = TshirtsPage(self.driver)
        check = tshirtspage.get_tshirts_titel()
        assert ("T-SHIRTS " in check)
        
