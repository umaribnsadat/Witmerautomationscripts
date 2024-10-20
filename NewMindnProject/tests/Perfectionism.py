import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from NewMindnProject.Objectproperties.ObjectProperties import ObjectRepository


class TestMindn(unittest.TestCase):
    def setUp(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument(r"--executable-path=C:\\selenium driver\\chromedriver.exe")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def login(self, email, password):
        self.driver.get(ObjectRepository.login_url)
        wait = WebDriverWait(self.driver, 20)
        login_button = wait.until(EC.element_to_be_clickable(ObjectRepository.login_button_css))
        self.driver.find_element(*ObjectRepository.login_email_name).send_keys(email)
        self.driver.find_element(*ObjectRepository.login_password_name).send_keys(password)
        login_button.click()

    def run_test_case(self, email, password, *answers):
        self.login(email, password)

        wait = WebDriverWait(self.driver, 20)

        # Wellness Link
        wellness_link = wait.until(EC.element_to_be_clickable((By.XPATH, ObjectRepository.wellness_link_xpath)))
        wellness_link.click()

        time.sleep(3)

        # Work-life balance Link
        perfectionism_link = wait.until(EC.element_to_be_clickable(ObjectRepository.perfectionism_assessment_xpath))
        perfectionism_link.click()

        time.sleep(3)

        # Start Button
        start_button = wait.until(EC.element_to_be_clickable((By.XPATH, ObjectRepository.start_button_xpath)))
        start_button.click()

        time.sleep(3)

        # Continue Button

        # Answer Questions
        for answer in answers:
            quest_locator = ObjectRepository.answer_locators.get(answer, (
                By.XPATH, ObjectRepository.get_question_xpath(answer)))
            quest_link = wait.until(EC.element_to_be_clickable(quest_locator))
            quest_link.click()
            time.sleep(4)

        # Submit Button
        submit_button = wait.until(EC.element_to_be_clickable(ObjectRepository.submit_button_xpath))
        submit_button.click()
        time.sleep(2)

        # Yes Button
        yes_button = wait.until(EC.element_to_be_clickable(ObjectRepository.yes_button_xpath))
        yes_button.click()
        time.sleep(4)

        # Download Report Button
        download_report_button = wait.until(EC.element_to_be_clickable(ObjectRepository.download_report_button_xpath))
        download_report_button.click()
        print("Download Report button clicked successfully")

        time.sleep(9)

    def test_case_1(self):
        login_email = ObjectRepository.login_email
        login_password = ObjectRepository.login_password
        test_case_1_answers = [
            'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree',
            'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree',
            'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree',
            'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree',
            'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree'
        ]
        self.run_test_case(login_email, login_password, *test_case_1_answers)

    def test_case_2(self):
        login_email = ObjectRepository.login_email
        login_password = ObjectRepository.login_password
        test_case_2_answers = [
            'Neither Agree nor Disagree', 'Neither Agree nor Disagree', 'Neither Agree nor Disagree',
            'Neither Agree nor Disagree', 'Neither Agree nor Disagree', 'Neither Agree nor Disagree',
            'Neither Agree nor Disagree', 'Neither Agree nor Disagree', 'Neither Agree nor Disagree',
            'Disagree', 'Disagree', 'Disagree', 'Disagree', 'Disagree', 'Disagree', 'Disagree',
            'Disagree', 'Disagree', 'Disagree', 'Disagree'
        ]
        self.run_test_case(login_email, login_password, *test_case_2_answers)

    def test_case_3(self):
        login_email = ObjectRepository.login_email
        login_password = ObjectRepository.login_password
        test_case_3_answers = [
            'Neither Agree nor Disagree', 'Neither Agree nor Disagree', 'Neither Agree nor Disagree',
            'Neither Agree nor Disagree', 'Neither Agree nor Disagree', 'Neither Agree nor Disagree',
            'Neither Agree nor Disagree', 'Neither Agree nor Disagree', 'Neither Agree nor Disagree',
            'Neither Agree nor Disagree', 'Neither Agree nor Disagree', 'Neither Agree nor Disagree',
            'Disagree', 'Disagree', 'Disagree', 'Disagree', 'Disagree', 'Disagree', 'Disagree',
            'Disagree'
        ]
        self.run_test_case(login_email, login_password, *test_case_3_answers)

    def test_case_4(self):
        login_email = ObjectRepository.login_email
        login_password = ObjectRepository.login_password
        test_case_4_answers = [
            'Strongly Agree', 'Strongly Agree', 'Strongly Agree', 'Strongly Agree',
            'Strongly Agree', 'Strongly Agree', 'Strongly Agree', 'Strongly Agree',
            'Strongly Agree', 'Strongly Agree', 'Strongly Agree', 'Strongly Agree',
            'Strongly Agree', 'Strongly Agree', 'Strongly Agree', 'Strongly Agree',
            'Strongly Agree', 'Strongly Agree', 'Strongly Agree', 'Strongly Agree'
        ]
        self.run_test_case(login_email, login_password, *test_case_4_answers)


if __name__ == '__main__':
    unittest.main()
