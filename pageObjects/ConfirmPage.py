from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    searchcountry = (By.ID, "country")
    country = (By.LINK_TEXT, "India")
    checkbox = (By.CSS_SELECTOR, ".checkbox")
    purchase = (By.CSS_SELECTOR, "input[value='Purchase']")
    success = (By.CLASS_NAME, "alert-success")

    def SearchCountry(self):
        return self.driver.find_element(*ConfirmPage.searchcountry)

    def CountryName(self):
        return self.driver.find_element(*ConfirmPage.country)

    def CheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def PurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def SuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.success)
