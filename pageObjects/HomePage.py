from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    status = (By.ID, "inlineRadio2")
    submit_button = (By.CSS_SELECTOR, "input[value='Submit']")
    alert_message = (By.CLASS_NAME, "alert-success")



    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage
        #driver.find_element(By.LINK_TEXT, "Shop")

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getStatus(self):
        return self.driver.find_element(*HomePage.status)

    def SubmitButton(self):
        return self.driver.find_element(*HomePage.submit_button)

    def getAlert(self):
        return self.driver.find_element(*HomePage.alert_message)






