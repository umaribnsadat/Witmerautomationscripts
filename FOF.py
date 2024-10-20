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

    def stress_tests(self, *answers):
        answer_locators = {
    'Do not believe at all': (By.XPATH, "//label[contains(text(),'Do not believe ')]"),
    'Believe 75% of the time': (By.XPATH, "//label[contains(normalize-space(), 'Believe 75%')]"),
    'Believe 25% of the time': (By.XPATH, "//label[contains(normalize-space(), 'Believe 25%')]"),
    'Believe 100% of the time': (By.XPATH, "//label[contains(normalize-space(), 'Believe 100%')]"),
    'Believe 50% of the time': (By.XPATH, "//label[contains(normalize-space(), 'Believe 50%')]")
        }

        self.driver.get("https://default.mindn.ai/")
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

        resilience_locator = (By.XPATH, "//button[normalize-space()='Start Assessment']")
        resilience_link = wait.until(EC.element_to_be_clickable(resilience_locator))
        resilience_link.click()

        time.sleep(3)

        start_locator = (By.XPATH, "//button[normalize-space()='Start']")
        start_link = wait.until(EC.element_to_be_clickable(start_locator))
        start_link.click()

        time.sleep(3)



        for i, answer in enumerate(answers, start=1):
            quest_locator = answer_locators.get(answer)
            if quest_locator:
                try:
                    quest_link = wait.until(EC.element_to_be_clickable(quest_locator))
                    quest_link.click()
                    time.sleep(2)  # Adjust the sleep time if necessary
                except Exception as e:
                    print(f"Error clicking answer: {e}")
            else:
                print(f"Answer locator not found for: {answer}")

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
        test_case_1_answers = [
            'Believe 100% of the time', 'Believe 100% of the time', 'Believe 100% of the time',
            'Believe 100% of the time', 'Believe 100% of the time', 'Believe 100% of the time',
            'Believe 100% of the time', 'Believe 100% of the time', 'Believe 100% of the time',
            'Believe 100% of the time', 'Believe 100% of the time', 'Believe 100% of the time',
            'Believe 100% of the time', 'Believe 100% of the time', 'Believe 100% of the time',
            'Believe 100% of the time', 'Believe 100% of the time', 'Believe 100% of the time',
            'Believe 100% of the time', 'Believe 100% of the time', 'Believe 100% of the time',
            'Believe 100% of the time', 'Believe 100% of the time', 'Believe 100% of the time',
            'Believe 100% of the time'
        ]
        self.stress_tests(*test_case_1_answers)

    def test_case_2(self):
        login_email = "umarhussain4046@gmail.com"
        login_password = "Dellm3800$"
        test_case_2_answers = [
            'Do not believe at all',
'Do not believe at all',
'Do not believe at all',
'Do not believe at all',
'Do not believe at all',
'Believe 75% of the time',
'Believe 75% of the time',
'Believe 75% of the time',
'Believe 75% of the time',
'Believe 75% of the time',
'Believe 75% of the time',
'Believe 75% of the time',
'Believe 75% of the time',
'Believe 75% of the time',
'Believe 75% of the time',
'Believe 75% of the time',
'Believe 75% of the time',
'Believe 75% of the time',
'Believe 100% of the time',
'Believe 100% of the time',
'Believe 25% of the time',
'Believe 25% of the time',
'Believe 50% of the time',
'Believe 50% of the time',
'Believe 75% of the time'
        ]
        self.stress_tests(*test_case_2_answers)

    def test_case_3(self):
        login_email = "umarhussain4046@gmail.com"
        login_password = "Dellm3800$"
        test_case_3_answers = [
            'Do not believe at all', 'Believe 25% of the time', 'Believe 50% of the time', 'Believe 50% of the time',
            'Believe 75% of the time', 'Do not believe at all', 'Believe 25% of the time', 'Believe 50% of the time',
            'Do not believe at all', 'Believe 75% of the time', 'Believe 100% of the time', 'Do not believe at all',
            'Do not believe at all', 'Believe 25% of the time', 'Do not believe at all', 'Believe 50% of the time',
            'Do not believe at all', 'Believe 100% of the time', 'Believe 50% of the time', 'Believe 50% of the time',
            'Do not believe at all',
            'Believe 25% of the time', 'Believe 50% of the time', 'Believe 75% of the time', 'Believe 100% of the time'
        ]
        self.stress_tests(*test_case_3_answers)

    def test_case_4(self):
        login_email = "umarhussain4046@gmail.com"
        login_password = "Dellm3800$"
        test_case_4_answers = [
            'Do not believe at all', 'Do not believe at all', 'Do not believe at all', 'Do not believe at all',
            'Do not believe at all', 'Do not believe at all', 'Do not believe at all', 'Do not believe at all',
            'Do not believe at all', 'Do not believe at all', 'Do not believe at all', 'Do not believe at all',
            'Do not believe at all', 'Do not believe at all', 'Do not believe at all', 'Do not believe at all',
            'Do not believe at all', 'Do not believe at all', 'Do not believe at all', 'Do not believe at all',
            'Do not believe at all', 'Do not believe at all', 'Do not believe at all', 'Do not believe at all',
            'Do not believe at all'
        ]
        self.stress_tests(*test_case_4_answers)

    def test_case_5(self):
        login_email = "umarhussain4046@gmail.com"
        login_password = "Dellm3800$"
        test_case_5_answers = [
            'Do not believe at all', 'Believe 25% of the time', 'Do not believe at all', 'Do not believe at all',
            'Believe 75% of the time', 'Do not believe at all', 'Believe 25% of the time', 'Believe 50% of the time',
            'Do not believe at all', 'Believe 75% of the time', 'Believe 100% of the time', 'Do not believe at all',
            'Do not believe at all', 'Believe 25% of the time', 'Do not believe at all', 'Believe 50% of the time',
            'Do not believe at all', 'Believe 100% of the time', 'Believe 50% of the time', 'Believe 50% of the time',
            'Do not believe at all',
            'Believe 25% of the time', 'Believe 50% of the time', 'Believe 75% of the time', 'Believe 100% of the time'
        ]
        self.stress_tests(*test_case_5_answers)


if __name__ == '__main__':
    unittest.main()
