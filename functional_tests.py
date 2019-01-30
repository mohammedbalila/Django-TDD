from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_goes_here(self):
        # Home page
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)

        # test header contentx
        header = self.browser.find_element_by_tag_name('h1')
        self.assertEqual('To-Do', header.text)

        # testing user input "the to do input feild"
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual('Enter a to-do item',
                         inputbox.get_attribute('placeholder'))
        # simulates typing in the input feild
        inputbox.send_keys('Buy some milk!')
        # simulates hitting enter
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('A new list item')
        self.fail('End of the test')


if __name__ == "__main__":
    unittest.main(warnings='ignore')
