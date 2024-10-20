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

        Intolerance_Of_Uncertainty = wait.until(EC.element_to_be_clickable((By.XPATH, ObjectRepository.intolerance_uncertainty_assessment_xpath)))
        Intolerance_Of_Uncertainty.click()

        time.sleep(3)



        start_button = wait.until(EC.element_to_be_clickable((By.XPATH, ObjectRepository.start_button_xpath)))
        start_button.click()

        time.sleep(3)

        for i, answer in enumerate(answers, start=1):
            quest_locator = ObjectRepository.answer_locators.get(answer, (By.XPATH, ObjectRepository.get_question_xpath(answer)))
            quest_link = wait.until(EC.element_to_be_clickable(quest_locator))
            quest_link.click()
            time.sleep(1)

            # Click "OK" button after the 9th answer in test case 1
            if i == 9:
                try:
                    ok_button = wait.until(EC.element_to_be_clickable(ObjectRepository.ok_locator))
                    ok_button.click()
                    time.sleep(2)
                except:
                    print("OK button not found, continuing with the test.")

        # Click the submit button
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, ObjectRepository.submit_button_xpath)))
        submit_button.click()
        print("Submit button clicked after answering all questions")

        # Click the yes button after submit
        yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, ObjectRepository.yes_button_xpath)))
        yes_button.click()
        print("Yes button clicked successfully")

        # Click the OK button after submit
        ok_button = wait.until(EC.element_to_be_clickable(ObjectRepository.ok_locator))
        ok_button.click()
        print("OK button clicked successfully after submit")

        # Click the download report button
        download_report_button = wait.until(EC.element_to_be_clickable((By.XPATH, ObjectRepository.download_report_button_xpath)))
        download_report_button.click()
        print("Download Report button clicked successfully")

        time.sleep(10)

    def test_case_1(self):
        login_email = ObjectRepository.login_email
        login_password = ObjectRepository.login_password
        test_case_1_answers = ['Completely characteristic of me'] * 20  # Repeat 'Completely characteristic of me' twenty times
        self.run_test_case(login_email, login_password, *test_case_1_answers)

    def test_case_2(self):
        login_email = ObjectRepository.login_email
        login_password = ObjectRepository.login_password
        test_case_2_answers = (['Not at all'] * 8) + ['Several days']  # Repeat 'Not at all' eight times and add 'Several days' once
        self.run_test_case(login_email, login_password, *test_case_2_answers)

    def test_case_3(self):
        login_email = ObjectRepository.login_email
        login_password = ObjectRepository.login_password
        test_case_3_answers = ['Not at all'] * 7 + ['More than half the days'] + ['Nearly everyday']
        self.run_test_case(login_email, login_password, *test_case_3_answers)

    def test_case_4(self):
        login_email = ObjectRepository.login_email
        login_password = ObjectRepository.login_password
        test_case_4_answers = ('Not at all', 'Not at all', 'Not at all', 'Not at all', 'Not at all',
                               'More than half the days', 'Nearly everyday', 'More than half the days',
                               'Nearly everyday')
        self.run_test_case(login_email, login_password, *test_case_4_answers)

    def test_case_5(self):
        login_email = ObjectRepository.login_email
        login_password = ObjectRepository.login_password
        test_case_5_answers = (
            'Not at all', 'Not at all', 'Not at all', 'More than half the days', 'Nearly everyday',
            'More than half the days', 'Nearly everyday', 'More than half the days', 'Nearly everyday')
        self.run_test_case(login_email, login_password, *test_case_5_answers)

    def test_case_6(self):
        login_email = ObjectRepository.login_email
        login_password = ObjectRepository.login_password
        test_case_6_answers = (
            'Not at all', 'More than half the days', 'Nearly everyday', 'More than half the days',
            'Nearly everyday', 'More than half the days', 'Nearly everyday', 'More than half the days',
            'Nearly everyday')
        self.run_test_case(login_email, login_password, *test_case_6_answers)


if __name__ == '__main__':
    unittest.main()
