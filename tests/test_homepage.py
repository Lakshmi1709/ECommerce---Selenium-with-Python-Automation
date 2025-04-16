import pytest

from TestData.HomepageData import HomepageData
from Utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestHomePage(BaseClass):
    def test_formsSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)

        # Filling in the form fields
        log.info("firstname is" +getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.getPassword().send_keys(getData["password"])
        homepage.getCheckBox().click()

        # Selecting gender option from the dropdown
        self.selectOptionByText(homepage.getGender(), getData["gender"])

        # Clicking on status and submitting the form
        homepage.getStatus().click()
        homepage.SubmitButton().click()

        # Verify the alert message
        message = homepage.getAlert().text
        print(message)
        assert "Success!" in message
        self.driver.refresh()


    @pytest.fixture(params= HomepageData.test_Homepage_Data )
    def getData(self, request):
        return request.param

