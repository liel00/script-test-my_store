from PageObjects.Homepage import HomePage
from PageObjects.SummerPage import SummerPage
from utilities.Base import Base

#Test number Four I test the color filter in the summer category.
# (There is a bug on the site that can not be filtered and therefore at this minute will fail)

class TestFour(Base):
    def test_Filter(self):
        log = self.getLogger()
        log.info("Test number Four Fillter ")
        homepage = HomePage(self.driver)
        self.move_Mouse_To_Element(homepage.get_women())
        self.move_Mouse_To_Element_click(homepage.get_women_summer())
        summerpage = SummerPage(self.driver)
        summerpage.get_blue()
        self.verifyLinkPresence("blue")
        bluefilter = summerpage.get_blue_text()
        allcard = summerpage.get_allcard()
        assert ( allcard[10] == bluefilter[6])
