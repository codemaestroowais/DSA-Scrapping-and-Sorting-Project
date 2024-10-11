from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import csv

def extract_solds(text):
    solds = 0
    solds_match = re.search(r'(\d+)\s*solds', text, re.IGNORECASE)
    if solds_match:
        solds = solds_match.group(1)  # Get the number before "solds"
    return solds

def extract_watchers(text):
    watchers = 0
    watchers_match = re.search(r'(\d+)\s*watchers', text, re.IGNORECASE)
    if watchers_match:
        watchers = watchers_match.group(1)  # Get the number before "watchers"
    return watchers

def extract_seller_name(text):
    pattern = r'([^()]+)\s+\(\d+\)\s+\d+\.\d+%'
    match = re.search(pattern, text)
    if match:
        return match.group(1).strip()  # Return the seller name
    return "N/A"

def extract_items_sold(text):
    pattern = r'\((\d+)\)\s+\d+\.\d+%'
    match = re.search(pattern, text)
    if match:
        return match.group(1)  # Return the items sold
    return "N/A"

def extract_reliability(text):
    pattern = r'(\d+\.\d+%)$'
    match = re.search(pattern, text)
    if match:
        return match.group(1)  # Return the reliability percentage
    return "N/A"
def Scrapping(self):
    # Fix the path to Chrome WebDriver
    service = Service(executable_path=r'C:\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    # Output CSV file path
    output_csv = 'Output.csv'
    BrandName = "Fender"

    # Lists to store data across all pages
    Names = []  
    Secondary_Info = []   
    Price = []
    Solds = []
    Watchers = []
    Discount = []
    Seller_Names = []
    Items_Sold = []
    Reliabilities = []

    # Create the CSV file if it doesn't exist
    if not os.path.exists(output_csv):
        with open(output_csv, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Names', 'Secondary_Info', 'Prices', 'Solds', 'Watches', 'Discount', 'Seller_Names', 'Items_Sold', 'Reliabilities'])

    # Loop over pages
    for i in range(1, 43):  # Adjust these values based on the actual page range
            
        print(f"Processing page {i}")
        page = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw=guitars&_sacat=0&_oaa=1&rt=nc&Brand={BrandName}&_dcat=33034&_ipg=240&_pgn={i}'
        driver.get(page)

        try:
            # Wait for the page to load the product titles
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 's-item__title')))
        except Exception as e:
            print(f"Error loading page {i}: {e}")
            continue  # Skip this page if it doesn't load properly

        # Scroll to the bottom to ensure all items are loaded
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)  # Wait to ensure the page is fully loaded

        # Extract page source and parse it using BeautifulSoup
        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')

        # Find all product elements
        elements = soup.findAll('div', attrs={'class': 's-item__info clearfix'})

        # Track products processed in this page
        products_processed = 0
        products_skipped = 0

        # Loop through each product entry and extract details
        for a in elements:
            # Extract product name and other info
            
            names = a.find('div', attrs={'class': 's-item__title'})
            secondary_info = a.find('span', attrs={'class': 'SECONDARY_INFO'})
            price = a.find('span', attrs={'class': 's-item__price'})
            List = a.findAll('span', attrs={'class': 'BOLD'}) 

            # Extract additional information if available
            discounts = a.find('span', attrs={'class': 's-item__discount'})
            seller_info = a.find('span', attrs={'class': 's-item__seller-info'})

            # Check if the product name and price exist
            if names and price:
                solds = extract_solds(" ".join([b.get_text() for b in List]))
                watchers = extract_watchers(" ".join([b.get_text() for b in List]))

                seller_name = "N/A"
                items_sold = "N/A"
                reliability = "N/A"

                # Check if seller_info is not None before processing
                if seller_info:
                    text_c = seller_info.get_text()  # Get the text from the seller_info
                    seller_name = extract_seller_name(text_c)
                    items_sold = extract_items_sold(text_c)
                    reliability = extract_reliability(text_c)

                # Append data to lists
                
                Names.append(names.text.strip())
                Secondary_Info.append(secondary_info.text.strip() if secondary_info else 'N/A')
                Price.append(price.text.strip())
                Solds.append(solds)
                Watchers.append(watchers)
                Discount.append(discounts.text.strip() if discounts else 'N/A')
                Seller_Names.append(seller_name)
                Items_Sold.append(items_sold)
                Reliabilities.append(reliability)
                products_processed += 1
                # Append to the CSV file
                with open(output_csv, 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([names.text.strip(), secondary_info.text.strip() if secondary_info else 'N/A', price.text.strip(), solds, watchers, discounts.text.strip() if discounts else 'N/A', seller_name, items_sold, reliability])
            else:
                products_skipped +=  1

        print(f"Page {i}: Processed {products_processed}, Skipped {products_skipped}")
    # Close the driver
    driver.quit()

    print(f"Scraping complete. Data saved to {output_csv}")