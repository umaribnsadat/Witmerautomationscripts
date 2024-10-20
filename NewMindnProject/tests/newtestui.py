import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestMindn(unittest.TestCase):
    def setUp(self):
        # Setup WebDriver with Chrome options
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument(r"--executable-path=C:\selenium driver\chromedriver.exe")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser after the test case
        self.driver.quit()

    def login(self, email, password):
        wait = WebDriverWait(self.driver, 20)
        print("Waiting for login button...")
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.text-uppercase.login-new-btn")))
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        login_button.click()
        print("Logged in successfully.")

    def click_using_xpath(self, element_xpath, retries=3):
        """
        Click an element using regular XPath with retries
        :param element_xpath: XPath of the element to click
        :param retries: Number of retry attempts before failing
        """
        wait = WebDriverWait(self.driver, 20)
        for attempt in range(retries):
            try:
                print(f"Attempt {attempt + 1} to click element using XPath.")
                # Wait for the element to be clickable
                element = wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
                element.click()
                print(f"Clicked on element using XPath: {element_xpath}")
                return True
            except Exception as e:
                print(f"Failed to click element on attempt {attempt + 1}, Error: {e}")
                time.sleep(2)  # Wait before retrying
        return False

    def click_using_js_executor(self, element_xpath):
        """
        Click an element using JavaScriptExecutor
        :param element_xpath: XPath of the element to click
        """
        try:
            # Find the element using the provided XPath
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, element_xpath))
            )

            # Scroll into view and click
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)
            print(f"Clicked on element using JS executor with XPath: {element_xpath}")
        except Exception as e:
            print(f"Failed to click using JS executor: {str(e)}")
            self.fail(f"Test failed because element with XPath {element_xpath} could not be clicked.")

    def click_start_button(self):
        """
        Click the Start button after the meditation option has been clicked.
        """
        try:
            wait = WebDriverWait(self.driver, 20)
            start_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Start']")))
            start_button.click()
            print("Clicked the Start button successfully.")
        except Exception as e:
            print(f"Failed to find or click the Start button: {str(e)}")
            self.fail("Start button not found or could not be clicked.")

    def test_case(self):
        # Login credentials
        login_email = "umarhussain4046@gmail.com"
        login_password = "Dellm3800$"

        # Open the website
        print("Opening the website...")
        self.driver.get("https://default.mindn.ai/")

        # Log in to the website
        self.login(login_email, login_password)

        # Click on 'Wellness' using normal XPath
        wellness_xpath = "//div[normalize-space()='Wellness']"
        self.click_using_xpath(wellness_xpath)

        time.sleep(2)

        # Click on 'Stress' using normal XPath
        stress_xpath = "//span[normalize-space()='Stress']"
        self.click_using_xpath(stress_xpath)

        time.sleep(2)

        # Scroll down to make the 'Meditation' section visible
        print("Scrolling down to the Meditation section...")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        # Click the 'Meditation' next arrow 3 times with a 3-second wait between each click
        meditation_next_button_xpath = "//button[@role='presentation' and @class='owl-next']"
        for _ in range(3):
            self.click_using_js_executor(meditation_next_button_xpath)
            time.sleep(3)

        # Click on the "Forest Serenity" option using JS Executor
        forest_serenity_xpath = "//h5[normalize-space()='Forest Serenity']"
        self.click_using_js_executor(forest_serenity_xpath)

        time.sleep(2)

        # Try to click the Start button after selecting Forest Serenity
        self.click_start_button()


if __name__ == '__main__':
    unittest.main()
