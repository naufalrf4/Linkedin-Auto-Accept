import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get LinkedIn credentials from environment variables
linkedin_username = os.getenv('LINKEDIN_EMAIL')
linkedin_password = os.getenv('LINKEDIN_PASSWORD')

# Get paths to the web drivers from environment variables
chrome_driver_path = os.getenv('CHROMEDRIVER_PATH')
edge_driver_path = os.getenv('EDGEDRIVER_PATH')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Choose which browser to use by commenting/uncommenting the relevant parts below

# Using ChromeDriver
service = ChromeService(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
try:
    driver = webdriver.Chrome(service=service, options=options)
    logging.info("ChromeDriver started successfully.")
except WebDriverException as e:
    logging.error(f"Error starting ChromeDriver: {e}")
    raise

# Using EdgeDriver
# service = EdgeService(edge_driver_path)
# options = webdriver.EdgeOptions()
# options.add_argument("--start-maximized")
# try:
#     driver = webdriver.Edge(service=service, options=options)
#     logging.info("EdgeDriver started successfully.")
# except WebDriverException as e:
#     logging.error(f"Error starting EdgeDriver: {e}")
#     raise

def login_to_linkedin():
    try:
        driver.get("https://www.linkedin.com/login")
        logging.info("Navigated to LinkedIn login page.")

        # Enter username and password
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        username.send_keys(linkedin_username)
        password.send_keys(linkedin_password)
        logging.info("Entered login credentials.")

        # Submit the login form
        password.send_keys(Keys.RETURN)
        logging.info("Submitted the login form.")
        time.sleep(5)

    except NoSuchElementException as e:
        logging.error(f"Login error: {e}")
        driver.quit()
        raise

def accept_invitations():
    try:
        driver.get("https://www.linkedin.com/mynetwork/invitation-manager/")
        logging.info("Navigated to the invitations page.")
        time.sleep(5)

        # Accept all invitations
        while True:
            accept_buttons = driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'Accept')]")
            if not accept_buttons:
                logging.info("No more invitations to accept.")
                break
            for button in accept_buttons:
                ActionChains(driver).move_to_element(button).click(button).perform()
                logging.info("Accepted an invitation.")
                time.sleep(1)  # Set delay to avoid being blocked by LinkedIn

    except NoSuchElementException as e:
        logging.error(f"Error accepting invitations: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    finally:
        driver.quit()
        logging.info("Driver closed.")

def main():
    try:
        login_to_linkedin()
        accept_invitations()
    except Exception as e:
        logging.error(f"An error occurred during the process: {e}")

if __name__ == "__main__":
    main()
