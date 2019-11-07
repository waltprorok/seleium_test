#!/usr/bin/env python3
from selenium import webdriver


class MTA(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def mta_sign_in(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000")
        click_link = driver.find_element_by_xpath('//*[@id="nav"]/div/ul/li[6]/a')
        click_link.click()
        email_inp = driver.find_element_by_xpath('//*[@id="email"]')
        email_inp.send_keys("teacher@domain.com")
        pw_inp = driver.find_element_by_xpath('//*[@id="password"]')
        pw_inp.send_keys("123456")
        submit_btn = driver.find_element_by_xpath('//*[@id="hideNavBar"]/div/div/div/div[2]/form/div[4]/div/button')
        submit_btn.click()

    def mta_log_out(self):
        driver = self.driver
        logout_link = driver.find_element_by_xpath('/html/body/div/nav/ul/li[3]/div/a[4]')
        logout_link.click()

    def tear_down(self):
        self.driver.close()


if __name__ == "__main__":
    Test = MTA()
    Test.mta_sign_in()
    Test.mta_log_out()
    Test.tear_down()
