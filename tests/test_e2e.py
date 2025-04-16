from selenium.webdriver.common.by import By
from Utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)

        #Checkout Page
        checkoutpage = homepage.shopItems()
        log.info("getting all the card titles")
        cards = checkoutpage.getCardTitles()
        for card in cards:
            productName = card.find_element(By.XPATH, "div/h4/a").text
            log.info(productName)
            if productName == "Blackberry":
                card.find_element(By.XPATH, "div/button").click()

        checkout_button = checkoutpage.ItemsCheckout()
        checkout_button.click()
        log.info(checkoutpage.TitleName().text)

        # ConfirmPage
        confirmpage = checkoutpage.lastItems()
        log.info("Entering country name as Ind")
        confirmpage.SearchCountry().send_keys("Ind")
        self.verifyLinkPresence("India")
        confirmpage.CountryName().click()
        confirmpage.CheckBox().click()
        confirmpage.PurchaseButton().click()
        message = confirmpage.SuccessMessage().text
        log.info("Text received from application"+message)
        assert "Success!" in message
        self.driver.close()