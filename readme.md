# LinkedIn Auto-Accept

A script to automate the acceptance of all LinkedIn invitations using Selenium WebDriver. This script can be used with Google Chrome or Microsoft Edge.

## Requirements

- Python 3.12 or newer
- Google Chrome or Microsoft Edge
- ChromeDriver (for Chrome) or EdgeDriver (for Edge)
- Python packages: selenium, python-dotenv

## Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/naufalrf4/Linkedin-Auto-Accept.git
   cd Linkedin-Auto-Accept
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install selenium python-dotenv
   ```

4. **Download and extract WebDriver:**

   - **Google Chrome:**
     Download [ChromeDriver](https://sites.google.com/chromium.org/driver/downloads) that matches your Chrome version and extract it to the project directory.

   - **Microsoft Edge:**
     Download [EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) that matches your Edge version and extract it to the project directory.

5. **Create a `.env` file in the project directory:**

   ```dotenv
   LINKEDIN_USERNAME=your_email@example.com
   LINKEDIN_PASSWORD=your_password
   CHROMEDRIVER_PATH=/path/to/your/chromedriver
   EDGEDRIVER_PATH=/path/to/your/msedgedriver
   ```

   Replace `your_email@example.com`, `your_password`, `path/to/your/chromedriver`, and `path/to/your/msedgedriver` with the appropriate information.

## Usage

1. **Activate the virtual environment (venv):**

   ```bash
   source venv/bin/activate  # Windows User, use `venv\Scripts\activate`
   ```

2. **Run the script:**

   ```bash
   python main.py
   ```

## Browser Setup

In the script, you can choose to use Google Chrome or Microsoft Edge by uncommenting the relevant section. Example for using ChromeDriver:

```python
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
```

Example for using EdgeDriver:

```python
# Using EdgeDriver
service = EdgeService(edge_driver_path)
options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")
try:
    driver = webdriver.Edge(service=service, options=options)
    logging.info("EdgeDriver started successfully.")
except WebDriverException as e:
    logging.error(f"Error starting EdgeDriver: {e}")
    raise
```

## Credit

[Naufal Rizqullah F](https://github.com/naufalrf4)
