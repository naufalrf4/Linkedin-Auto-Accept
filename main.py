import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

linkedin_username = os.getenv('LINKEDIN_EMAIL')
linkedin_password = os.getenv('LINKEDIN_PASSWORD')
chrome_driver_path = os.getenv('CHROMEDRIVER_PATH')
# edge_driver_path = os.getenv('EDGEDRIVER_PATH')

# Using ChromeDriver
service = ChromeService(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
try:
    driver = webdriver.Chrome(service=service, options=options)
    print("ChromeDriver started successfully.")
except WebDriverException as e:
    print(f"Error starting ChromeDriver: {e}")
    raise

# Using EdgeDriver
# service = EdgeService(edge_driver_path)
# options = webdriver.EdgeOptions()
# options.add_argument("--start-maximized")
# try:
#     driver = webdriver.Edge(service=service, options=options)
#     print("EdgeDriver started successfully.")
# except WebDriverException as e:
#     print(f"Error starting EdgeDriver: {e}")
#     raise

def login_to_linkedin():
    try:
        driver.get("https://www.linkedin.com/login")
        print("Navigated to LinkedIn login page.")

        # Enter username and password
        username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        print(f"Username field found: {username}")

        password = driver.find_element(By.ID, "password")
        print(f"Password field found: {password}")

        username.send_keys(linkedin_username)
        password.send_keys(linkedin_password)
        print("Entered login credentials.")

        # Ensure the login button is clickable
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Sign in']"))
        )
        print(f"Login button found: {login_button}")

        # Click the login button
        login_button.click()
        print("Clicked the login button.")
        time.sleep(5)

    except NoSuchElementException as e:
        print(f"Login error: {e}")
        driver.quit()
        raise
    except Exception as e:
        print(f"An unexpected error occurred during login: {e}")
        driver.quit()
        raise

def accept_invitations():
    try:
        driver.get("https://www.linkedin.com/mynetwork/invitation-manager/")
        print("Navigated to the invitations page.")
        time.sleep(5)

        # Accept all invitations
        while True:
            accept_buttons = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@aria-label, 'Accept')]"))
            )
            print(f"Found {len(accept_buttons)} accept buttons.")

            if not accept_buttons:
                print("No more invitations to accept.")
                break

            for button in accept_buttons:
                ActionChains(driver).move_to_element(button).click(button).perform()
                print("Accepted an invitation.")
                time.sleep(1)  # Set delay to avoid being blocked by LinkedIn

    except NoSuchElementException as e:
        print(f"Error accepting invitations: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        driver.quit()
        print("Driver closed.")

def main():
    try:
        login_to_linkedin()
        accept_invitations()
    except Exception as e:
        print(f"An error occurred during the process: {e}")

if __name__ == "__main__":
    main()
