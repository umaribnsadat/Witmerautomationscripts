import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from NewMindnProject.Objectproperties.ObjectProperties import ObjectRepository  # Correct import


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
        wellness_link = wait.until(EC.element_to_be_clickable((By.XPATH, ObjectRepository.wellness_link_xpath)))
        wellness_link.click()

        time.sleep(3)

        Intolerance_Of_Uncertainty = wait.until(
            EC.element_to_be_clickable(ObjectRepository.work_stress_assessment_xpath))
        Intolerance_Of_Uncertainty.click()

        time.sleep(3)

        start_button = wait.until(EC.element_to_be_clickable((By.XPATH, ObjectRepository.start_button_xpath)))
        start_button.click()

        time.sleep(3)

        continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, ObjectRepository.Continue_locator)))
        continue_button.click()
        time.sleep(3)

        for i, answer in enumerate(answers, start=1):
            quest_locator = ObjectRepository.answer_locators.get(answer, (
                By.XPATH, ObjectRepository.get_question_xpath(answer)))
            quest_link = wait.until(EC.element_to_be_clickable(quest_locator))
            quest_link.click()
            time.sleep(1)

        # Click the submit button
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, ObjectRepository.submit_button_xpath)))
        submit_button.click()
        print("Submit button clicked after answering all questions")

        # Click the yes button after submit
        yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, ObjectRepository.yes_button_xpath)))
        yes_button.click()
        print("Yes button clicked successfully")

        # Click the download report button
        download_report_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, ObjectRepository.download_report_button_xpath)))
        download_report_button.click()
        print("Download Report button clicked successfully")

        time.sleep(10)

    def test_case_1(self):
        login_email = ObjectRepository.login_email
        login_password = ObjectRepository.login_password
        test_case_1_answers = [
            'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree',
            'Strongly Agree', 'Strongly Agree', 'Strongly Agree', 'Strongly Agree',
            'Strongly Agree',
            'Strongly Agree', 'Strongly Agree', 'Strongly Agree', 'Strongly Agree',
            'Strongly Agree',
            'Strongly Agree', 'Strongly Agree', 'Strongly Agree', 'Strongly Disagree',
            'Strongly Agree',
            'Strongly Agree']
        self.run_test_case(login_email, login_password, *test_case_1_answers)

    def test_case_2(self):
        login_email = ObjectRepository.login_email
        login_password = ObjectRepository.login_password
        test_case_2_answers = [
            'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree',
            'Strongly Agree', 'Strongly Agree', 'Strongly Agree', 'Strongly Agree', 'Strongly Agree',
            'Strongly Agree', 'Strongly Agree', 'Strongly Agree', 'Strongly Agree', 'Strongly Agree',
            'Strongly Agree', 'Strongly Agree', 'Strongly Agree', 'Strongly Disagree', 'Strongly Agree',
            'Agree']
        self.run_test_case(login_email, login_password, *test_case_2_answers)

    def test_case_3(self):
        login_email = ObjectRepository.login_email
        login_password = ObjectRepository.login_password
        test_case_3_answers = ['Disagree', 'Somewhat Agree', 'Disagree', 'Somewhat Agree', 'Agree', 'Somewhat Agree',
                               'Agree', 'Somewhat Agree', 'Agree', 'Somewhat Agree', 'Agree', 'Somewhat Agree', 'Agree',
                               'Somewhat Agree', 'Agree', 'Somewhat Agree', 'Agree', 'Somewhat Agree', 'Agree',
                               'Somewhat Agree']
        self.run_test_case(login_email, login_password, *test_case_3_answers)

    def test_case_4(self):
        login_email = ObjectRepository.login_email
        login_password = ObjectRepository.login_password
        test_case_4_answers = ['Agree', 'Agree', 'Agree', 'Agree', 'Disagree', 'Disagree', 'Disagree', 'Disagree',
                               'Disagree', 'Disagree', 'Disagree', 'Disagree', 'Disagree', 'Disagree', 'Disagree',
                               'Disagree', 'Disagree', 'Agree', 'Disagree', 'Disagree']
        self.run_test_case(login_email, login_password, *test_case_4_answers)


if __name__ == '__main__':
    unittest.main()
