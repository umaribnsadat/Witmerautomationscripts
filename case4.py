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

    def wait_and_click(self, locator, timeout=20):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            element.click()
            return element
        except StaleElementReferenceException:
            print(f"StaleElementReferenceException occurred. Trying to re-locate element {locator}.")
            return self.wait_and_click(locator, timeout)
        except Exception as e:
            print(f"Error waiting for element {locator}: {e}")
            return None

    def find_ok_button(self):
        ok_button_locator_candidates = [
            (By.XPATH, "//button[normalize-space()='OK']"),
            (By.XPATH, "//button[contains(text(), 'OK')]"),
            (By.XPATH, "//button[contains(@class, 'ok-button')]")
        ]

        for locator in ok_button_locator_candidates:
            try:
                ok_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
                return ok_button
            except TimeoutException:
                continue

        return None

    def stress_tests(self, *answers):
        answer_locators = {
            'Always': (By.XPATH, "//label[normalize-space()='Always']"),
            'Never': (By.XPATH, "//label[normalize-space()='Never']"),
            'Strongly Agree': (By.XPATH, "//label[normalize-space()='Strongly Agree']"),
            'Agree': (By.XPATH, "//label[text()='Agree ']"),
            'Strongly Disagree': (By.XPATH, "//label[normalize-space()='Strongly Disagree']"),
            'Often': (By.XPATH, "//label[text()='Often']"),
            'Rarely': (By.XPATH, "//label[normalize-space()='Rarely']"),
            'Disagree': (By.XPATH, "//label[text()='Disagree']"),
            'Neither Agree or Disagree': (By.XPATH, "//input[@value='Neither Agree nor Disagree']")
        }

        try:
            self.login("umarhussain4046@gmail.com", "Dellm3800$")

            # Check for both "Retake Assessment" and "Take Assessment" buttons and click on the one that exists
            assessment_locators = [
                (By.XPATH, "//button[normalize-space()='Retake Assessment']"),
                (By.XPATH, "//button[normalize-space()='Take Assessment']")
            ]

            for locator in assessment_locators:
                try:
                    assessment_loc = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
                    assessment_loc.click()
                    break  # Clicked one of the buttons, so exit the loop
                except TimeoutException:
                    continue  # Continue to the next locator if this one is not found within the timeout

            time.sleep(3)

            start_locator = (By.XPATH, "//button[normalize-space()='Start']")
            start_loc = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(start_locator))
            start_loc.click()

            time.sleep(3)

            Continue_locator = (By.XPATH, "//button[@class='ass-start-btn note-button text-uppercase']")
            Continue_loc = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(Continue_locator))
            Continue_loc.click()

            # Click on answers for questions 1 to 54
            # Adjusted part of the stress_tests method

            # Click on answers for questions 1 to 54
            for i in range(1, 55):
                current_answer = answers[i - 1]
                quest_locator = (By.XPATH, f"//label[normalize-space()='{current_answer}']")
                try:
                    quest_link = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(quest_locator))
                    time.sleep(1)
                    quest_link.click()
                    time.sleep(1)  # Consider reducing or conditionally applying this to improve test speed
                except TimeoutException:
                    print(f"TimeoutException occurred while waiting for element {quest_locator}")

                # Correct the condition to click on OK button for question 14
                if i == 13:
                    ok_button_14 = self.find_ok_button()
                    if ok_button_14:
                        ok_button_14.click()
                        print("OK button for question 14 clicked successfully")

                # Correct the condition to click on OK button for question 23
                if i == 22:
                    ok_button_23 = self.find_ok_button()
                    if ok_button_23:
                        ok_button_23.click()
                        print("OK button for question 23 clicked successfully")

                # Check if this is the last question
                if i == 54:
                    # Check if the last answer was clicked successfully
                    last_answer_clicked = self.wait_and_click(quest_locator, timeout=30)
                    if last_answer_clicked:
                        print("Last answer for question 54 clicked successfully")
                        time.sleep(2)  # Wait for 2 seconds after clicking the last answer
                    else:
                        print("Error: Last answer for question 54 not clicked")
                        self.fail("Test case failed: Last answer for question 54 not clicked")

            # After all questions have been answered
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
        self.stress_tests(

            'Never', 'Never', 'Never', 'Never', 'Often', 'Always', 'Often', 'Often', 'Always', 'Often',
            'Sometimes', 'Always', 'Often', 'Often', 'Always', 'Sometimes', 'Sometimes', 'Never', 'Always',
            'Often', 'Always', 'Sometimes', 'Agree', 'Agree', 'Strongly Agree', 'Neither Agree nor Disagree',
            'Agree', 'Agree', 'Strongly Disagree', 'Agree', 'Neither Agree nor Disagree', 'Strongly Agree',
            'Agree', 'Agree', 'Agree', 'Strongly Agree', 'Neither Agree nor Disagree', 'Strongly Agree', 'Disagree',
            'Strongly Agree', 'Strongly Disagree', 'Neither Agree nor Disagree', 'Strongly Agree', 'Strongly Disagree',
            'Agree', 'Strongly Disagree', 'Strongly Agree', 'Strongly Disagree', 'Disagree', 'Neither Agree nor Disagree',
            'Disagree', 'Strongly Disagree', 'Strongly Disagree', 'Agree'
        )


if __name__ == "__main__":
    unittest.main()
