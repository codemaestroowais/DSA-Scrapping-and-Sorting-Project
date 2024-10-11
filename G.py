# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(765, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.FirstLabel = QtWidgets.QLabel(self.centralwidget)
        self.FirstLabel.setGeometry(QtCore.QRect(40, 358, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.FirstLabel.setFont(font)
        self.FirstLabel.setObjectName("FirstLabel")
        self.SortingButton = QtWidgets.QPushButton(self.centralwidget)
        self.SortingButton.setGeometry(QtCore.QRect(770, 390, 71, 21))
        self.SortingButton.setObjectName("SortingButton")
        self.LoadLabel = QtWidgets.QLabel(self.centralwidget)
        self.LoadLabel.setGeometry(QtCore.QRect(40, 298, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.LoadLabel.setFont(font)
        self.LoadLabel.setObjectName("LoadLabel")
        self.LoadDataComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.LoadDataComboBox.setGeometry(QtCore.QRect(40, 318, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.LoadDataComboBox.setFont(font)
        self.LoadDataComboBox.setObjectName("LoadDataComboBox")
        self.LoadDataComboBox.addItem("")
        self.LoadDataComboBox.addItem("")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 298, 481, 159))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SearchBar1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.SearchBar1.setObjectName("SearchBar1")
        self.verticalLayout.addWidget(self.SearchBar1)
        self.SearchBar2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.SearchBar2.setObjectName("SearchBar2")
        self.verticalLayout.addWidget(self.SearchBar2)
        self.SearchBar3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.SearchBar3.setObjectName("SearchBar3")
        self.verticalLayout.addWidget(self.SearchBar3)
        self.SearchBar4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.SearchBar4.setObjectName("SearchBar4")
        self.verticalLayout.addWidget(self.SearchBar4)
        self.SearchBar5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.SearchBar5.setObjectName("SearchBar5")
        self.verticalLayout.addWidget(self.SearchBar5)
        self.SearchBar6 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.SearchBar6.setObjectName("SearchBar6")
        self.verticalLayout.addWidget(self.SearchBar6)
        self.SearchBar7 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.SearchBar7.setObjectName("SearchBar7")
        self.verticalLayout.addWidget(self.SearchBar7)
        self.SelectLabel = QtWidgets.QLabel(self.centralwidget)
        self.SelectLabel.setGeometry(QtCore.QRect(40, 394, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.SelectLabel.setFont(font)
        self.SelectLabel.setObjectName("SelectLabel")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(240, 260, 301, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(240, 460, 291, 82))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.PauseButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.PauseButton.setFont(font)
        self.PauseButton.setObjectName("PauseButton")
        self.verticalLayout_2.addWidget(self.PauseButton)
        self.ResumeButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ResumeButton.setFont(font)
        self.ResumeButton.setObjectName("ResumeButton")
        self.verticalLayout_2.addWidget(self.ResumeButton)
        self.RestartButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.RestartButton.setFont(font)
        self.RestartButton.setObjectName("RestartButton")
        self.verticalLayout_2.addWidget(self.RestartButton)
        self.StopButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.StopButton.setFont(font)
        self.StopButton.setObjectName("StopButton")
        self.verticalLayout_2.addWidget(self.StopButton)
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(660, 308, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.SearchButton.setFont(font)
        self.SearchButton.setObjectName("SearchButton")
        self.AgainLoadButton = QtWidgets.QPushButton(self.centralwidget)
        self.AgainLoadButton.setGeometry(QtCore.QRect(660, 338, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.AgainLoadButton.setFont(font)
        self.AgainLoadButton.setObjectName("AgainLoadButton")
        self.SortingComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.SortingComboBox.setGeometry(QtCore.QRect(40, 378, 101, 20))
        self.SortingComboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SortingComboBox.setObjectName("SortingComboBox")
        self.SortingComboBox.addItem("")
        self.SortingComboBox.addItem("")
        self.SortingComboBox.addItem("")
        self.SortingComboBox.addItem("")
        self.SortingComboBox.addItem("")
        self.SortingComboBox.addItem("")
        self.SortingComboBox.addItem("")
        self.SortingComboBox.addItem("")
        self.SortingComboBox.addItem("")
        self.SortingComboBox.addItem("")
        self.SortingComboBox.addItem("")
        self.SortingComboBox.addItem("")
        self.SortingComboBox.setItemText(11, "")
        self.SelectButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.SelectButton_2.setGeometry(QtCore.QRect(40, 418, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.SelectButton_2.setFont(font)
        self.SelectButton_2.setObjectName("SelectButton_2")
        self.LoadButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.LoadButton_2.setGeometry(QtCore.QRect(40, 340, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.LoadButton_2.setFont(font)
        self.LoadButton_2.setAutoFillBackground(False)
        self.LoadButton_2.setObjectName("LoadButton_2")
        self.DataTable = QtWidgets.QTableWidget(self.centralwidget)
        self.DataTable.setGeometry(QtCore.QRect(40, 10, 691, 241))
        self.DataTable.setObjectName("DataTable")
        self.DataTable.setColumnCount(0)
        self.DataTable.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 765, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.FirstLabel.setText(_translate("MainWindow", "Sorting Algorithm:"))
        self.SortingButton.setText(_translate("MainWindow", "PushButton"))
        self.LoadLabel.setText(_translate("MainWindow", "Load data: "))
        self.LoadDataComboBox.setItemText(0, _translate("MainWindow", "Read from CSV file"))
        self.LoadDataComboBox.setItemText(1, _translate("MainWindow", "Scrapping Data"))
        self.SelectLabel.setText(_translate("MainWindow", "No of columns sort:"))
        self.PauseButton.setText(_translate("MainWindow", "PAUSE"))
        self.ResumeButton.setText(_translate("MainWindow", "RESUME"))
        self.RestartButton.setText(_translate("MainWindow", "RESTART"))
        self.StopButton.setText(_translate("MainWindow", "STOP"))
        self.SearchButton.setText(_translate("MainWindow", "INSPECT"))
        self.AgainLoadButton.setText(_translate("MainWindow", "Import Data"))
        self.SortingComboBox.setItemText(0, _translate("MainWindow", "BUBBLE SORT"))
        self.SortingComboBox.setItemText(1, _translate("MainWindow", "SELECTION SORT"))
        self.SortingComboBox.setItemText(2, _translate("MainWindow", "INSERTION SORT"))
        self.SortingComboBox.setItemText(3, _translate("MainWindow", "MERGE SORT "))
        self.SortingComboBox.setItemText(4, _translate("MainWindow", "QUICK SORT"))
        self.SortingComboBox.setItemText(5, _translate("MainWindow", "COUNTING SORTt"))
        self.SortingComboBox.setItemText(6, _translate("MainWindow", "RADIX SORT"))
        self.SortingComboBox.setItemText(7, _translate("MainWindow", "BUCKET SORT"))
        self.SortingComboBox.setItemText(8, _translate("MainWindow", "COMB SORT"))
        self.SortingComboBox.setItemText(9, _translate("MainWindow", "GENOME SORT"))
        self.SortingComboBox.setItemText(10, _translate("MainWindow", "OLD EVEN SORT"))
        self.SelectButton_2.setText(_translate("MainWindow", "Sort"))
        self.LoadButton_2.setText(_translate("MainWindow", "Import"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
