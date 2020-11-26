import pytest

from PageObjects.Homepage import HomePage
from TestData.SinginPageData import SinginPageData
from utilities.Base import Base

# Test number five I can log in with an existing user and the non-existing user is blocked.

class TestFive(Base):
    def test_Singin(self,getData):
        log = self.getLogger()
        log.info("Test number five Singin ")
        homepage = HomePage(self.driver)
        singinpage = homepage.get_singin()
        singinpage.get_email(getData["email"])
        singinpage.get_password(getData["password"])
        singinpage.get_submit()
        if getData["email"] == "Tes124@gmail.com":
            assert ("There is 1 error" == singinpage.get_massage_fail())
        elif getData["email"] == "Test00@gmail.com" :
             assert ("Welcome " in singinpage.get_massage_succeed())



    @pytest.fixture(params=SinginPageData.test_SinginPage_data)
    def getData(self, request):
        return request.param
