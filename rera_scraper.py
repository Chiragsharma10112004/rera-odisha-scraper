import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    chrome_options = Options()
    if os.environ.get("RUNNING_IN_CLOUD"):
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.binary_location = "/usr/bin/chromium-browser"
    else:
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def scrape_projects():
    base_url = "https://rera.odisha.gov.in"
    project_list_url = f"{base_url}/projects/project-list"
    driver = setup_driver()
    driver.get(project_list_url)
    wait = WebDriverWait(driver, 60)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table#example")))
    projects = []
    rows = driver.find_elements(By.CSS_SELECTOR, "table#example tbody tr")[:6]
    for idx, row in enumerate(rows, start=1):
        view_link = row.find_element(By.LINK_TEXT, "View Details")
        driver.execute_script("arguments[0].scrollIntoView();", view_link)
        view_link.click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.card-header h5")))
        rera_regd_no = driver.find_element(By.XPATH, "//th[text()='Rera Regd No.']/following-sibling::td").text.strip()
        project_name = driver.find_element(By.CSS_SELECTOR, "div.card-header h5").text.strip()
        promoter_tab = driver.find_element(By.XPATH, "//a[contains(text(),'Promoter Details')]")
        promoter_tab.click()
        time.sleep(1)
        company_name = driver.find_element(By.XPATH, "//th[text()='Company Name']/following-sibling::td").text.strip()
        registered_office_address = driver.find_element(By.XPATH, "//th[contains(text(),'Registered Office Address')]/following-sibling::td").text.strip()
        gst_no = driver.find_element(By.XPATH, "//th[text()='GST No.']/following-sibling::td").text.strip()
        projects.append({
            "Rera Regd. No": rera_regd_no,
            "Project Name": project_name,
            "Promoter Name": company_name,
            "Address of the Promoter": registered_office_address,
            "GST No": gst_no
        })
        driver.back()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table#example")))
    driver.quit()
    return projects

if __name__ == "__main__":
    data = scrape_projects()
    for i, proj in enumerate(data, start=1):
        print(f"Project #{i}:")
        for key, value in proj.items():
            print(f"  {key}: {value}")
        print("\n")
