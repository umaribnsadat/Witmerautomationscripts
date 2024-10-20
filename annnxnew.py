import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException


class TestCases(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(r"--executable-path=C:\selenium driver\chromedriver.exe")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def login(self, email, password):
        self.driver.get("https://default.mindn.ai/")
        login_button_locator = (By.CSS_SELECTOR, ".btn.text-uppercase.login-new-btn")
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(login_button_locator))
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        login_button.click()

    def stress_tests(self, *answers):
        answer_locators = {
            'Not at all': (By.XPATH, "//label[normalize-space()='Not at all']"),
            'More than half the days': (By.XPATH, "//label[normalize-space()='More than half the days']"),
            'Nearly every day': (By.XPATH, "//label[normalize-space()='Nearly everyday']")
        }

        try:
            self.login("umarhussain4046@gmail.com", "Dellm3800$")
            wellness_locator = (By.XPATH, "//div[normalize-space()='Wellness']")
            wait = WebDriverWait(self.driver, 20)
            wellness_link = wait.until(EC.element_to_be_clickable(wellness_locator))
            wellness_link.click()

            time.sleep(3)

            stress_link_locator = (By.XPATH, "//span[normalize-space()='Anxiety']")
            stress_link = wait.until(EC.element_to_be_clickable(stress_link_locator))
            stress_link.click()

            time.sleep(3)

            dropdownloc_locator = (By.XPATH, "//button[contains(@class,'dropdown-toggle dropdown-toggle-split')]")
            dropdownloc_locator = wait.until(EC.element_to_be_clickable(dropdownloc_locator))
            dropdownloc_locator.click()

            time.sleep(5)

            sleepq_locator = (By.XPATH, "//a[normalize-space()='Anxiety']")
            sleepq_locator = wait.until(EC.element_to_be_clickable(sleepq_locator))
            sleepq_locator.click()
            time.sleep(6)

            resilience_locator = (By.XPATH, "//button[normalize-space()='Start Assessment']")
            resilience_link = wait.until(EC.element_to_be_clickable(resilience_locator))
            resilience_link.click()

            time.sleep(3)

            start_locator = (By.XPATH, "//button[normalize-space()='Start']")
            start_link = wait.until(EC.element_to_be_clickable(start_locator))
            start_link.click()

            time.sleep(3)

            for i, answer in enumerate(answers, start=1):
                quest_locator = answer_locators[answer]
                quest_link = wait.until(EC.element_to_be_clickable(quest_locator))
                quest_link.click()
                time.sleep(4)

                 # Check if this is the last question
                if i == 7:
                    # Check if the last answer was clicked successfully
                    last_answer_clicked = wait.until(EC.element_to_be_clickable(quest_locator))
                    if last_answer_clicked:
                        print("Last answer for question 54 clicked successfully")
                        time.sleep(2)  # Wait for 2 seconds after clicking the last answer
                    else:
                        print("Error: Last answer for question 54 not clicked")
                        self.fail("Test case failed: Last answer for question 54 not clicked")

            submit_button_locator = (By.XPATH, "//button[normalize-space()='Submit']")
            submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(submit_button_locator))
            submit_button.click()
            print("Submit button clicked after answering all questions")

            # Handle additional buttons (Yes and OK) if needed
            yes_locator = (By.XPATH, "//button[normalize-space()='Yes']")
            yes_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(yes_locator))
            yes_button.click()
            print("Yes button clicked successfully")

            ok_locator = (By.XPATH, "//button[normalize-space()='OK']")
            ok_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ok_locator))
            ok_button.click()
            print("OK button clicked successfully")

            down_locator = (By.XPATH, "//button[normalize-space()='Download Report']")
            down_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(down_locator))
            down_button.click()
            print("Download Report button clicked successfully")

            time.sleep(10)

        except Exception as e:
            print(f"Error in stress_tests: {e}")
            raise

    def test_case_1(self):
        login_email = "umarhussain4046@gmail.com"
        login_password = "Dellm3800$"
        test_case_1_answers = ['Not at all'] * 7  # Repeat 'Not at all' seven times
        self.run_test_case(login_email, login_password, *test_case_1_answers)

    def test_case_2(self):
        login_email = "umarhussain4046@gmail.com"
        login_password = "Dellm3800$"
        test_case_2_answers = (['Not at all'] * 6) + ['Several days']  # Repeat 'Not at all' six times and add 'Several days' once
        self.run_test_case(login_email, login_password, *test_case_2_answers)

    def test_case_3(self):
        login_email = "umarhussain4046@gmail.com"
        login_password = "Dellm3800$"
        test_case_3_answers = ['Not at all'] * 5 + ['More than half the days'] + ['Nearly everyday']
        self.stress_tests(*test_case_3_answers)  # Run the test case


if __name__ == '__main__':
    unittest.main()
