from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path=r'C:\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)
output_csv = 'new1.csv'

Name_list = []
Sold_list = []
Price_list = []
PreviousPrice_list = []
Discount_list = []
ShippingRate_list = []
Seller_list = []
for i in range(1, 61):
    print(f"Processing page {i}")
    page = f'https://www.aliexpress.com/w/wholesale-makeup-set.html?page={i}&g=y&SearchText=makeup+set'
    driver.get(page)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'multi--content--11nFIBL')))
    except Exception as e:
        print(f"Error loading page {i}: {e}")
        continue  
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(10)
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    elements = soup.findAll('div', attrs={'class': 'multi--content--11nFIBL'})
    products_processed = 0
    products_skipped = 0
    for elem in elements:
        name_elem = elem.find('h3', attrs={'class': 'multi--titleText--nXeOvyr'})
        sold_elem = elem.find('span', attrs={'class': 'multi--trade--Ktbl2jB'})
        price_elem = elem.find('div', attrs={'class': 'multi--price-sale--U-S0jtj'})
        previous_price_elem = elem.find('div', attrs={'class': 'multi--price-original--1zEQqOK'})
        discount_elem = elem.find('span', attrs={'class': 'multi--discount--3hksz5G'})
        shipping_rate_elem = elem.find('span', attrs={'class': 'tag--text--1BSEXVh tag--textStyle--3dc7wLU multi--serviceStyle--1Z6RxQ4'})
        seller_elem = elem.find('span', attrs={'class': 'cards--store--3GyJcot'})
        if name_elem:
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

    print(f"Page {i}: Processed {products_processed}, Skipped {products_skipped}")

df = pd.DataFrame({
    'Name': Name_list,
    'Sold': Sold_list,
    'Price': Price_list,
    'PreviousPrice': PreviousPrice_list,
    'Discount': Discount_list,
    'ShippingRate': ShippingRate_list,
    'Seller': Seller_list
})
df.to_csv(output_csv, mode='w', header=True, index=False, encoding='utf-8')
driver.quit()
print(f"Scraping complete. Data saved to {output_csv}")