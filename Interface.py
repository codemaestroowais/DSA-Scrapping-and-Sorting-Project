import sys
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
import csv
import pandas as pd
from SortingAlgorithms import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QListWidget, QListWidgetItem, QLabel, QMessageBox, QWidget
from PyQt5.QtCore import QThread, pyqtSignal
from NewScrapping import*
class Worker(QThread):
    # Signal to notify the main thread that the work is done
    finished = pyqtSignal(str)
    progress=pyqtSignal(list)
    def __init__(self, scrap_function):
        super().__init__()
        self.scrap_function = scrap_function  # Pass the scraping function
        self.IsPaused=False
        self.IsRunning=False
    def run(self):
        # Call the scraping function in the background
        self.scrap_function()  # Perform the scraping

        # After the task is done, emit a signal to update the UI
        self.finished.emit("Task Completed!")
        
    def pause(self):
        self.IsPaused = True
    def stop(self):
        # Stops the thread
        self.IsRunning = False
    def resume(self):
        self.IsPaused=False

class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        loadUi("Interface.ui", self)
        self.setWindowTitle('My Application')
        self.setStyleSheet("""
            background-color: #5271ff;
            color: white;
        """)
        button_style = """
            QPushButton {
                background-color: white;
                color: #00008b;
                border-radius: 10px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #f0f0f0;  
            }
        """
        for button in self.findChildren(QPushButton):
            button.setStyleSheet(button_style)
        input_style = """
            background-color: white;
            color: #00008b;  
            border: 2px solid #00008b;  
        """
        self.ImportButton.adjustSize()
        self.pushButton_13.adjustSize()
        self.pushButton_14.adjustSize()
        self.pushButton_15.adjustSize()
        self.pushButton_16.adjustSize()
        self.column1.setStyleSheet(input_style)
        self.column2.setStyleSheet(input_style)
        self.column3.setStyleSheet(input_style)
        self.column4.setStyleSheet(input_style)
        self.column5.setStyleSheet(input_style)
        self.column6.setStyleSheet(input_style)
        self.column7.setStyleSheet(input_style)
        self.column1.setPlaceholderText("Search by Column 1")
        self.column2.setPlaceholderText("Search by Column 2")
        self.column3.setPlaceholderText("Search by Column 3")
        self.column4.setPlaceholderText("Search by Column 4")
        self.column5.setPlaceholderText("Search by Column 5")
        self.column6.setPlaceholderText("Search by Column 6")
        self.column7.setPlaceholderText("Search by Column 7")
        self.SearchField=[]
        self.SearchField.append(self.column1)
        self.SearchField.append(self.column2)
        self.SearchField.append(self.column3)
        self.SearchField.append(self.column4)
        self.SearchField.append(self.column5)
        self.SearchField.append(self.column6)
        self.SearchField.append(self.column7)
        for combobox in self.findChildren(QComboBox):
            combobox.setStyleSheet(input_style)
        
        for table in self.findChildren(QTableWidget):
            table.setStyleSheet(input_style)
        label_style = """
            background-color: #137fc6;  
            color: white;
            padding: 4px;
            border-radius: 5px;
        """
        for label in self.findChildren(QLabel):
            label.setStyleSheet(label_style)
        self.ImportButton.clicked.connect(self.LoadDataForCSV)
        self.LoadTable()
        self.progressBar.setValue(0)
        self.BubbleSortButton.clicked.connect(self.BubbleSort)
        self.SelectionSortButton.clicked.connect(self.SelectionSort)
        self.InsertionSortButton.clicked.connect(self.InsertionSort)
        self.MergeSortButton.clicked.connect(self.MergeSort)
        self.QuickSortButton.clicked.connect(self.QuickSort)
        self.CountingSortButton.clicked.connect(self.CountingSort)
        self.RadixSortButton.clicked.connect(self.RadixSort)
        self.BucketSortButton.clicked.connect(self.BucketSort)
        self.CombSortButton.clicked.connect(self.CombSort)
        self.SearchButton.clicked.connect(self.searching)
        self.pushButton_16.clicked.connect(self.StartScrapping)
        self.pushButton_15.clicked.connect(self.Resumescrapping)
        self.pushButton_13.clicked.connect(self.pausescrapping)
        self.pushButton_14.clicked.connect(self.stopscrapping)
        
    def pausescrapping(self):
        if self.worker:
            self.worker.pause()
    def Resumescrapping(self):
        if self.worker:
            self.worker.resume()
    def stopscrapping(self):
        if self.worker:
            self.worker.stop()
    def increaseprogress(self, value):
        # Get the current value of the progress bar
        current_value = self.progressBar.value()
        length=len(value)
        percentage=(length/25000)*100
        # Set the new value (increase by 10 until it reaches 100)
        if current_value < 100:
            self.progressBar.setValue(percentage)
    def StartScrapping(self):
        self.worker = Worker(self.Scrapping)
        self.worker.IsRunning=True
        if self.worker.IsRunning==True:
            self.worker.start()
    def LoadDataForCSV(self):
        self.Table.setRowCount(0)
        df=ReadArrayFromCsv('new4.csv')
        colums=df.columns
        rows=df.to_numpy()
        list=[]
        for row in rows:
            list.append(row)
        lists=[]
        for number in list:
            lists.append(number)
        self.Table.setRowCount(len(list))
        roww=0
        for row in list:
            row[0]=str(row[0])
            row[1]=str(row[1])
            row[2]=str(row[2])
            row[3]=str(row[3])
            row[4]=str(row[4])
            row[5]=str(row[5])
            row[6]=str(row[6])
            self.Table.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row[0])))
            self.Table.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row[1])))
            self.Table.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row[2])))
            self.Table.setItem(roww, 3 , QtWidgets.QTableWidgetItem((row[3])))
            self.Table.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row[4])))
            self.Table.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row[5])))
            self.Table.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row[6])))
            roww +=1
        return lists
    def LoadTable(self):
        self.Table.setColumnCount(7)
        self.Table.setHorizontalHeaderLabels(['Name','Sold','Price','PreviousPrice','Discount','ShippingRate','Seller'])    
    def BubbleSort(self):
        number=[]
        if(self.SelectingColumnsComboBox.currentText()!='None'):
            number.append(int(self.SelectingColumnsComboBox.currentText()))
        if(self.SelectingColumnsComboBox_2.currentText()!="None"):
            number.append(int(self.SelectingColumnsComboBox_2.currentText()))    
        if len(number)>0:
            List=self.GetAllData()
            List=self.convertdatatooriginaltype(List)
            SortedList=[]
            SortedList=BubbleSort(List, number)
            self.UpdateTable(SortedList)
        else:
            self.ShowMessageBox("no column selected", 'Information')
    def SelectionSort(self):
        number=[]
        if(self.SelectingColumnsComboBox.currentText()!='None'):
            number.append(int(self.SelectingColumnsComboBox.currentText()))
        if(self.SelectingColumnsComboBox_2.currentText()!="None"):
            number.append(int(self.SelectingColumnsComboBox_2.currentText()))    
        if len(number)>0:
            List=self.GetAllData()
            List=self.convertdatatooriginaltype(List)
            SortedList=[]
            SortedList=SelectionSort(List, number)
            self.UpdateTable(SortedList)
        else:
            self.ShowMessageBox("no column selected", 'Information') 
    def MergeSort(self):
        number=[]
        if(self.SelectingColumnsComboBox.currentText()!='None'):
            number.append(int(self.SelectingColumnsComboBox.currentText()))
        if(self.SelectingColumnsComboBox_2.currentText()!="None"):
            number.append(int(self.SelectingColumnsComboBox_2.currentText()))    
        if len(number)>0:
            List=self.GetAllData()
            List=self.convertdatatooriginaltype(List)
            SortedList=[]
            SortedList=MergeSort(List, number)
            self.UpdateTable(SortedList)
        else:
            self.ShowMessageBox("no column selected", 'Information') 
    def InsertionSort(self):
        number=[]
        if(self.SelectingColumnsComboBox.currentText()!='None'):
            number.append(int(self.SelectingColumnsComboBox.currentText()))
        if(self.SelectingColumnsComboBox_2.currentText()!="None"):
            number.append(int(self.SelectingColumnsComboBox_2.currentText()))    
        if len(number)>0:
            List=self.GetAllData()
            List=self.convertdatatooriginaltype(List)
            SortedList=[]
            SortedList=InsertionSort(List, number)
            self.UpdateTable(SortedList)
        else:
            self.ShowMessageBox("no column selected", 'Information')    
    def QuickSort(self):
        number=[]
        if(self.SelectingColumnsComboBox.currentText()!='None'):
            number.append(int(self.SelectingColumnsComboBox.currentText()))
        if(self.SelectingColumnsComboBox_2.currentText()!="None"):
            number.append(int(self.SelectingColumnsComboBox_2.currentText()))    
        if len(number)>0:
            List=self.GetAllData()
            List=self.convertdatatooriginaltype(List)
            SortedList=[]
            SortedList=QuickSort(List, number)
            self.UpdateTable(SortedList)
        else:
            self.ShowMessageBox("no column selected", 'Information') 
    def CountingSort(self):
        
        number=[]
        if(self.SelectingColumnsComboBox.currentText()!='None'):
            number.append(int(self.SelectingColumnsComboBox.currentText()))
        if(self.SelectingColumnsComboBox_2.currentText()!="None"):
            number.append(int(self.SelectingColumnsComboBox_2.currentText())) 
        if len(number)>0:
            if 0 in number or 1 in number or 3 in number or 4 in number or 6 in number  or 2 in number:  
                self.ShowMessageBox("Wrong column selected", 'Information')        
            else:
                List=self.GetAllData()
                List=self.convertdatatooriginaltype(List)
                SortedList=[]
                SortedList=CountingSort(List, number)
                self.UpdateTable(SortedList)
        else:
            self.ShowMessageBox("no column selected", 'Information') 
    def RadixSort(self):
        number=[]
        if(self.SelectingColumnsComboBox.currentText()!='None'):
            number.append(int(self.SelectingColumnsComboBox.currentText()))
        if(self.SelectingColumnsComboBox_2.currentText()!="None"):
            number.append(int(self.SelectingColumnsComboBox_2.currentText()))    
        if len(number)>0:
            List=self.GetAllData()
            List=self.convertdatatooriginaltype(List)
            SortedList=[]
            SortedList=RadixSort(List, number)
            self.UpdateTable(SortedList)
        else:
            self.ShowMessageBox("no column selected", 'Information')
    def BucketSort(self):
        number=[]
        if(self.SelectingColumnsComboBox.currentText()!='None'):
            number.append(int(self.SelectingColumnsComboBox.currentText()))
        if(self.SelectingColumnsComboBox_2.currentText()!="None"):
            number.append(int(self.SelectingColumnsComboBox_2.currentText()))    
        if len(number)>0:
            List=self.GetAllData()
            List=self.convertdatatooriginaltype(List)
            SortedList=[]
            SortedList==BucketSort(List, number)
            self.UpdateTable(SortedList)
        else:
            self.ShowMessageBox("no column selected", 'Information')
    def OddEvenSort(self):
        number=[]
        if(self.SelectingColumnsComboBox.currentText()!='None'):
            number.append(int(self.SelectingColumnsComboBox.currentText()))
        if(self.SelectingColumnsComboBox_2.currentText()!="None"):
            number.append(int(self.SelectingColumnsComboBox_2.currentText()))    
        if len(number)>0:
            List=self.GetAllData()
            List=self.convertdatatooriginaltype(List)
            SortedList=[]
            SortedList=OddEvenSort(List, number)
            self.UpdateTable(SortedList)
        else:
            self.ShowMessageBox("no column selected", 'Information')
    def CombSort(self):
        number=[]
        if(self.SelectingColumnsComboBox.currentText()!='None'):
            number.append(int(self.SelectingColumnsComboBox.currentText()))
        if(self.SelectingColumnsComboBox_2.currentText()!="None"):
            number.append(int(self.SelectingColumnsComboBox_2.currentText()))    
        if len(number)>0:
            List=self.GetAllData()
            List=self.convertdatatooriginaltype(List)
            SortedList=[]
            SortedList=CombSort(List, number)
            self.UpdateTable(SortedList)
        else:
            self.ShowMessageBox("no column selected", 'Information')
    def GenomeSort(self):
        number=[]
        if(self.SelectingColumnsComboBox.currentText()!='None'):
            number.append(int(self.SelectingColumnsComboBox.currentText()))
        if(self.SelectingColumnsComboBox_2.currentText()!="None"):
            number.append(int(self.SelectingColumnsComboBox_2.currentText()))    
        if len(number)>0:
            List=self.GetAllData()
            List=self.convertdatatooriginaltype(List)
            SortedList=[]
            SortedList=GenomeSort(List, number)
            self.UpdateTable(SortedList)
        else:
            self.ShowMessageBox("no column selected", 'Information')
    def ShowMessageBox(self, Message, Title):
       # Create a message box
       msg_box = QMessageBox()
       # Set the title and text of the message box
       msg_box.setWindowTitle(Title)
       msg_box.setText(Message)
       msg_box.setIcon(QMessageBox.Information)  # Set the icon (Information, Warning, Critical, etc.)
       
       # Add buttons (Yes, No, Cancel, etc.)
       msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
       # Show the message box and capture the user's response
       response = msg_box.exec_()
       # Handle the user's response
       if response == QMessageBox.Ok:
           print("User clicked OK")
       else:
           print("User clicked Cancel")
    def convertdatatooriginaltype(self, table_data):
        column_types = []
        for col_idx in range(len(table_data[0])):
            is_string = False
            is_float = False
            is_int = False
            for row in table_data:
                value = row[col_idx]
                try:
                    float_value = float(value)
                    if float_value.is_integer():
                        is_int = True
                    else:
                        is_float = True
                except ValueError:
                    is_string = True
                    break
            if is_string:
                column_types.append(str)
            elif is_float:
                column_types.append(float)
            else:
                column_types.append(int)

        converted_data = []
        for row in table_data:
            converted_row = []
            for col_idx, value in enumerate(row):
                converted_row.append(column_types[col_idx](value))
            converted_data.append(converted_row)

        return converted_data   
    def GetAllData(self):
        # Get the number of rows and columns
        row_count = self.Table.rowCount()
        column_count = self.Table.columnCount()

        # Retrieve all data from the table
        all_data = []
        for row in range(row_count):
            row_data = []
            for column in range(column_count):
                item = self.Table.item(row, column)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append('')  # Handle empty cells
            all_data.append(row_data)
        return all_data        
    def UpdateTable(self, List):
        self.Table.setRowCount(0)
        self.Table.setRowCount(len(List))
        roww=0
        for row in List:
            row[0]=str(row[0])
            row[1]=str(row[1])
            row[2]=str(row[2])
            row[3]=str(row[3])
            row[4]=str(row[4])
            row[5]=str(row[5])
            row[6]=str(row[6])
            self.Table.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row[0])))
            self.Table.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row[1])))
            self.Table.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row[2])))
            self.Table.setItem(roww, 3 , QtWidgets.QTableWidgetItem((row[3])))
            self.Table.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row[4])))
            self.Table.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row[5])))
            self.Table.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row[6])))
            roww +=1  
    def searching(self):
        variable = self.comboBox.currentText().strip()
        condition_type = self.comboBox_2.currentText().strip()  
        search_values = [field.text().strip().lower() for field in self.SearchField]

        for row in range(self.Table.rowCount()):
            if condition_type == 'AND':
                show_row = True 
            elif condition_type == 'OR':
                show_row = False 
            elif condition_type == 'NOT':
                show_row = True  
                
            for col in range(self.Table.columnCount()):
                item = self.Table.item(row, col)
                search_value = search_values[col]

                if item is not None:
                    item_text = item.text().lower()

                    if variable == 'Contains':
                        condition_met = search_value and search_value in item_text
                    elif variable == 'Starts with':
                        condition_met = search_value and item_text.startswith(search_value)
                    elif variable == 'Ends with':
                        condition_met = search_value and item_text.endswith(search_value)

                    if condition_type == 'AND':
                        if search_value and not condition_met:
                            show_row = False
                            break 
                    elif condition_type == 'OR':
                        if search_value and condition_met:
                            show_row = True
                            break 
                    elif condition_type == 'NOT':
                       
                        if search_value and condition_met:
                            show_row = False
                            break 
                else:
                    if search_value:
                        if condition_type == 'AND':
                            show_row = False
                            break
                        elif condition_type == 'NOT':
                            continue  
            self.Table.setRowHidden(row, not show_row)
    def Scrapping(self):
        service = Service(executable_path=r'C:\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        output_csv = 'Output.csv'

        Names = []  
        Conditions = []   
        Prices = []
        Shippings = []
        Countrys = []
        Solds = []
        SellerInfos = []

        for i in range(1, 43): 
            print(f"Processing page {i}")
            page = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw=music&_sacat=267&_ipg=240&rt=nc&Format=Hardcover&_dcat=267&_pgn={i}'
            driver.get(page)
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 's-item__title')))
            except Exception as e:
                print(f"Error loading page {i}: {e}")
                continue 
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(10) 
            content = driver.page_source
            soup = BeautifulSoup(content, 'html.parser')
            elements = soup.findAll('div', attrs={'class': 's-item__info clearfix'})
            products_processed = 0
            products_skipped = 0
            for a in elements:
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
                    if sold_element:
                        sold_text = sold_element.text.strip()
                        sold_number = re.findall(r'\d+', sold_text)
                        sold_number = ''.join(sold_number)
                    else:
                        sold_number = '0'
                    Solds.append(sold_number)
                    SellerInfos.append(SellerInfo.text.strip() if SellerInfo else 'N/A')
                    products_processed += 1
                    self.worker.progress.emit(Names)
                    self.increaseprogress(Names)
                else:
                    products_skipped += 1
            print(f"Page {i}: Processed {products_processed}, Skipped {products_skipped}")
            while self.worker.IsPaused:
                time.sleep(0.1)  # Wait
            if self.worker.IsRunning==False:
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
                driver.quit()
                self.LoadTableForScrapping()
                return

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
        driver.quit()
        print(f"Scraping complete. Data saved to {output_csv}")
        self.LoadTableForScrapping()
    def LoadTableForScrapping(self):
        self.Table.setRowCount(0)
        df=ReadArrayFromCsv('Output.csv')
        colums=df.columns
        rows=df.to_numpy()
        list=[]
        for row in rows:
            list.append(row)
        lists=[]
        for number in list:
            lists.append(number)
        self.Table.setRowCount(len(list))
        roww=0
        for row in list:
            row[0]=str(row[0])
            row[1]=str(row[1])
            row[2]=str(row[2])
            row[3]=str(row[3])
            row[4]=str(row[4])
            row[5]=str(row[5])
            row[6]=str(row[6])
            self.Table.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row[0])))
            self.Table.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row[1])))
            self.Table.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row[2])))
            self.Table.setItem(roww, 3 , QtWidgets.QTableWidgetItem((row[3])))
            self.Table.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row[4])))
            self.Table.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row[5])))
            self.Table.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row[6])))
            roww +=1
        return lists 


app = QApplication(sys.argv)
window = Mainwindow()
window.show()
sys.exit(app.exec_())
