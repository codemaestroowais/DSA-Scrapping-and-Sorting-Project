from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

def extract_seller_name(text):
    pattern = r'([^()]+)\s+\(\d+\)\s+\d+\.\d+%'
    match = re.search(pattern, text)
    if match:
        return match.group(1).strip()
    return "N/A"

def extract_items_sold(text):
    pattern = r'\((\d+)\)\s+\d+\.\d+%'
    match = re.search(pattern, text)
    if match:
        return match.group(1)  
    return "0"

def extract_reliability(text):
    pattern = r'(\d+\.\d+%)$'
    match = re.search(pattern, text)
    if match:
        return match.group(1)  
    return "0"
service = Service(executable_path=r'C:\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)
output_csv = 'new4.csv'

Names = []  
Conditions = []   
Prices = []
Shippings = []
Countrys = []
Solds = []
SellerInfos = []

# Loop over pages
for i in range(1, 43):  # Adjust these values based on the actual page range
    print(f"Processing page {i}")
    page = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw=music&_sacat=267&_ipg=240&rt=nc&Format=Trade%2520Paperback&_dcat=267&_pgn={i}'
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
        Name = a.find('div', attrs={'class': 's-item__title'})
        Condition= a.find('span', attrs={'class': 'SECONDARY_INFO'})
        Price = a.find('span', attrs={'class': 's-item__price'})
        Shipping = a.find('span', attrs={'class': 's-item__shipping s-item__logisticsCost'})
        Country = a.find('span', attrs={'class': 's-item__location s-item__itemLocation'})
        Sold = a.find('span', attrs={'class': 'BOLD'})
        SellerInfo = a.find('span', attrs={'class': 's-item__seller-info-text'})
        if Name and Price:
            Names.append(Name.text.strip())
            Conditions.append(Condition.text.strip() if Condition else 'N/A')
            price_element = a.find('span', attrs={'class': 's-item__price'})
            if price_element:
                price_text = price_element.text.strip()
                price_number = re.findall(r'\d+\.?\d*', price_text)
                price_number = ''.join(price_number)
            else:
                price_number = '0'
            Prices.append(price_number)

            Shippings.append(Shipping.text.strip() if Shipping else 'N/A')
            Countrys.append(Country.text.strip() if Country else 'N/A')
            sold_element = a.find('apan', attrs={'class': 'BOLD'})

            # Extract the full text and keep only the integer part
            if sold_element:
                sold_text = sold_element.text.strip()
                # Use regular expression to extract only digits (integers)
                sold_number = re.findall(r'\d+', sold_text)
                # Join the list in case of multiple matches (though typically it should be just one)
                sold_number = ''.join(sold_number)
            else:
                sold_number = '0'

            Solds.append(sold_number)
            SellerInfos.append(SellerInfo.text.strip() if SellerInfo else 'N/A')
            products_processed += 1
        else:
            products_skipped += 1

    print(f"Page {i}: Processed {products_processed}, Skipped {products_skipped}")

# After all pages are scraped, write the data to CSV
df = pd.DataFrame({
    'Name': Names, 
    'Condition': Conditions, 
    'Price': Prices,
    'Shipping': Shippings, 
    'Country': Countrys,
    'Solds': Solds,
    'SellerInfo': SellerInfos
})

df.to_csv(output_csv, mode='w', header=True, index=False, encoding='utf-8')

# Close the driver
driver.quit()

print(f"Scraping complete. Data saved to {output_csv}")
