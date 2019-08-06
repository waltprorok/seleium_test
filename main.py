#!/usr/bin/env python3
import tickets_at_work as taw


if __name__ == "__main__":
    Test = taw.TicketsAtWork()
    Test.taw_sign_in()
    Test.click_wdw_page()
    Test.click_wdw_link()
    Test.taw_log_out()
    Test.tear_down()
