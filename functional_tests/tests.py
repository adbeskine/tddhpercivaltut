from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

# browser = webdriver.Chrome()
# browser.get('http://localhost:8000')
# 
# assert 'To-Do' in browser.title
# browser.quit()


class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def tearDown(self):
		self.browser.quit()

	#-----HELPER METHODS-----#

	def check_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])



	def test_can_start_a_list_and_retrive_it_later(self):

		# Alex has heard about a cool new online to-do app. He goes to check out its homepage
		self.browser.get(self.live_server_url)
	
		# He notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# He is invited to enter a to-do item straight away
		input_box = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')

	
		# he types "buy peacock feathers" into a text box
		input_box.send_keys('buy peacock feathers')
	
		# when he hits enter, the page updates, and now the page lists
		# "1: buy peacock feathers" as an item in a to-do list

		input_box.send_keys(Keys.ENTER)
		time.sleep(1)

		self.check_row_in_list_table('1: buy peacock feathers')
	
		# There is still a text box inviting her to add another item. She enters "Use peacock feathers to make a fly"
		input_box = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')
		input_box.send_keys("use peacock feathers to make a fly")
		input_box.send_keys(Keys.ENTER)

		# The page updates and now shows both items on her list
		table = self.browser.find_element_by_id('id_list_table')
		rows= table.find_elements_by_tag_name('tr')
		time.sleep(1)
		self.check_row_in_list_table('1: buy peacock feathers')
		self.check_row_in_list_table('2: use peacock feathers to make a fly')
	
	# Edith wonders whether the site will remember her list. Then she sees that
	# the site has generated a unique URL for her -- there is some explanatory text to that effect.
		self.fail("finish the test!")


	# She visits that URL - her to-do list is still there.
	
	# Satisfied, she goes back to sleep
