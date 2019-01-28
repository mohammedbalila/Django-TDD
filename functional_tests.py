from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_goes_here(self):
        # Home page
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)

        # test header contentx
        header = self.browser.find_element_by_tag_name('h1')
        self.assertEqual('To-Do', header.text)

        # testing user input "the to do input feild"
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual('Enter a to do item',
                         inputbox.get_attribute('placeholder'))
        # simulates typing in the input feild
        inputbox.send_keys('Buy some milk!')
        # simulates hitting enter 
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy some milk!' for row in rows))
        self.fail('End of the test')


if __name__ == "__main__":
    unittest.main(warnings='ignore')
