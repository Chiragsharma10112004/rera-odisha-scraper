# RERA Odisha Projects Scraper

This Python project scrapes the first 6 projects listed under the **"Projects Registered"** section on the [RERA Odisha Project List](https://rera.odisha.gov.in/projects/project-list) website.

## Features

- Scrapes project summary data from the main project list page.
- Navigates to each project's **View Details** page to extract detailed information:
  - **Rera Registration Number**
  - **Project Name**
  - **Promoter Name** (Company Name under Promoter Details tab)
  - **Address of the Promoter** (Registered Office Address under Promoter Details tab)
  - **GST Number**
- Outputs the extracted data in a structured JSON format.

## Technologies Used

- Python 3
- Selenium WebDriver with Chrome (headless mode)
- BeautifulSoup4 for HTML parsing
- webdriver_manager for automatic ChromeDriver management

## Setup Instructions

1. Clone the repository or download the code.

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the scraper script:
   python scraper.py



