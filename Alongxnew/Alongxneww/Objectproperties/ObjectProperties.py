from selenium.webdriver.common.by import By

class ObjectRepository:
    # Login Page Elements
    # login_url = "https://default.mindn.ai/"
    login_url = "https://memops-web-prod-ci-as.azurewebsites.net/"

    # Updated Locators using XPath
    login_email_name = (By.XPATH, "//input[@id='email']")
    login_password_name = (By.XPATH, "//input[@id='password']")
    login_button_css = (By.XPATH, "//button[@id='btnLogin']")

    # Login Credentials
    # login_email = 'umarhussain4046@gmail.com'
    # login_password = 'Dellm3800$'
    login_email = "memopsteam@gmail.com"
    login_password = "Alongx@123"


    # Home Page Elements
    wellness_link_xpath = "//div[normalize-space()='Wellness']"
    anger_link_xpath = "//span[normalize-space()='Anger']"
    stress_link_xpath = "//span[normalize-space()='Stress']"
    Anxiety_locator = (By.XPATH, "//a[normalize-space()='Anxiety']")
    Burnout_locator = (By.XPATH, "//span[normalize-space()='Burnout']")
    Intolerance_Of_Uncertainty = "//span[normalize-space() = 'Intolerance Of Uncertainty']"
    worklife_link_xpath = (By.XPATH, "//span[contains(text(),'Work-life balance​')]")
    perfectionism_link_xpath = (By.XPATH, "//span[normalize-space()='Perfectionism']")
    sleep_link_locator = (By.XPATH, "//span[normalize-space()='Sleep']")
    sleepq_locator_xpath = (By.XPATH, "//a[normalize-space()='General Stress (Beta)']")

    # New Assessment Links
    work_stress_assessment_xpath = (By.XPATH, "//span[normalize-space()='Work Stress Assessment']")
    general_stress_assessment_xpath = (By.XPATH, "//span[normalize-space()='General Stress Assessment']")
    work_life_balance_assessment_xpath = (By.XPATH, "//span[normalize-space()='Work-Life Balance Assessment']")
    anger_assessment_xpath = (By.XPATH, "//span[normalize-space()='Anger Assessment']")
    sleep_quality_assessment_xpath = (By.XPATH, "//span[normalize-space()='Sleep Quality Assessment']")
    perfectionism_assessment_xpath = (By.XPATH, "//span[normalize-space()='Perfectionism Assessment']")
    intolerance_uncertainty_assessment_xpath = (
        By.XPATH, "//span[normalize-space()='Intolerance of Uncertainty Assessment']")

    start_assessment_button_xpath = "//button[normalize-space()='Start Assessment']"
    start_button_xpath = "//button[normalize-space()='Start']"
    productivity_button = "//div[normalize-space()='Productivity']"
    Masterclass_button = "//span[normalize-space()='Masterclasses']"
    Continue_locator = "//button[@class='ass-start-btn note-button text-uppercase']"
    ok_locator = (By.XPATH, "//button[normalize-space()='OK']")
    submit_button_xpath = "//button[normalize-space()='Submit']"
    download_report_button_xpath = "//button[normalize-space()='Download Report']"
    yes_button_xpath = "//button[normalize-space()='Yes']"

    dropdown_button_locator = (By.XPATH, "//button[contains(@class,'dropdown-toggle dropdown-toggle-split')]")

    # SleepQ Link Locator

    answer_locators = {
        'Always': (By.XPATH, "//label[normalize-space()='Always']"),
        'Never': (By.XPATH, "//label[normalize-space()='Never']"),
        'Strongly Agree': (By.XPATH, "//label[normalize-space()='Strongly Agree']"),
        'Agree': (By.XPATH, "//label[text()='Agree ']"),
        'Strongly Disagree': (By.XPATH, "//label[normalize-space()='Strongly Disagree']"),
        'Often': (By.XPATH, "//label[text()='Often']"),
        'Rarely': (By.XPATH, "//label[normalize-space()='Rarely']"),
        'Disagree': (By.XPATH, "//label[text()='Disagree']"),
        'Neither Agree nor Disagree': (By.XPATH, "//input[@value='Neither Agree nor Disagree']"),
        'Completely characteristic of me': (By.XPATH, "//label[contains(text(),'Completely characteristic ')]"),
        'Mostly characteristic of me': (By.XPATH, "//label[contains(text(),'Mostly characteristic ')]"),
        'Seldom characteristic of me': (By.XPATH, "//label[contains(text(),'Seldom characteristic ')]"),
        'Not at all characteristic of me': (By.XPATH, "//label[contains(text(),'Not at all characteristic ')]")
    }

    @staticmethod
    def get_question_xpath(answer):
        return f"//label[normalize-space()='{answer}']"
