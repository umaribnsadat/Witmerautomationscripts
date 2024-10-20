import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(r"--executable-path=C:\selenium driver\chromedriver.exe")

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

logout_clicked = False  # Variable to track whether logout has been clicked or not

try:
    # Navigate to the website
    driver.get("https://default.mindn.ai/")

    # Wait for the login button to be present
    login_button_locator = (By.CSS_SELECTOR, ".btn.text-uppercase.login-new-btn")
    wait = WebDriverWait(driver, 20)
    login_button = wait.until(EC.element_to_be_clickable(login_button_locator))

    # Input the email into the "email" input field
    email_address = "umarhussain4046@gmail.com"  # Replace with your actual email address
    driver.find_element(By.NAME, "email").send_keys(email_address)

    # Input the password into the "password" input field
    password_value = "Dellm3800$"  # Replace with your actual password
    driver.find_element(By.NAME, "password").send_keys(password_value)

    # Click the login button
    login_button.click()

    # Wait for the page to load after login
    masterclasses_locator = (By.XPATH, "//span[normalize-space()='Masterclasses']")
    masterclasses_link = wait.until(EC.element_to_be_clickable(masterclasses_locator))
    masterclasses_link.click()

    # Wait for some time (you can adjust the duration as needed)
    time.sleep(8)

    # Use JavaScript Executor to click the dropdown
    dropdown_locator = (By.XPATH, "//a[@id='profileDropdown']")
    dropdown_element = driver.find_element(*dropdown_locator)
    driver.execute_script("arguments[0].click();", dropdown_element)

    # Wait for 10 seconds before clicking the logout button
    time.sleep(10)

    # Click on the logout button with increased wait time
    logout_button_locator = (By.XPATH, "//li[@class='nav-item dropdown show']//div[4]")
    logout_button = wait.until(EC.element_to_be_clickable(logout_button_locator))
    logout_button.click()

    logout_clicked = True  # Update the variable to indicate logout has been clicked

except StaleElementReferenceException:
    print("Stale element reference. Trying to locate the logout button again.")

    # Click on the logout button with another attempt
    logout_button = wait.until(EC.element_to_be_clickable(logout_button_locator))
    logout_button.click()

    logout_clicked = True  # Update the variable to indicate logout has been clicked

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Print the status of logout click
    print(f"Logout clicked: {logout_clicked}")

    # Do not quit here if you want to keep the browser open
    pass