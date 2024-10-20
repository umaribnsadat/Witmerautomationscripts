from selenium.webdriver.common.by import By
from NewMindnProject.utils.config_loader import ConfigLoader

from NewMindnProject.pages.base_page import BasePage

config = ConfigLoader()


class HomePage(BasePage):
    wellness_link_xpath = (By.XPATH, config.get_property('wellness_link_xpath'))
    stress_link_xpath = (By.XPATH, config.get_property('stress_link_xpath'))
    anxiety_link_xpath = (By.XPATH, config.get_property('anxiety_link_xpath'))
    burnout_link_xpath = (By.XPATH, config.get_property('burnout_link_xpath'))
    start_assessment_button_xpath = (By.XPATH, config.get_property('start_assessment_button_xpath'))
    start_button_xpath = (By.XPATH, config.get_property('start_button_xpath'))
    productivity_button_xpath = (By.XPATH, config.get_property('productivity_button_xpath'))
    masterclass_button_xpath = (By.XPATH, config.get_property('masterclass_button_xpath'))
    continue_button_xpath = (By.XPATH, config.get_property('continue_button_xpath'))
    ok_button_xpath = (By.XPATH, config.get_property('ok_button_xpath'))
    submit_button_xpath = (By.XPATH, config.get_property('submit_button_xpath'))
    yes_button_xpath = (By.XPATH, config.get_property('yes_button_xpath'))
    download_report_button_xpath = (By.XPATH, config.get_property('download_report_button_xpath'))

    def click_wellness(self):
        self.click_element(self.wellness_link_xpath)

    def click_stress(self):
        self.click_element(self.stress_link_xpath)

    def click_anxiety(self):
        self.click_element(self.anxiety_link_xpath)

    def click_burnout(self):
        self.click_element(self.burnout_link_xpath)

    def click_start_assessment(self):
        self.click_element(self.start_assessment_button_xpath)

    def click_start(self):
        self.click_element(self.start_button_xpath)

    def click_continue(self):
        self.click_element(self.continue_button_xpath)

    def click_submit(self):
        self.click_element(self.submit_button_xpath)

    def click_yes(self):
        self.click_element(self.yes_button_xpath)

    def click_download_report(self):
        self.click_element(self.download_report_button_xpath)

    def click_ok(self):
        self.click_element(self.ok_button_xpath)

    @staticmethod
    def get_question_locator(answer):
        return (By.XPATH, config.get_property('question_label_xpath_template').format(answer=answer))
