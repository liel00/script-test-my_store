from PageObjects.Homepage import HomePage
from utilities.Base import Base

# Test number six I check if a logout can be performed

class TestSix(Base):

      def test_LogOut(self):
          log = self.getLogger()
          log.info("Test number six LogOut ")
          homepage = HomePage(self.driver)
          singinpage = homepage.get_singin()
          singinpage.get_email("Test00@gmail.com")
          singinpage.get_password("Ts123456")
          singinpage.get_submit()
          singinpage.get_singout()
