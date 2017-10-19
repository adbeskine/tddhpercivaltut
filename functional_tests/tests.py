from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import unittest

# browser = webdriver.Chrome()
# browser.get('http://localhost:8000')
# 
# assert 'To-Do' in browser.title
# browser.quit()
MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def tearDown(self):
		self.browser.quit()

	#-----HELPER METHODS-----#

	def wait_for_row_in_list_table(self, row_text):
		start_time = time.time()
		while True:
			try:
				table = self.browser.find_element_by_id('id_list_table')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return
			except(AssertionError, WebDriverException) as e:
				if time.time() - start_time > MAX_WAIT:
					raise e
				time.sleep(0.5)



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
		self.wait_for_row_in_list_table('1: buy peacock feathers')
	
		# There is still a text box inviting her to add another item. She enters "Use peacock feathers to make a fly"
		input_box = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')
		input_box.send_keys("use peacock feathers to make a fly")
		input_box.send_keys(Keys.ENTER)

		# The page updates and now shows both items on her list
		table = self.browser.find_element_by_id('id_list_table')
		rows= table.find_elements_by_tag_name('tr')
		self.wait_for_row_in_list_table('1: buy peacock feathers')
		self.wait_for_row_in_list_table('2: use peacock feathers to make a fly')
	
	# Edith wonders whether the site will remember her list. Then she sees that
	# the site has generated a unique URL for her -- there is some explanatory text to that effect.
		self.fail("finish this test!")


	# She visits that URL - her to-do list is still there.
	
	# Satisfied, she goes back to sleep

  #-----------------------------------------------------------------#

	def test_multiple_users_can_start_lists_at_different_urls(self):
		# Edith starts a new to-do list
		self.browser.get(self.live_server_url)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('buy peacock feathers')
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: buy peacock feathers')

		# She notices her list has a unique url
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')

		# Now a new user, Francis, comes along to the site
		## We use a new browser to make sure that no info from edith's session (cookies etc) will come through
		self.browser.quit()
		self.browser = webdriver.Chrome()

		# Francis visits the home page. There is no sign of Edith's list
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)

		# Francis starts a new list by entering a new item
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('buy milk')
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: buy milk')

		# Francis gets his own unique url
		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url, edith_list_url)

		# Again, there is no trace of Edith's list
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('buy peacock feathers', page_text)
		self.assertIn('buy milk', page_text)