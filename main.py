#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class MTA(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def mta_sign_in(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000")
        url = "/login"
        click_link = driver.find_element_by_xpath('//a[@href="' + url + '"]')
        click_link.click()
        email_inp = driver.find_element_by_name("email")
        email_inp.send_keys("waltprorok@gmail.com")
        pw_inp = driver.find_element_by_name("password")
        pw_inp.send_keys("123456")
        submit_btn = driver.find_element_by_type("submit")
        submit_btn.click()

    def click_wdw_page(self):
        driver = self.driver
        url = "/tickets/waltdisneyworld"
        click_link = driver.find_element_by_xpath('//a[@href="' + url + '"]')
        try:
            click_link.click()
        except NoSuchElementException:
            time.sleep(2)

    def click_wdw_link(self):
        driver = self.driver
        url = "/tickets/waltdisneyworld/seasonal"
        click_link = driver.find_element_by_xpath('//a[@href="' + url + '"]')
        click_link.click()

    def taw_log_out(self):
        driver = self.driver
        logout_link = driver.find_element_by_link_text("LOGOUT")
        logout_link.click()

    def tear_down(self):
        self.driver.close()


if __name__ == "__main__":
    Test = MTA()
    Test.mta_sign_in()
    # Test.click_wdw_page()
    # Test.click_wdw_link()
    # Test.taw_log_out()
    # Test.tear_down()


