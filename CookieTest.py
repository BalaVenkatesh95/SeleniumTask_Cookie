"""
 Test case file with all required test cases to execute
"""
import time

from Cookie_Functions import CookieClass
import pytest



url = "https://www.saucedemo.com/"
#Creating Instance of SauceDemoClass to utilise its methods / functions
cookie = CookieClass(url)

# Test case to navigate to URL

def test_navigate_url():
   testing_url = "https://www.saucedemo.com/"
   assert cookie.fetch_url() == testing_url
print("Landed on login page")

def test_cookies_before_login():
   cookie.display_cookies()

#Test Case for login
def test_cookies_after_login():
   cookie.login_user()
   cookie.display_cookies()


def test_logout():
   cookie.login_user()
   cookie.logout()

#Test Case to quit / shutdown browser
def test_shutdown():
   cookie.shutdown()
