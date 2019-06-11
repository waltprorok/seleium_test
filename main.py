import unittest
from selenium import webdriver


class TicketsAtWorkSignIn(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def taw_sign_in(self):
        driver = self.driver
        driver.get("https://ticketsatwork.com")
        email_inp = driver.find_element_by_name("login_email")
        email_inp.send_keys("wprorok@entertainmentbenefits.com")
        pw_inp = driver.find_element_by_name("login_password")
        pw_inp.send_keys("Admin213!")
        sumbit_btn = driver.find_element_by_name("submit")
        sumbit_btn.click()

    def taw_click_page(self):
        driver = self.driver
        click_product = driver.find_element_by_link_text('Walt Disney World®')
        click_product.click()

    def click_wdw_link(self):
        driver = self.driver
        url = "/tickets/waltdisneyworld/seasonal"
        click_link = driver.find_element_by_xpath(
            '//a[@href="' + url + '"]')
        click_link.click()

    def taw_log_out(self):
        driver = self.driver
        logout_link = driver.find_element_by_link_text("LOGOUT")
        logout_link.click()

    def tear_down(self):
        self.driver.close()


if __name__ == "__main__":
    Test = TicketsAtWorkSignIn()
    Test.setUp()
    Test.taw_sign_in()
    Test.taw_click_page()
    Test.click_wdw_link()
    Test.taw_log_out()
    Test.tear_down()
