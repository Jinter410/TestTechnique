from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

class SeleniumAPI:
    """A simple API class to interact with Selenium..

    Attributes:
        driver (webdriver): The WebDriver instance for browser interaction.
    """

    def __init__(self, headless=False):
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")

        prefs = {
            "profile.default_content_setting_values.notifications": 2, 
            "profile.default_content_setting_values.geolocation": 2,
            "profile.default_content_setting_values.media_stream": 2,  
        }
        chrome_options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(options=chrome_options)

    def navigate(self, url):
        """Navigate to a specified URL.

        Args:
            url (str): The URL to navigate to.
        """
        self.driver.get(url)
        # Wait for the page to load
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete'
        )
    
    def click_element(self, selector):
        """Click an element located by the selector.

        Args:
            selector (str): The CSS selector for the element to click.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        )
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        element.click()


    def take_screenshot(self, filename):
        """Take a screenshot of the current page and save it to a specified file.

        Args:
            filename (str): The name of the file to save the screenshot to.
        """
        self.driver.save_screenshot(filename)
    
    def execute_script(self, script):
        """Execute a JavaScript script on the current page.

        Args:
            script (str): The JavaScript code to execute.
        """
        return self.driver.execute_script(script)


    def close(self):
        """Closes the WebDriver and the browser."""
        self.driver.quit()

    def read_instructions(self, json_file_path):
        """Read and return instructions from a JSON file.

        Args:
            json_file_path (str): The path to the JSON file containing instructions.
        """
        with open(json_file_path, 'r') as json_file:
            instructions = json.load(json_file)
        return instructions

    def execute_instructions(self, instructions):
        """Execute a set of instructions read from a JSON file.

        Args:
            instructions (dict): A dictionary containing the instructions.
        """
        for action in instructions["actions"]:
            if action["type"] == "navigate":
                self.navigate(action["url"])
            elif action["type"] == "click":
                self.click_element(action["selector"])
            elif action["type"] == "execute_script":
                print(self.execute_script(action["script"]))
            elif action["type"] == "screenshot":
                self.take_screenshot(action["filename"])