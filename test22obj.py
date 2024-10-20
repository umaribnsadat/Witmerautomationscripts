import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from object_repository import ObjectRepository  # Import the object repository


class TestMindn(unittest.TestCase):
    def setUp(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument(r"--executable-path=C:\selenium driver\chromedriver.exe")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def login(self, email, password):
        wait = WebDriverWait(self.driver, 20)
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ObjectRepository.login_button_css)))
        self.driver.find_element(By.NAME, ObjectRepository.login_email_name).send_keys(email)
        self.driver.find_element(By.NAME, ObjectRepository.login_password_name).send_keys(password)
        login_button.click()

    def run_test_case(self, email, password, *answers):
        self.driver.get("https://default.mindn.ai/")
        self.login(email, password)

        wait = WebDriverWait(self.driver, 20)
        wellness_link = wait.until(EC.element_to_be_clickable((By.XPATH, ObjectRepository.wellness_link_xpath)))
        wellness_link.click()

        time.sleep(3)

        stress_link = wait.until(EC.element_to_be_clickable((By.XPATH, ObjectRepository.stress_link_xpath)))
        stress_link.click()

        time.sleep(3)

        resilience_link = wait.until(EC.element_to_be_clickable((By.XPATH, ObjectRepository.start_assessment_button_xpath)))
        resilience_link.click()

        time.sleep(3)

        start_link = wait.until(EC.element_to_be_clickable((By.XPATH, ObjectRepository.start_button_xpath)))
        start_link.click()

        for i, answer in enumerate(answers, start=1):
            quest_link = wait.until(EC.element_to_be_clickable((By.XPATH, ObjectRepository.get_question_xpath(answer))))
            quest_link.click()
            time.sleep(4)

        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, ObjectRepository.submit_button_xpath)))
        submit_button.click()
        time.sleep(2)

        yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, ObjectRepository.yes_button_xpath)))
        yes_button.click()
        time.sleep(4)

        down_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, ObjectRepository.download_report_button_xpath)))
        down_button.click()
        print("Download Report button clicked successfully")

        time.sleep(10)

    def test_case_1(self):
        login_email = ObjectRepository.login_email
        login_password = ObjectRepository.login_password
        test_case_1_answers = ['Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree',
                               'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree',
                               'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree',
                               'Strongly Disagree', 'Strongly Agree', 'Strongly Agree', 'Strongly Agree',
                               'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree'
        ]
        self.run_test_case(login_email, login_password, *test_case_1_answers)

    def test_case_2(self):
        login_email = ObjectRepository.login_email
        login_password = ObjectRepository.login_password
        test_case_2_answers = ['Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree',
                               'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree',
                               'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree',
                               'Strongly Disagree', 'Strongly Disagree', 'Strongly Disagree',
                               'Strongly Disagree', 'Strongly Disagree', 'Strongly Agree',
                               'Strongly Agree', 'Strongly Agree', 'Strongly Disagree',
                               'Strongly Disagree', 'Strongly Disagree', 'Disagree'
        ]
        self.run_test_case(login_email, login_password, *test_case_2_answers)

    def test_case_3(self):
        login_email = ObjectRepository.login_email
        login_password = ObjectRepository.login_password
        test_case_3_answers = ['Agree', 'Agree', 'Agree', 'Agree', 'Agree', 'Agree',
                               'Agree', 'Agree', 'Agree', 'Agree', 'Disagree', 'Disagree',
                               'Disagree', 'Disagree', 'Disagree', 'Disagree', 'Disagree',
                               'Disagree', 'Disagree', 'Disagree'
        ]
        self.run_test_case(login_email, login_password, *test_case_3_answers)

    def test_case_4(self):
        login_email = ObjectRepository.login_email
        login_password = ObjectRepository.login_password
        test_case_4_answers = ['Strongly Agree', 'Strongly Agree', 'Strongly Agree',
                               'Strongly Agree', 'Strongly Agree', 'Strongly Agree',
                               'Strongly Agree', 'Strongly Agree', 'Strongly Agree',
                               'Strongly Agree', 'Strongly Agree', 'Strongly Agree',
                               'Strongly Agree', 'Strongly Disagree', 'Strongly Disagree',
                               'Strongly Disagree', 'Strongly Agree', 'Strongly Agree',
                               'Strongly Agree', 'Strongly Agree'
        ]
        self.run_test_case(login_email, login_password, *test_case_4_answers)


if __name__ == '__main__':
    unittest.main()
