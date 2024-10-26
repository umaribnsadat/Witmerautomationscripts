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

        take_assessment_button = (By.XPATH, "(//button[@class='btn'])[1]")
        wait = WebDriverWait(self.driver, 20)
        take_assessment_button = wait.until(EC.element_to_be_clickable(take_assessment_button))
        take_assessment_button.click()

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

        submit_button_locator = (By.XPATH, '//button[@type="submit"]')
        submit_button = wait.until(EC.element_to_be_clickable(submit_button_locator))
        submit_button.click()
        time.sleep(2)

        yes_button_locator = (By.XPATH, "//button[normalize-space()='Yes']")
        yes_button = wait.until(EC.element_to_be_clickable(yes_button_locator))
        yes_button.click()
        time.sleep(4)

        ok_button_locator = (By.XPATH, "//button[normalize-space()='OK']")
        ok_button = wait.until(EC.element_to_be_clickable(ok_button_locator))
        ok_button.click()
        time.sleep(2)

        down_locator = (By.XPATH, "//button[normalize-space()='Download Report']")
        down_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(down_locator))
        down_button.click()

        time.sleep(9)
        print("Download Report button clicked successfully")

    def test_case_1(self):
        login_email = "umarhussain4046@gmail.com"
        login_password = "Dellm3800$"
        test_case_1_answers = ['Moderately Accurate',
                               'Moderately Accurate',
                               'Very Accurate',
                               'Moderately Accurate',
                               'Very Accurate',
                               'Moderately Accurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Accurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Very Inaccurate',
                               'Moderately Accurate',
                               'Moderately Inaccurate',
                               'Very Accurate',
                               'Very Accurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Very Accurate',
                               'Very Inaccurate',
                               'Moderately Accurate',
                               'Very Accurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Accurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Very Accurate',
                               'Very Accurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Neither Accurate nor Inaccurate',
                               'Very Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Very Inaccurate',
                               'Moderately Accurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Very Accurate',
                               'Moderately Accurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Accurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Very Accurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Neither Accurate nor Inaccurate',
                               'Very Accurate',
                               'Very Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Very Inaccurate',
                               'Very Inaccurate',
                               'Very Accurate',
                               'Very Accurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Accurate',
                               'Very Inaccurate',
                               'Very Inaccurate',
                               'Moderately Inaccurate',
                               'Very Inaccurate',
                               'Very Accurate',
                               'Very Inaccurate',
                               'Very Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Moderately Inaccurate',
                               'Very Inaccurate',
                               'Very Inaccurate',
                               'Moderately Inaccurate',
                               'Very Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Inaccurate',
                               'Very Accurate',
                               'Moderately Accurate',
                               'Very Accurate',
                               'Moderately Inaccurate',
                               'Very Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Moderately Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Very Inaccurate',
                               'Very Inaccurate',
                               'Moderately Inaccurate',
                               'Very Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Very Accurate',
                               'Very Inaccurate',
                               'Very Inaccurate']  # Repeat 'Not at all' seven times
        self.run_test_case(login_email, login_password, *test_case_1_answers)

    def test_case_2(self):
        login_email = "umarhussain4046@gmail.com"
        login_password = "Dellm3800$"
        test_case_2_answers = ['Very Accurate',
                               'Moderately Accurate',
                               'Very Accurate',
                               'Very Accurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Very Inaccurate',
                               'Moderately Accurate',
                               'Very Inaccurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Very Accurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Very Accurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Very Accurate',
                               'Very Inaccurate',
                               'Very Accurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Very Accurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Very Accurate',
                               'Very Accurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Very Inaccurate',
                               'Moderately Accurate',
                               'Very Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Very Accurate',
                               'Moderately Inaccurate',
                               'Very Inaccurate',
                               'Very Accurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Very Accurate',
                               'Very Accurate',
                               'Moderately Accurate',
                               'Moderately Inaccurate',
                               'Very Accurate',
                               'Moderately Accurate',
                               'Very Inaccurate',
                               'Moderately Accurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Accurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Very Accurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Very Inaccurate',
                               'Very Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Moderately Inaccurate',
                               'Very Accurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Very Accurate',
                               'Neither Accurate nor Inaccurate',
                               'Very Inaccurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Very Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Very Inaccurate',
                               'Very Accurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Very Accurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate']  # Repeat 'Not at all' seven times kartik data
        self.run_test_case(login_email, login_password, *test_case_2_answers)

    def test_case_3(self):
        login_email = "umarhussain4046@gmail.com"
        login_password = "Dellm3800$"
        test_case_3_answers = ['Moderately Accurate',
                               'Neither Accurate nor Inaccurate',
                               'Very Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Neither Accurate nor Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Inaccurate',
                               'Very Accurate',
                               'Very Inaccurate',
                               'Moderately Accurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Inaccurate',
                               'Very Inaccurate',
                               'Very Inaccurate',
                               'Moderately Accurate',
                               'Neither Accurate nor Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Very Inaccurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Accurate',
                               'Moderately Inaccurate',
                               'Very Inaccurate',
                               'Very Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Accurate',
                               'Very Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Accurate',
                               'Neither Accurate nor Inaccurate',
                               'Very Inaccurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Very Inaccurate',
                               'Very Inaccurate',
                               'Very Inaccurate',
                               'Moderately Accurate',
                               'Very Inaccurate',
                               'Very Inaccurate',
                               'Very Inaccurate',
                               'Moderately Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Very Inaccurate',
                               'Moderately Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Very Inaccurate',
                               'Moderately Accurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Very Inaccurate',
                               'Moderately Accurate',
                               'Neither Accurate nor Inaccurate',
                               'Very Inaccurate',
                               'Very Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Very Inaccurate',
                               'Very Inaccurate',
                               'Very Inaccurate',
                               'Very Inaccurate',
                               'Very Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Very Inaccurate',
                               'Very Inaccurate',
                               'Very Inaccurate',
                               'Very Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Neither Accurate nor Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Moderately Inaccurate',
                               'Very Inaccurate',
                               'Moderately Inaccurate',
                               'Very Inaccurate',
                               'Very Inaccurate',
                               'Moderately Accurate',
                               'Moderately Accurate',
                               'Very Inaccurate',
                               'Very Inaccurate',
                               'Very Inaccurate']  # Repeat 'Not at all' seven times kartik data
        self.run_test_case(login_email, login_password, *test_case_3_answers)


if __name__ == '__main__':
    unittest.main()
