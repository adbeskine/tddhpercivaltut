from selenium import webdriver
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
		self.fail('Finish the test!')
	
	# He is invited to enter a to-do item straight away
	
	# he types "buy peacock feathers" into a text box
	
	# when he hits enter, the page updates, and now the page lists
	# "1: Buy peacock feathers" as an item in a to-do list
	
	# There is still a text box inviting her to add another item. She enters "Use peacock feathers to make a fly"
	
	# The page updates and now shows both items on her list
	
	# Edith wonders whether the site will remember her list. Then she sees that
	# the site has generated a unique URL for her -- there is some explanatory text to that effect.
	
	# She isits that URL - her to-do list is still there.
	
	# Satisfied, she goes back to sleep

if __name__ == '__main__':
	unittest.main()