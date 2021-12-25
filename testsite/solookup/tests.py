from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .models import Boat

class BoatTest(TestCase):

    def test_string_rep(self):
        boat = Boat(so_num = 1)
        self.assertEqual(boat.so_num, 1)

        # test checks if boat saves its so_num

# class BoatAddTest(LiveServerTestCase):
# 	def testform(self):
# 		selenium = webdriver.Chrome()
# 		selenium.get('http://127.0.0.1:8000/solookup/newboat/')

# 		model_name = selenium.find_element_by_id('id_model')
# 		so_num = selenium.find_element_by_id('id_so_num')
# 		serial_num = selenium.find_element_by_id('id_serial_num')
# 		color = selenium.find_element_by_id('id_color')
# 		dealer_name = selenium.find_element_by_id('id_dealer_name')
# 		motor = selenium.find_element_by_id('id_motor')
# 		anti_strt = selenium.find_element_by_id('id_anticipated_Start')

# 		submit = selenium.find_element_by_id('submit_button')

# 		model_name.send_keys('1910-Bay')
# 		so_num.send_keys('123478')
# 		serial_num.send_keys('12345')
# 		color.send_keys('Blue')
# 		dealer_name.send_keys('70-WEST')
# 		motor.send_keys('Yamaha 360CC')
# 		anti_strt.send_keys('04/30/2021')

# 		submit.send_keys(Keys.RETURN)

# 		assert '123478' in selenium.page_source

class LoginTest(LiveServerTestCase):
	def testlogin(self):

		selenium = webdriver.Chrome()
		selenium.get('http://127.0.0.1:8000/accounts/login')

		username = selenium.find_element_by_id('id_username').send_keys('Intruder')
		psswrd = selenium.find_element_by_id('id_password').send_keys('12345')

		selenium.find_element_by_id('login_button').click()

		assert 'login' in selenium.page_source

class LoginTestSuccess(LiveServerTestCase):
	def testsuccess(self):

		selenium = webdriver.Chrome()
		selenium.get('http://127.0.0.1:8000/accounts/login')

		username = selenium.find_element_by_id('id_username').send_keys('aweber')
		psswrd = selenium.find_element_by_id('id_password').send_keys('Tidewater@1')

		# login = selenium.find_element_by_id('login_button')
		selenium.find_element_by_id('login_button').click()
		

		assert 'solookup' in selenium.page_source





