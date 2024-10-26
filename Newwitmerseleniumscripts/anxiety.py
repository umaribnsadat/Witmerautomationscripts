import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from new import chrome_options

chrome_options.add_argument('--no-sandbox')



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

        # Navigate to the assessment page
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

        sleepqq_locator = (By.XPATH, "//a[normalize-space()='Anxiety']")
        sleepqq_locator = wait.until(EC.element_to_be_clickable(sleepqq_locator))
        sleepqq_locator.click()

        time.sleep(6)



        resilience_locator = (By.XPATH, "//button[normalize-space()='Start Assessment']")
        resilience_link = wait.until(EC.element_to_be_clickable(resilience_locator))
        resilience_link.click()

        time.sleep(3)

        start_locator = (By.XPATH, "//button[normalize-space()='Start']")
        start_link = wait.until(EC.element_to_be_clickable(start_locator))
        start_link.click()

        time.sleep(3)

        # Answer the questions
        for i, answer in enumerate(answers, start=1):
            quest_locator = (By.XPATH, f"//label[normalize-space()='{answer}']")
            quest_link = wait.until(EC.element_to_be_clickable(quest_locator))
            quest_link.click()
            time.sleep(4)

        # Submit the assessment
        submit_button_locator = (By.XPATH, '//button[@type="submit"]')
        submit_button = wait.until(EC.element_to_be_clickable(submit_button_locator))
        submit_button.click()
        time.sleep(2)

        # Click 'Yes' to confirm submission
        yes_button_locator = (By.XPATH, "//button[normalize-space()='Yes']")
        yes_button = wait.until(EC.element_to_be_clickable(yes_button_locator))
        yes_button.click()
        time.sleep(4)

        down_locator = (By.XPATH, "//button[normalize-space()='Download Report']")
        down_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(down_locator))
        down_button.click()
        print("Download Report button clicked successfully")

        time.sleep(10)

        # Check if the last answer is "Nearly every day" and click it if necessary
        if 'Nearly every day' in answers:
            nearly_every_day_locator = (By.XPATH, "//input[@value='Nearly everyday']")
            nearly_every_day_button = wait.until(EC.element_to_be_clickable(nearly_every_day_locator))
            nearly_every_day_button.click()

    def stress_tests(self, *answers):
        answer_locators = {
            'Not at all': (By.XPATH, "//label[normalize-space()='Not at all']"),
            'More than half the days': (By.XPATH, "//label[normalize-space()='More than half the days']"),
            'Nearly everyday': (By.XPATH, "//label[normalize-space()='Nearly everyday']")
        }
        for answer in answers:
            locator = answer_locators.get(answer)
            if locator:
                answer_xpath = locator[1]
                answer_element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((locator[0], answer_xpath)))
                answer_element.click()
                time.sleep(2)

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
        self.run_test_case(login_email, login_password, *test_case_3_answers)  # Run the test case

if __name__ == '__main__':
    unittest.main()
