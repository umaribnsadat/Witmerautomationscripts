import unittest
import time
from selenium import webdriver


class TestMindn(unittest.TestCase):

    def setUp(self):
        # Setup WebDriver with options
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument(r"--executable-path=C:\selenium driver\chromedriver.exe")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.maximize_window()

    def test_open_whatsapp_web(self):
        # Open WhatsApp Web and wait for 30 seconds
        self.driver.get("https://web.whatsapp.com")
        time.sleep(30)

    def tearDown(self):
        # Quit the driver after the test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
