# RERA Odisha Projects Scraper

This Python project scrapes project data from the official [RERA Odisha Project List](https://rera.odisha.gov.in/projects/project-list) website. It extracts summary information for the first 6 projects listed under the "Projects Registered" section, then navigates to each project's details page to gather comprehensive information.

## Features

- Scrapes project summary data from the main project list page.
- Visits each project's **View Details** page to extract detailed info, including:
  - RERA Registration Number
  - Project Name
  - Promoter Name (Company Name under Promoter Details tab)
  - Address of the Promoter (Registered Office Address under Promoter Details tab)
  - GST Number
- Outputs the collected data in a well-structured JSON format for easy consumption.

## Technologies Used

- Python 3
- Selenium WebDriver (using Chrome in headless mode)
- BeautifulSoup4 for HTML parsing
- `webdriver_manager` for automatic ChromeDriver installation and management

## Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Chiragsharma10112004/rera-odisha-scraper.git
   cd rera-odisha-scraper/rera-odisha-scraper
2. **Create and activate a virtual environment (recommended)**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Run the scraper script**
   ```bash
   python rera_scraper.py

---












