# Basic libraries to import for completing the whole work.
from Chat1 import *
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
import time
from PyQt5.QtCore import QThread, pyqtSignal

class Worker(QThread):
    finished = pyqtSignal(str)
    progress=pyqtSignal(list)
    def __init__(self, scrap_function):
        super().__init__()
        self.scrap_function = scrap_function
        self.IsPaused=False
        self.IsRunning=False
    def run(self):
        self.scrap_function()  
        self.finished.emit("Task Completed!")
        
    def pause(self):
        self.IsPaused = True
    def stop(self):
        self.IsRunning = False
    def resume(self):
        self.IsPaused=False
class Mainwindow(QMainWindow):
    def __init__(self):
        loadUi("GUI.ui",self)
        super(Mainwindow,self).__init__()
        self.SelectedNumbers=[]
        self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.setWindowTitle('My Application')
        self.DataList=[]
        self.LoadTable()
        self.SortButton.clicked.connect(self.StartSorting)
        self.LoadButton.clicked.connect(self.LoadData)
        self.SelectButton.clicked.connect(self.open_number_selection)
        self.SearchButton.clicked.connect(self.perform_search)
        self.AgainLoadButton.clicked.connect(self.LoadTableForCSV)
        self.progressBar.setValue(0)
        self.FirstLabel.adjustSize()
        self.SearchBar1.setPlaceholderText('Search Column 1')
        self.SearchBar2.setPlaceholderText('Search Column 2')
        self.SearchBar3.setPlaceholderText('Search Column 3')
        self.SearchBar4.setPlaceholderText('Search Column 4')
        self.SearchBar5.setPlaceholderText('Search Column 5')
        self.SearchBar6.setPlaceholderText('Search Column 6')
        self.SearchBar7.setPlaceholderText('Search Column 7')
        self.RestartButton.clicked.connect(self.StartScrapping)
        self.PauseButton.clicked.connect(self.pause_scrapping)
        self.StopButton.clicked.connect(self.stop_scrapping)
        self.ResumeButton.clicked.connect(self.Resume_scrapping)

        self.SearchField=[]
        self.SearchField.append(self.SearchBar1)
        self.SearchField.append(self.SearchBar2)
        self.SearchField.append(self.SearchBar3)
        self.SearchField.append(self.SearchBar4)
        self.SearchField.append(self.SearchBar5)
        self.SearchField.append(self.SearchBar6)
        self.SearchField.append(self.SearchBar7)
        text=self.LoadDataComboBox.currentText()
        self.worker = None
    
    
    def is_column_string(table_data, column_indices):
        flag=False
        for column_idx in column_indices:
            for value in [row[column_idx] for row in table_data]:
                try:
                    float(value)  or int(value)
                except ValueError:
                    flag=True
                    return True
                    break  
        return flag        
        
    def pause_scrapping(self):
        if self.worker:
            self.worker.pause()
    def Resume_scrapping(self):
        if self.worker:
            self.worker.resume()
    def stop_scrapping(self):
        if self.worker:
            self.worker.stop()
    def increase_progress(self, value):
        current_value = self.progressBar.value()
        length=len(value)
        percentage=(length/100)*100
        if current_value < 100:
            self.progressBar.setValue(percentage)
            
    def perform_search(self):
        variable=self.comboBox.currenttext()
        search_values = [field.text().lower() for field in self.SearchField]
        for row in range(self.DataTable.rowCount()):
            show_row = True
            for col in range(self.DataTable.columnCount()):
                item = self.DataTable.item(row, col)
                if item is not None:
                    item_text = item.text().lower()
                    if variable == 'Contains':
                        if search_values[col] and search_values[col] not in item_text:
                            show_row = False
                            break
                    elif variable == 'Starts with':
                        if search_values[col] and not item_text.startswith(search_values[col]):
                            show_row = False
                            break
                    elif variable == 'Ends with':
                        if search_values[col] and not item_text.endswith(search_values[col]):
                            show_row = False
                            break
                else:
                    if search_values[col]:
                        show_row = False
                        break
            self.DataTable.setRowHidden(row, not show_row)
        
    def LoadData(self):
        text=self.LoadDataComboBox.currentText()
        if text=="Read from CSV file":
            DataList=self.LoadTableForCSV()
    def StartScrapping(self):
        self.worker = Worker(self.Scrapping)
        self.worker.IsRunning=True
        if self.worker.IsRunning==True:
            self.worker.start()

    def is_column_string(column_data):
        for value in column_data:
            try:
                float(value) or int(value)  
            except ValueError:
                return True  
        return False
            
    def ClearAllData(self):
        self.DataTable.setRowCount(0)  
        
    def ShowSelectedOption(self):
        selected_option = self.SortingComboBox.currentText()
        return selected_option 
    
    def LoadTable(self):
        self.DataTable.setColumnCount(7)
        self.DataTable.setHorizontalHeaderLabels(['Mobile Name','Price','Discount','Rating','Company Name','Description','Color'])    
    def LoadTableForCSV(self):
        self.DataTable.setRowCount(0)
        df=ReadArrayFromCsv('data.csv')
        colums=df.columns
        self.DataTable.setColumnCount(7)
        self.DataTable.setHorizontalHeaderLabels(['Mobile Name','Price','Discount','Rating','Company Name','Description','Color'])
        rows=df.to_numpy()
        list=[]
        for row in rows:
            list.append(row)
        lists=[]
        for number in list:
            lists.append(number)
        self.DataTable.setRowCount(len(list))
        roww=0
        for row in list:
            row[0]=str(row[0])
            row[1]=str(row[1])
            row[2]=str(row[2])
            row[3]=str(row[3])
            row[4]=str(row[4])
            row[5]=str(row[5])
            row[6]=str(row[6])
            self.DataTable.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row[0])))
            self.DataTable.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row[1])))
            self.DataTable.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row[2])))
            self.DataTable.setItem(roww, 3 , QtWidgets.QTableWidgetItem((row[3])))
            self.DataTable.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row[4])))
            self.DataTable.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row[5])))
            self.DataTable.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row[6])))
            roww +=1
        return lists 
    
        
    def TextFromCombobox(self):
        selected_option = self.SortingComboBox.currentText()
        return selected_option
    
    def GetAllData(self):
        row_count = self.DataTable.rowCount()
        column_count = self.DataTable.columnCount()
        all_data = []
        for row in range(row_count):
            row_data = []
            for column in range(column_count):
                item = self.DataTable.item(row, column)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append('')
            all_data.append(row_data)
        return all_data
    def StartSorting(self):
        print(self.SelectedNumbers)
        if len(self.SelectedNumbers)>0:
            print("hamdan")
            Text=self.TextFromCombobox()
            Sort=Text
            list=self.GetAllData()
            TimeTaken=0
            if len(list)>0:
                SortedList=[]
                if Text=="Bubble Sort":
                    print("bubble Sort")
                    start=time.time()
                    SortedList=BubbleSort(list, self.SelectedNumbers)
                    print(SortedList)
                    print("owais")
                    End=time.time()
                    TimeTaken=End-start
                elif Text=="Selection Sort":
                    start=time.time()
                    SortedList=SelectionSort(list, self.SelectedNumbers)
                    End=time.time()
                    TimeTaken=End-start
                elif Text=="Insertion Sort":
                    start=time.time()
                    SortedList=InsertionSort(list, self.SelectedNumbers)
                    End=time.time()
                    TimeTaken=End-start
                elif Text=="Merge Sort":
                    start=time.time()
                    SortedList=MergeSort(list, self.SelectedNumbers)
                    End=time.time()
                    TimeTaken=End-start
                elif Text=="Quick Sort":
                    start=time.time()
                    SortedList=QuickSort(list, self.SelectedNumbers)
                    End=time.time()
                    TimeTaken=End-start
                elif Text=="Counting Sort":
                    start=time.time()
                    SortedList=CountingSort(list, self.SelectedNumbers)
                    End=time.time()
                    TimeTaken=End-start
                elif Text=="Radix Sort":
                    start=time.time()
                    SortedList=RadixSort(list, self.SelectedNumbers)
                    End=time.time()
                    TimeTaken=End-start
                elif Text=="Bucket Sort":
                    start=time.time()
                    SortedList=BucketSort(list, self.SelectedNumbers)
                    End=time.time()
                    TimeTaken=End-start
                elif Text=="Shell Sort":
                    start=time.time()
                    SortedList=Sort(list, self.SelectedNumbers)
                    End=time.time()
                    TimeTaken=End-start
                if SortedList:
                    self.SelectedNumbers=None
                    self.ClearAllData()
                    self.UpdateTable(SortedList)
                    Message=f"The taken for {Sort} is {TimeTaken} s"
                    self.ShowMessageBox(Message, "Information")
            else:
                self.SelectedNumbers=None
                self.ShowMessageBox("No Data to Sort", "Message")
        else:
            self.ShowMessageBox("No Columns Selected.", "Infromation")
     
    def Search(self):
        List=self.GetAllData()
        list1=[]
        list1.append(self.SearchBar1.text())
        list1.append(self.SearchBar2.text())
        list1.append(self.SearchBar3.text())
        list1.append(self.SearchBar4.text())
        list1.append(self.SearchBar5.text())
        list1.append(self.SearchBar6.text())
        list1.append(self.SearchBar7.text())
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
    
    
    def UpdateTable(self, List):
        self.DataTable.setRowCount(0)
        self.DataTable.setRowCount(len(List))
        roww=0
        for row in List:
            row[0]=str(row[0])
            row[1]=str(row[1])
            row[2]=str(row[2])
            row[3]=str(row[3])
            row[4]=str(row[4])
            row[5]=str(row[5])
            row[6]=str(row[6])
            self.DataTable.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row[0])))
            self.DataTable.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row[1])))
            self.DataTable.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row[2])))
            self.DataTable.setItem(roww, 3 , QtWidgets.QTableWidgetItem((row[3])))
            self.DataTable.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row[4])))
            self.DataTable.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row[5])))
            self.DataTable.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row[6])))
            roww +=1    
        
    def open_number_selection(self):
        list_widget = QListWidget()
        list_widget.setSelectionMode(QListWidget.MultiSelection)
        for i in range(0, 7):
            item = QListWidgetItem(str(i))
            list_widget.addItem(item)
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Select Numbers")
        msg_box.setText("Please select the numbers you want.")
        layout = msg_box.layout()
        layout.addWidget(list_widget)
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        response = msg_box.exec_()
        if response == QMessageBox.Ok:
            selected_items = list_widget.selectedItems()
            self.SelectedNumbers = [int(item.text()) for item in selected_items]
            selected_numbers_str = ', '.join([str(num) for num in self.SelectedNumbers])
    def Scrapping():
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
            for _ in range(5): 
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3) 
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

app = QApplication(sys.argv)
window = Mainwindow()
window.show()
sys.exit(app.exec_())