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

        stress_link_locator = (By.XPATH, "//ul[@id='menu-list']//span[contains(@class, 'nav-link') and contains("
                                         "@class, 'text-small') and contains(@class, 'active')]")
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

        Continue_locator = (By.XPATH, "//button[@class='ass-start-btn note-button text-uppercase']")
        Continue_loc = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(Continue_locator))
        Continue_loc.click()
        time.sleep(3)

        for i, answer in enumerate(answers, start=1):
            quest_locator = (By.XPATH, f"//label[normalize-space()='{answer}']")
            quest_link = wait.until(EC.element_to_be_clickable(quest_locator))
            quest_link.click()
            time.sleep(4)

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

        time.sleep(10)

    def test_case_1(self):
        login_email = "umarhussain4046@gmail.com"
        login_password = "Dellm3800$"
        test_case_1_answers = ['Never'] * 33  # Repeat 'Not at all' seven times
        self.run_test_case(login_email, login_password, *test_case_1_answers)

    def test_case_2(self):
        login_email = "umarhussain4046@gmail.com"
        login_password = "Dellm3800$"
        test_case_2_answers = ['Rarely', 'Sometimes', 'Rarely', 'Sometimes', 'Rarely', 'Sometimes', 'Rarely',
                               'Sometimes',
                               'Often', 'Often', 'Often', 'Often', 'Often',
                               'Sometimes', 'Sometimes', 'Sometimes', 'Sometimes', 'Sometimes',
                               'Rarely', 'Rarely', 'Rarely', 'Rarely', 'Rarely',
                               'Rarely', 'Rarely', 'Rarely', 'Rarely', 'Rarely',
                               'Sometimes', 'Sometimes', 'Sometimes', 'Sometimes', 'Sometimes'

                               ]
        self.run_test_case(login_email, login_password, *test_case_2_answers)

    def test_case_3(self):
        login_email = "umarhussain4046@gmail.com"
        login_password = "Dellm3800$"
        test_case_3_answers = ['Always', 'Always', 'Always', 'Always', 'Always', 'Always', 'Always', 'Always',
                               'Always', 'Always', 'Always', 'Always', 'Always',
                               'Always', 'Always', 'Always', 'Always', 'Always',
                               'Always', 'Always', 'Always', 'Always', 'Always',
                               'Always', 'Always', 'Always', 'Always', 'Always',
                               'Always', 'Always', 'Always', 'Always', 'Always'
                               ]
        self.run_test_case(login_email, login_password, *test_case_3_answers)


if __name__ == '__main__':
    unittest.main()
