import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
class GoogleSearchE2ETest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_google_search(self):
        driver = self.driver
        driver.get("https://www.google.com")
        self.assertIn("Google", driver.title)
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("PyUnit E2E testing")
        search_box.send_keys(Keys.RETURN)
        time.sleep(2) # Wait for results to load
        #results = driver.find_elements(By.CSS_SELECTOR, "div.g")
        results = driver.find_elements(By.CSS_SELECTOR, 'div#search .g')


        self.assertGreater(len(results), 0, "No search results found.")
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()