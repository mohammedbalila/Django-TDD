from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
    
    def tearDown(self):
        self.browser.quit()

    def test_goes_here(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('End of the test')

        
if __name__ == "__main__":
    unittest.main(warnings='ignore')  
