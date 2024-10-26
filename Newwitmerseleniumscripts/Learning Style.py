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

        stress_link_locator = (By.XPATH, "body > div:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > span:nth-child(1)")
        stress_link = wait.until(EC.element_to_be_clickable(stress_link_locator))
        stress_link.click()
