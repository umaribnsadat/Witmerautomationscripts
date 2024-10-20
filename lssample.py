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
        self.driver.get("https://default.mindn.ai/")
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.text-uppercase.login-new-btn")))
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        login_button.click()

    def stress_tests(self, *answers):
        answer_locators = {
            'try it out': (By.XPATH, "//label[contains(normalize-space(), 'try it out')]"),
            'realistic': (By.XPATH, "//label[contains(normalize-space(), 'realistic')]"),
            'pictures': (By.XPATH, "//label[contains(normalize-space(), 'pictures')]"),
            'understand details of a subject but may be fuzzy about its overall structure': (By.XPATH,
                                                                                             "//label[contains(text(),'understand details of a project but may be fuzzy about its overall structure')]"),
            'talk about it': (By.XPATH, "//label[contains(normalize-space(), 'talk about it')]"),
            'that deals with ideas and theories': (
                By.XPATH, "//label[contains(normalize-space(), 'that deals with ideas and theories')]"),
            'pictures, diagrams, graphs, or maps': (
                By.XPATH, "//label[contains(normalize-space(), 'pictures, diagrams, graphs, or maps')]"),
            'all the parts, I understand the whole thing': (
                By.XPATH, "//label[contains(normalize-space(), 'all the parts, I understand the whole thing')]"),
            'sit back and listen': (By.XPATH, "//label[contains(normalize-space(), 'sit back and listen')]"),
            'to learn concepts': (By.XPATH, "//label[contains(normalize-space(), 'to learn concepts')]"),
            'focus on the written text': (
                By.XPATH, "//label[contains(normalize-space(), 'focus on the written text')]"),
            'I usually work my way to the solutions one step at a time': (By.XPATH,
                                                                          "//label[contains(normalize-space(), 'I usually work my way to the solutions one step at a time')]"),
            'I have usually gotten to know many of the peers': (
                By.XPATH, "//label[contains(normalize-space(), 'I have usually gotten to know many of the peers')]"),
            'something that teaches me new facts or tells me how to do something': (By.XPATH,
                                                                                    "//label[contains(normalize-space(), 'something that teaches me new facts or tells me how to do something')]"),
            'who spend a lot of time explaining': (
                By.XPATH, "//label[contains(normalize-space(), 'who spend a lot of time explaining')]"),
            'I think of the incidents and try to put them together to figure out the themes': (By.XPATH,
                                                                                               "//label[contains(normalize-space(), 'I think of the incidents and try to put them together to figure out the themes')]"),
            'try to fully understand the problem first': (
                By.XPATH, "//label[contains(normalize-space(), 'try to fully understand the problem first')]"),
            'theory': (By.XPATH, "//label[contains(normalize-space(), 'theory')]"),
            'what I hear': (By.XPATH, "//label[contains(normalize-space(), 'what I hear')]"),
            'lay out the material in clear sequential steps': (
                By.XPATH, "//label[contains(normalize-space(), 'lay out the material in clear sequential steps')]"),
            'in a study group': (By.XPATH, "//label[contains(normalize-space(), 'in a study group')]"),
            'careful about the details of my work': (
                By.XPATH, "//label[contains(normalize-space(), 'careful about the details of my work')]"),
            'written instructions': (By.XPATH, "//label[contains(normalize-space(), 'written instructions')]"),
            'at a fairly regular pace. If I study hard, I’ll “get it” ': (By.XPATH,
                                                                          "//label[contains(normalize-space(), 'at a fairly regular pace. If I study hard, I’ll “get it” ')]"),
            'try things out': (By.XPATH, "//label[contains(normalize-space(), 'try things out')]"),
            'say things in creative, interesting ways': (
                By.XPATH, "//label[contains(normalize-space(), 'say things in creative, interesting ways')]"),
            'what the instructor said about it': (
                By.XPATH, "//label[contains(normalize-space(), 'what the instructor said about it')]"),
            'focus on details and miss the big picture': (
                By.XPATH, "//label[contains(normalize-space(), 'focus on details and miss the big picture')]"),
            'something I have thought a lot about': (
                By.XPATH, "//label[contains(normalize-space(), 'something I have thought a lot about')]"),
            'come up with new ways of doing it': (
                By.XPATH, "//label[contains(normalize-space(), 'come up with new ways of doing it')]"),
            'text summarizing the results': (
                By.XPATH, "//label[contains(normalize-space(), 'text summarizing the results')]"),
            'work on (think about or write) the beginning of the paper and progress forward': (By.XPATH,
                                                                                               "//label[contains(normalize-space(), 'work on (think about or write) the beginning of the paper and progress forward')]"),
            'have “group brainstorming” where everyone contributes ideas': (By.XPATH,
                                                                            "//label[contains(normalize-space(), 'have “group brainstorming” where everyone contributes ideas')]"),
            'sensible': (By.XPATH, "//label[contains(normalize-space(), 'sensible')]"),
            'what they said about themselves': (
                By.XPATH, "//label[contains(normalize-space(), 'what they said about themselves')]"),
            'try to make connections between that subject and related subjects': (By.XPATH,
                                                                                  "//label[contains(normalize-space(), 'try to make connections between that subject and related subjects')]"),
            'reserved': (By.XPATH, "//label[contains(normalize-space(), 'reserved')]"),
            'abstract material (concepts, theories)': (
                By.XPATH, "//label[contains(normalize-space(), 'abstract material (concepts, theories)')]"),
            'read a book': (By.XPATH, "//label[contains(normalize-space(), 'read a book')]"),
            'very helpful to me': (By.XPATH, "//label[contains(normalize-space(), 'very helpful to me')]"),
            'appeals to me': (By.XPATH, "//label[contains(normalize-space(), 'appeals to me')]"),
            'I tend to repeat all my steps and check my work carefully': (By.XPATH,
                                                                          "//label[contains(normalize-space(), 'I tend to repeat all my steps and check my work carefully')]"),
            'with difficulty and without much detail': (
                By.XPATH, "//label[contains(normalize-space(), 'with difficulty and without much detail')]"),
            'think of possible consequences or applications of the solution in a wide range of areas': (By.XPATH,
                                                                                                        "//label[contains(normalize-space(), 'think of possible consequences or applications of the solution in a wide range of areas')]")
        }

        for answer in answers:
            locator = answer_locators.get(answer)
            if locator:
                wait = WebDriverWait(self.driver, 20)
                element = wait.until(EC.element_to_be_clickable(locator))
                element.click()
                time.sleep(4)
            else:
                print(f"Answer '{answer}' not found in answer_locators.")

        for answer in answers:
            locator = answer_locators.get(answer)
            if locator:
                wait = WebDriverWait(self.driver, 20)
                element = wait.until(EC.element_to_be_clickable(locator))
                element.click()
                time.sleep(4)
            else:
                print(f"Answer '{answer}' not found in answer_locators.")

    def run_test_case(self, email, password, *answers):
        self.login(email, password)

        wellness_locator = (By.XPATH, "//div[normalize-space()='Wellness']")
        wait = WebDriverWait(self.driver, 20)
        wellness_link = wait.until(EC.element_to_be_clickable(wellness_locator))
        wellness_link.click()

        time.sleep(3)

        stress_link_locator = (By.XPATH, "(//span[@class='nav-link text-small active'])[23]")
        stress_link = wait.until(EC.element_to_be_clickable(stress_link_locator))
        stress_link.click()

        time.sleep(3)

        start_locator = (By.XPATH, "//button[normalize-space()='Start']")
        start_link = wait.until(EC.element_to_be_clickable(start_locator))
        start_link.click()

        time.sleep(3)

        self.stress_tests(*answers)

        submit_button_locator = (By.XPATH, '//button[@type="submit"]')
        submit_button = wait.until(EC.element_to_be_clickable(submit_button_locator))
        submit_button.click()
        time.sleep(2)

        yes_button_locator = (By.XPATH, "//button[normalize-space()='Yes']")
        yes_button = wait.until(EC.element_to_be_clickable(yes_button_locator))
        yes_button.click()
        time.sleep(4)

    def test_case_1(self):
        login_email = "umarhussain4046@gmail.com"
        login_password = "Dellm3800$"
        test_case_1_answers = [
            'try it out',
            'realistic',
            'pictures',
            'understand details of a subject but may be fuzzy about its overall structure',
            'talk about it',
            'that deals with ideas and theories',
            'pictures, diagrams, graphs, or maps',
            'all the parts, I understand the whole thing',
            'sit back and listen',
            'to learn concepts',
            'focus on the written text',
            'I usually work my way to the solutions one step at a time',
            'I have usually gotten to know many of the peers',
            'something that teaches me new facts or tells me how to do something',
            'who spend a lot of time explaining',
            'I think of the incidents and try to put them together to figure out the themes',
            'try to fully understand the problem first',
            'theory',
            'what I hear',
            'lay out the material in clear sequential steps',
            'in a group',
            'careful about the details of my work',
            'written instructions',
            'at a fairly regular pace. If I study hard, I’ll “get it” ',
            'try things out',
            'say things in creative, interesting ways',
            'what the instructor said about it',
            'focus on details and miss the big picture',
            'something I have thought a lot about',
            'come up with new ways of doing it',
            'text summarizing the results',
            'work on (think about or write) the beginning of the paper and progress forward',
            'have “group brainstorming” where everyone contributes ideas',
            'sensible',
            'what they said about themselves',
            'try to make connections between that subject and related subjects',
            'reserved',
            'abstract material (concepts, theories)',
            'read a book',
            'very helpful to me',
            'appeals to me',
            'I tend to repeat all my steps and check my work carefully',
            'with difficulty and without much detail',
            'think of possible consequences or applications of the solution in a wide range of areas'
        ]
        self.run_test_case(login_email, login_password, *test_case_1_answers)

if __name__ == '__main__':
            unittest.main()