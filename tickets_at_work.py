#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

TICKETS_AT_WORK = "https://www.ticketsatwork.local/tickets/index.php"


class TicketsAtWork(object):

    def __init__(self):
        opts = Options()
        opts.headless = True
        self.driver = webdriver.Chrome(options=opts)
        self.driver.maximize_window()

    def taw_sign_in(self):
        driver = self.driver
        driver.get(TICKETS_AT_WORK)
        email_inp = driver.find_element_by_name("login_email")
        email_inp.send_keys("root@domain.com")
        pw_inp = driver.find_element_by_name("login_password")
        pw_inp.send_keys("cable")
        submit_btn = driver.find_element_by_name("submit")
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