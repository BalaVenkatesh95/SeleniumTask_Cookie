import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager



class CookieClass:
   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))





   # browser initiation and url navigation
   def initiation_function(self):
       try:
           self.driver.maximize_window()
           self.driver.get(self.url)
           return True
       except:
           print("ERROR : URL is incorrect/Network Error")
           return False


   # Quit browser
   def shutdown(self):
       if self.initiation_function():
           return self.driver.quit()
       else:
           return False

   def fetch_url(self):
       if self.initiation_function():
           return self.driver.current_url
       else:
           return False
   # Emulates login process of user
   def login_user(self):


       if self.initiation_function():
           username_field = self.driver.find_element('id', 'user-name')
           password_field = self.driver.find_element('id', 'password')
           login_button = self.driver.find_element('id', 'login-button')
           username_field.send_keys("standard_user")
           password_field.send_keys("secret_sauce")
           login_button.click()
           time.sleep(5)
       else:
           return False


   # Function to get cookie
   def display_cookies(self):
       if self.initiation_function() == True:
        print("Cookies:", self.driver.get_cookies())

   # Logout Function
   def logout(self):
       homepage_screen = self.driver.find_element('xpath', "//div[@class='app_logo' and contains(text(), 'Swag Labs')]")
       result = homepage_screen.is_displayed()
       if result == True:
           print("Landed on Homepage successfully")
       hamburger_button = self.driver.find_element('id', 'react-burger-menu-btn')
       hamburger_button.click()
       logout_button = self.driver.find_element('link text', 'Logout')
       logout_button.click()