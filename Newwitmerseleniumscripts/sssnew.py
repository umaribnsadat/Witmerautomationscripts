import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestMindn(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(r"--executable-path=C:\selenium driver\chromedriver.exe")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_mindn_valid_login(self):
        # Navigate to the website
        self.driver.get("https://default.mindn.ai/")

        # Wait for the login button to be present
        login_button_locator = (By.CSS_SELECTOR, ".btn.text-uppercase.login-new-btn")
        wait = WebDriverWait(self.driver, 20)
        login_button = wait.until(EC.element_to_be_clickable(login_button_locator))

        # Input the email into the "email" input field
        email_address = "umarhussain4046@gmail.com"
        self.driver.find_element(By.NAME, "email").send_keys(email_address)

        # Input the password into the "password" input field
        password_value = "Dellm3800$"
        self.driver.find_element(By.NAME, "password").send_keys(password_value)

        # Click the login button
        login_button.click()

        # Wait for the page to load after login (adjust the timeout if needed)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='work-life-heading text-center container']//h2[@class='main-section-title m-0']")))

        # Check the text on the page after login
        expected_text = "TAP INTO THE INFINITE POTENTIAL OF YOUR MIND"
        actual_text = self.driver.find_element(By.XPATH, "//div[@class='work-life-heading text-center container']//h2[@class='main-section-title m-0']").text

        # Use the correct XPath expression for assertion
        self.assertEqual(actual_text, expected_text, f"Assertion failed: Expected '{expected_text}', but got '{actual_text}'")

    def test_mindn_wrong_login(self):
        self.driver.get("https://default.mindn.ai/")

        # Wait for the login button to be present
        login_button_locator = (By.CSS_SELECTOR, ".btn.text-uppercase.login-new-btn")
        wait = WebDriverWait(self.driver, 20)
        login_button = wait.until(EC.element_to_be_clickable(login_button_locator))

        # Input the email into the "email" input field
        email_address = "umarhussain4046@gmal.com"  # Replace with your actual email address
        self.driver.find_element(By.NAME, "email").send_keys(email_address)

        # Input the password into the "password" input field
        password_value = "Dellm3800"  # Replace with your actual password
        self.driver.find_element(By.NAME, "password").send_keys(password_value)

        # Click the login button
        login_button.click()

        # Wait for the page to load after login (adjust the timeout if needed)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='work-life-heading text-center container']//h2[@class='main-section-title m-0']")))

        # Add assertions or checks for a wrong login attempt if needed

if __name__ == "__main__":
    unittest.main()