from PageObjects.Homepage import HomePage
from utilities.Base import Base

# Test number two I test a product that is not in the store through the search

class TestTwo(Base):
    def test_SearchFalse(self):
        log = self.getLogger()
        log.info("Test number two SearchFalse ")
        homepage = HomePage(self.driver)
        homepage.get_search("Tie")
        tshirtspage = homepage.get_clicksearch()
        check = tshirtspage.get_check_tie()
        assert ("No results were found for your search" in check)
