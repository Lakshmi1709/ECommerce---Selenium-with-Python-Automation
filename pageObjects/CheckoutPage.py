import time

from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    cardCheckout = (By.CSS_SELECTOR, ".btn-primary")
    titlename = (By.LINK_TEXT, "Blackberry")
    checkout_button = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)
        #products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    def ItemsCheckout(self):
        return self.driver.find_element(*CheckoutPage.cardCheckout)

    def TitleName(self):
        return self.driver.find_element(*CheckoutPage.titlename)

    def lastItems(self):
        self.driver.find_element(*CheckoutPage.checkout_button).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage