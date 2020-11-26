import time


from PageObjects.Homepage import HomePage
from utilities.Base import Base

# Test number one I check if the desired result has more or equal to one. In our Mecca I check out T-shirts

class TestOne(Base):

    def test_SearchTrue(self):
        log = self.getLogger()
        log.info("Test number one SearchTrue ")
        homepage = HomePage(self.driver)
        homepage.get_search("T-shirts")
        tshirtspage = homepage.get_clicksearch()
        check = tshirtspage.get_check_tshirts()
        assert 1 <= int(check[0])


