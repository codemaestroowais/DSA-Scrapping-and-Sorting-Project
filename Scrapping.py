from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# File path for the output CSV (use relative or absolute path as needed)
output_csv = 'new1.csv'

# Check if the file exists to avoid writing the header again if appending
file_exists = os.path.isfile(output_csv)

# Set up the WebDriver
service = Service(executable_path=r'C:\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
#options = webdriver.ChromeOptions()
#options.add_argument('headless')  # Run in headless mode (optional)
driver = webdriver.Chrome(service=service)

# Lists to store scraped data
Name_list = []
Sold_list = []
Price_list = []
PreviousPrice_list = []
Discount_list = []
ShippingRate_list = []
Seller_list = []

# Loop through the pages (modify range as needed)
for i in range(1, 2):  # Increase the range to scrape more pages
    print(f"Processing page {i}")
    page = f'https://www.aliexpress.com/w/wholesale-makeup-set.html?page={i}&g=y&SearchText=makeup+set'
    driver.get(page)

    try:
        # Wait for the main product grid to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.list-item')))
    except Exception as e:
        print(f"Error loading page {i}: {e}")
        continue

    # Scroll down to load more products dynamically
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)  # Wait for additional products to load

    # Parse page source with BeautifulSoup
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    elements = soup.find_all('div','multi--content--11nFIBL')

    products_processed = 0
    products_skipped = 0

    # Extract data for each product
    # Assuming 'soup' and 'elements' have already been initialized
for elem in elements:
    # Update the CSS selectors based on your inspection of the website
    name_elem = elem.select_one('.manhattan--titleText--WccSjUS')  # Use class name from website
    sold_elem = elem.select_one('.manhattan--trade--2PeJIEB')
    price_elem = elem.select_one('.manhattan--price-sale--1CCSZfK')
    
    # Make sure to fetch the previous price for each product, inside the loop
    previous_price_elem = elem.select_one('.multi--price-original--1zEQqOK span')

    discount_elem = elem.select_one('.multi--discount--2aBXi8A')
    shipping_rate_elem = elem.select_one('.multi--serviceIcon--1DDzBtl')
    seller_elem = elem.select_one('.store--name--2rTqiE4')

    # Check if name and price exist to process the product
    if name_elem and price_elem:
        Name_list.append(name_elem.text.strip())
        Sold_list.append(sold_elem.text.strip() if sold_elem else 'N/A')
        Price_list.append(price_elem.text.strip())
        PreviousPrice_list.append(previous_price_elem.text.strip() if previous_price_elem else 'N/A')
        Discount_list.append(discount_elem.text.strip() if discount_elem else 'N/A')
        ShippingRate_list.append(shipping_rate_elem.text.strip() if shipping_rate_elem else 'N/A')
        Seller_list.append(seller_elem.text.strip() if seller_elem else 'N/A')
        products_processed += 1
    else:
        products_skipped += 1


    print(f"Page {i}: Processed {products_processed} products, Skipped {products_skipped} products")

# Check if any data was actually scraped
if Name_list:
    # Create DataFrame from the scraped data
    df = pd.DataFrame({
        'Name': Name_list,
        'Sold': Sold_list,
        'Price': Price_list,
        'PreviousPrice': PreviousPrice_list,
        'Discount': Discount_list,
        'ShippingRate': ShippingRate_list,
        'Seller': Seller_list
    })

    # Append data to CSV if the file exists, otherwise create a new file
    df.to_csv(output_csv, mode='a', header=not file_exists, index=False)
    print(f"Scraping complete. Data saved to {output_csv}")
else:
    print("No data was scraped.")

# Close the browser
driver.quit()