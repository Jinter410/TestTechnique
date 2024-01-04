import os
import unittest
from api.selenium_api import SeleniumAPI
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class TestSeleniumAPI(unittest.TestCase):

    def setUp(self):
        """Initial setup for each test."""
        self.api = SeleniumAPI(headless=False)
        self.api.navigate("https://digitalkin.ai/")

    def tearDown(self):
        """Cleanup after each test."""
        self.api.close()

    def test_navigate(self):
        """Test the navigate function of the Selenium API."""
        self.assertIn("DigitalKin", self.api.driver.title)

    def test_button_click(self):
        """Test clicking a button and verifying class changes."""
        button_selector = ".background-pause-button.visible"
        self.api.click_element(button_selector)

        # Wait until button gets clicked
        WebDriverWait(self.api.driver, 10).until(
            lambda d: "visible" not in d.find_element(By.CSS_SELECTOR, ".background-pause-button").get_attribute("class")
        )

        # Check that the "visible" class is no longer present but that "background-pause-button" still exists
        button_after_click = self.api.driver.find_element(By.CSS_SELECTOR, ".background-pause-button")
        self.assertNotIn("visible", button_after_click.get_attribute("class"))
        self.assertIn("background-pause-button", button_after_click.get_attribute("class"))

    def test_execute_script(self):
        """Test the execute script function of the Selenium API."""
        text = self.api.execute_script("return document.querySelector('h2').textContent;")
        self.assertEqual("Libérez le temps humain", text.strip())

    def test_take_screenshot(self):
        """Test the take screenshot function of the Selenium API."""
        screenshot_file = "test_screenshot.png"
        self.api.take_screenshot(screenshot_file)
        self.assertTrue(os.path.exists(screenshot_file))
        os.remove(screenshot_file)  # Clean up after the test

if __name__ == '__main__':
    unittest.main()
