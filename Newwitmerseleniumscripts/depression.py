import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.text-uppercase.login-new-btn")))
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        login_button.click()

    def run_test_case(self, email, password, *answers):
        self.driver.get("https://default.mindn.ai/")
        self.login(email, password)

        wellness_locator = (By.XPATH, "//div[normalize-space()='Wellness']")
        wait = WebDriverWait(self.driver, 20)
        wellness_link = wait.until(EC.element_to_be_clickable(wellness_locator))
        wellness_link.click()

        time.sleep(3)

        stress_link_locator = (By.XPATH, "//span[normalize-space()='Depression']")
        stress_link = wait.until(EC.element_to_be_clickable(stress_link_locator))
        stress_link.click()

        time.sleep(3)

        resilience_locator = (By.XPATH, "//button[normalize-space()='Start Assessment']")
        resilience_link = wait.until(EC.element_to_be_clickable(resilience_locator))
        resilience_link.click()

        time.sleep(3)

        start_locator = (By.XPATH, "//button[normalize-space()='Start']")
        start_link = wait.until(EC.element_to_be_clickable(start_locator))
        start_link.click()

        time.sleep(3)

        for i, answer in enumerate(answers, start=1):
            quest_locator = (By.XPATH, f"//label[normalize-space()='{answer}']")
            quest_link = wait.until(EC.element_to_be_clickable(quest_locator))
            quest_link.click()
            time.sleep(4)

            # Click "OK" button after the 9th answer in test case 1
            if i == 9:
                try:
                    ok_button_locator = (By.XPATH, "//button[normalize-space()='OK']")
                    ok_button = wait.until(EC.element_to_be_clickable(ok_button_locator))
                    ok_button.click()
                    time.sleep(2)
                except:
                    print("OK button not found, continuing with the test.")

        submit_button_locator = (By.XPATH, '//button[@type="submit"]')
        submit_button = wait.until(EC.element_to_be_clickable(submit_button_locator))
        submit_button.click()
        time.sleep(2)

        yes_button_locator = (By.XPATH, "//button[normalize-space()='Yes']")
        yes_button = wait.until(EC.element_to_be_clickable(yes_button_locator))
        yes_button.click()
        time.sleep(4)

        down_locator = (By.XPATH, "//button[normalize-space()='Download Report']")
        down_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(down_locator))
        down_button.click()
        print("Download Report button clicked successfully")

        time.sleep(9)

    def test_case_1(self):
        login_email = "umarhussain4046@gmail.com"
        login_password = "Dellm3800$"
        test_case_1_answers = ['Not at all'] * 9  # Repeat 'Not at all' nine times
        self.run_test_case(login_email, login_password, *test_case_1_answers)

    def test_case_2(self):
        login_email = "umarhussain4046@gmail.com"
        login_password = "Dellm3800$"
        test_case_2_answers = (['Not at all'] * 8) + ['Several days']  # Repeat 'Not at all' eight times and add 'Several days' once
        self.run_test_case(login_email, login_password, *test_case_2_answers)

    def test_case_3(self):
        login_email = "umarhussain4046@gmail.com"
        login_password = "Dellm3800$"
        test_case_3_answers = ['Not at all'] * 7 + ['More than half the days'] + ['Nearly everyday']
        self.run_test_case(login_email, login_password, *test_case_3_answers)

    def test_case_4(self):
        login_email = "umarhussain4046@gmail.com"
        login_password = "Dellm3800$"
        test_case_4_answers = ('Not at all', 'Not at all', 'Not at all', 'Not at all', 'Not at all',
                               'More than half the days', 'Nearly everyday', 'More than half the days',
                               'Nearly everyday')
        print(test_case_4_answers)

        self.run_test_case(login_email, login_password, *test_case_4_answers)

    def test_case_5(self):
        login_password = "Dellm3800$"
        login_email = "umarhussain4046@gmail.com"
        test_case_5_answers = (
        'Not at all', 'Not at all', 'Not at all', 'More than half the days', 'Nearly everyday',
        'More than half the days', 'Nearly everyday', 'More than half the days', 'Nearly everyday')
        print(test_case_5_answers)
        self.run_test_case(login_email, login_password, *test_case_5_answers)

    def test_case_6(self):
        login_email = "umarhussain4046@gmail.com"
        login_password = "Dellm3800$"
        test_case_6_answers = (
        'Not at all', 'More than half the days', 'Nearly everyday', 'More than half the days',
        'Nearly everyday', 'More than half the days', 'Nearly everyday', 'More than half the days',
        'Nearly everyday')
        print(test_case_6_answers)

        self.run_test_case(login_email, login_password, *test_case_6_answers)

if __name__ == '__main__':
    unittest.main()
