def Scrapping(self):
    #     service = Service(executable_path=r'C:\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    #     driver = webdriver.Chrome(service=service)
    #     output_csv = 'new2.csv'

    #     Names = []  
    #     Conditions = []   
    #     Prices = []
    #     Shippings = []
    #     Countrys = []
    #     Solds = []
    #     SellerInfos = []

    #     for i in range(1, 43): 
    #         print(f"Processing page {i}")
    #         page = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw=music&_sacat=267&_ipg=240&rt=nc&Format=Hardcover&_dcat=267&_pgn={i}'
    #         driver.get(page)
    #         try:
    #             WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 's-item__title')))
    #         except Exception as e:
    #             print(f"Error loading page {i}: {e}")
    #             continue 
    #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #         time.sleep(10) 
    #         content = driver.page_source
    #         soup = BeautifulSoup(content, 'html.parser')
    #         elements = soup.findAll('div', attrs={'class': 's-item__info clearfix'})
    #         products_processed = 0
    #         products_skipped = 0
    #         for a in elements:
    #             Name = a.find('div', attrs={'class': 's-item__title'})
    #             Condition= a.find('span', attrs={'class': 'SECONDARY_INFO'})
    #             Price = a.find('span', attrs={'class': 's-item__price'})
    #             Shipping = a.find('span', attrs={'class': 's-item__shipping s-item__logisticsCost'})
    #             Country = a.find('span', attrs={'class': 's-item__location s-item__itemLocation'})
    #             Sold = a.find('span', attrs={'class': 'BOLD'})
    #             SellerInfo = a.find('span', attrs={'class': 's-item__seller-info-text'})
    #             if Name and Price:
    #                 Names.append(Name.text.strip())
    #                 Conditions.append(Condition.text.strip() if Condition else 'N/A')
    #                 price_element = a.find('span', attrs={'class': 's-item__price'})
    #                 if price_element:
    #                     price_text = price_element.text.strip()
    #                     price_number = re.findall(r'\d+\.?\d*', price_text)
    #                     price_number = ''.join(price_number)
    #                 else:
    #                     price_number = '0'
    #                 Prices.append(price_number)
    #                 Shippings.append(Shipping.text.strip() if Shipping else 'N/A')
    #                 Countrys.append(Country.text.strip() if Country else 'N/A')
    #                 sold_element = a.find('apan', attrs={'class': 'BOLD'})
    #                 if sold_element:
    #                     sold_text = sold_element.text.strip()
    #                     sold_number = re.findall(r'\d+', sold_text)
    #                     sold_number = ''.join(sold_number)
    #                 else:
    #                     sold_number = '0'
    #                 Solds.append(sold_number)
    #                 SellerInfos.append(SellerInfo.text.strip() if SellerInfo else 'N/A')
    #                 products_processed += 1
    #                 self.worker.progress.emit(Names)
    #                 self.increase_progress(Names)
    #             else:
    #                 products_skipped += 1
    #         print(f"Page {i}: Processed {products_processed}, Skipped {products_skipped}")
    #         while self.worker.IsPaused:
    #             time.sleep(0.1)  # Wait
    #         if self.worker.IsRunning==False:
    #             df = pd.DataFrame({
    #         'Name': Names, 
    #         'Condition': Conditions, 
    #         'Price': Prices,
    #         'Shipping': Shippings, 
    #         'Country': Countrys,
    #         'Solds': Solds,
    #         'SellerInfo': SellerInfos
    #     })
        
    #             df.to_csv(output_csv, mode='w', header=True, index=False, encoding='utf-8')

    #             driver.quit()
    #             self.LoadTableForScrapping()

    #     df = pd.DataFrame({
    #         'Name': Names, 
    #         'Condition': Conditions, 
    #         'Price': Prices,
    #         'Shipping': Shippings, 
    #         'Country': Countrys,
    #         'Solds': Solds,
    #         'SellerInfo': SellerInfos
    #     })
    #     df.to_csv(output_csv, mode='w', header=True, index=False, encoding='utf-8')
    #     driver.quit()
    #     print(f"Scraping complete. Data saved to {output_csv}")
    #     self.LoadTableForScrapping()