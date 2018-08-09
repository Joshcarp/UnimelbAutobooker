# Written by Joshua Carpeggiani for educational use,
# Only supports same day booking, but will try book for any time and any resource,
# code found on github at https://github.com/Joshcarp/UnimelbAutobooker/upload/master



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
import getpass

now = datetime.datetime.now().day
def book_it(user, passwd):
    browser = webdriver.Chrome()
    browser.get("https://bookit.unimelb.edu.au/cire/login.aspx")
    time.sleep(3)
    username = browser.find_element_by_id("username_box")
    password = browser.find_element_by_id("password_box")
    username.send_keys(user)
    password.send_keys(passwd)
    # login via button
    browser.find_element_by_id('login_cmd').click()
    # go to quickbooking
    time.sleep(2)
    browser.get("https://bookit.unimelb.edu.au/MyPC/QuickBooking.htm")
    time.sleep(2)
    
    for resource in [
    '//*[@id="resourceTypeId"]/option[4]', # try for project room
    '//*[@id="resourceTypeId"]/option[2]' # if that doesnt work, try for booth
    ]:
        commands = [
                    '//*[@id="fcb_specific_btn_Where"]', '//*[@id="siteId"]/option[2]',
                    '//*[@id="locationId"]/option[1]', '//*[@id="fcb_specific_btn_What"]',
                    resource, '//*[@id="fcb_specific_btn_When"]',
                    '//*[@id="quick_startTime"]/option[3]'
                    ]
        for command in commands:
            time.sleep(1)
            a = browser.find_element_by_xpath(command)
            time.sleep(1)
            a.click()
        length_attempt = []
        time.sleep(3)
        #    a = browser.find_element_by_xpath('//*[@id="qb_whenDatePicker"]/div/table/tbody/tr[3]/td[7]/a')
        #    time.sleep(1)
        #    a.click()
        for i in [4,3,2,1]:
            try:
                a = browser.find_element_by_xpath(f'//*[@id="quick_bookingDuration"]/option[{i}]')
                a.click()
                time.sleep(3)
                a = browser.find_element_by_xpath('//*[@id="qb_find_button"]')
                a.click()
                time.sleep(3)
                a = browser.find_element_by_xpath('//*[@id="qb_results_yes"]')
                time.sleep(1)
                a.click()
            except:
                pass


if input("Please note I am not responsible for any data breaches or password\
         information theft, press y if you accept:").lower() == 'y':
    user = input('Enter your Unimelb username:')
    password = getpass.getpass('Enter your Unimelb password:')
    book_it(user, password)