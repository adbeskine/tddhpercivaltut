from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

# browser = webdriver.Chrome()
# browser.get('http://localhost:8000')
# 
# assert 'To-Do' in browser.title
# browser.quit()


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrive_it_later(self):

		# Alex has heard about a cool new online to-do app. He goes to check out its homepage
		self.browser.get('http://localhost:8000')
	
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

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: buy peacock feathers' for row in rows), 
			"New to-do item did not appear in table"
			)
	
		# There is still a text box inviting her to add another item. She enters "Use peacock feathers to make a fly"
		self.fail('finish the test!')
	# The page updates and now shows both items on her list
	
	# Edith wonders whether the site will remember her list. Then she sees that
	# the site has generated a unique URL for her -- there is some explanatory text to that effect.
	
	# She isits that URL - her to-do list is still there.
	
	# Satisfied, she goes back to sleep

if __name__ == '__main__':
	unittest.main()