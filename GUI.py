from PyQt5 import QtGui
from PyQt5.QtSql import QSqlQueryModel, QSqlDatabase, QSqlRelationalDelegate
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox
import sys
from PyQt5 import QtWidgets
import MySQLdb as mdb
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import MySQLdb.cursors

mydb= MySQLdb.connect(host="localhost", user="root", passwd="basimehsan", db="cs_220")



class Window2(QMainWindow):
    def __init__(self):
       super().__init__()
       win = QWidget()
       self.title = "Court Case Database Management System1"
       self.top = 200
       self.left = 500
       self.width = 400
       self.height = 300
       # self.setWindowIcon(QtGui.QIcon("icon.png"))
       # self.setLayout(QVBoxLayout)
       self.setWindowTitle(self.title)
       self.setGeometry(self.left, self.top, self.width, self.height)

       layout = QVBoxLayout()

       """table_widget = MyTableWidget()

       layout.addWidget(table_widget)
       win.setLayout(layout)"""
       self.tabwidget = QTabWidget()
       win = self.tabwidget
       self.tab1 = QWidget()
       self.tab2 = QWidget()
       self.tab3 = QWidget()
       self.tab4 = QWidget()
       self.tab5 = QWidget()
       self.tab6 = QWidget()

       self.tab1.layouttab1 = QVBoxLayout(self)
       self.tableWidget = QTableWidget()

       # db = QSqlDatabase.addDatabase("QMYSQL")
       # db.setHostName("localhost")
       # db.setDatabaseName("cs_220")
       # db.setUserName("root")
       # db.setPassword("basimehsan")
       # ok = db.open()

       # self.model = QSqlQueryModel()
       #self.model.setTable("lawyer")
       #self.model.select()
       # self.model.setQuery("select * from cs_220.lawyer")
       # self.model.setHeaderData(0, Qt.Horizontal, "Lawyer Id")
       # self.model.setHeaderData(1, Qt.Horizontal, "First Name")
       # self.model.setHeaderData(2, Qt.Horizontal, "Last Name")
       # self.model.setHeaderData(3, Qt.Horizontal, "Specialization")
       # self.model.setHeaderData(4, Qt.Horizontal, "Years of Experience")
       # self.model.setHeaderData(5, Qt.Horizontal, "Phone")
       # self.model.setHeaderData(6, Qt.Horizontal, "Email")
       # self.view = QTableView()
       # self.view.setModel(self.model)
       # self.view.setItemDelegate(QSqlRelationalDelegate(self.view))
       #self.view.show()
       cur = mydb.cursor()
       cur.execute("SELECT * FROM lawyer")
       self.tableWidget.setRowCount(0)
       self.tableWidget.setColumnCount(7)
       self.tableWidget.setHorizontalHeaderLabels(['laywer_id','fname','lname','specialization','years_of_xp','phone','email'])
       result = cur.fetchall()
       for row, row_data in enumerate(result):
           self.tableWidget.insertRow(row)
           for col, col_data in enumerate(row_data):
               print(row,col, col_data)
               self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(col_data))


       self.tab1.layouttab1.addWidget(self.tableWidget)
       self.tab1.setLayout(self.tab1.layouttab1)

       self.tabwidget.addTab(self.tab1, "Lawyer")
       self.tabwidget.addTab(self.tab2, "Judge")
       self.tabwidget.addTab(self.tab3, "Plaintiff")
       self.tabwidget.addTab(self.tab4, "Defendant")
       self.tabwidget.addTab(self.tab5, "Court")
       self.tabwidget.addTab(self.tab6, "Case")
       #win.show()
       self.setCentralWidget(win)
       #self.show()


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        win = QWidget()
        self.title = "Court Case Database Management System"
        self.top = 100
        self.left = 100
        self.width = 600
        self.height = 500
        #self.setWindowIcon(QtGui.QIcon("icon.png"))
        #self.setLayout(QVBoxLayout)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        layout = QVBoxLayout()

        #self.InitWindow()
        #table_widget = MyTableWidget()
        pushButton = ConnectionButton()
        dbbutton= TablesButton()

        layout.addWidget(pushButton)
        layout.addWidget(dbbutton)
        win.setLayout(layout)
        self.setCentralWidget(win)
       # self.pushButton.clicked.connect(self.window2)
        self.main_window()

    def main_window(self):
            self.setWindowTitle(self.title)
            self.setGeometry(self.left, self.top, self.width, self.height)
            self.show()


class ConnectionButton(QPushButton):
    def __init__(self):
        super(QPushButton, self).__init__()
        self.button = QPushButton('Connect to Database', self)
        self.button.setGeometry(1, 1, 380, 23)
        self.button.clicked.connect(self.DBConnection)


    def DBConnection(self):
        try:
            db = mdb.connect('localhost', 'root', 'basimehsan', 'cs_220')
            QMessageBox.about(self, "Database Connection", 'Database Connected Successfully')

        except mdb.Error as e:
            QMessageBox.about(self, "Database Connection", 'Failed To Connect Database')
            sys.exit(1)


class TablesButton(QPushButton):
    def __init__(self):
        super(QPushButton, self).__init__()
        self.button = QPushButton('Open Database', self)
        self.button.clicked.connect(self.window2)

    def window2(self):
        self.w = Window2()
        self.w.show()
       # self.hide()


class MyTableWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.tabwidget = QTabWidget()
        wii= self.tabwidget
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()


        self.tab1.layouttab1 = QVBoxLayout(self)
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("Cell (4,2)"))
        self.tab1.layouttab1.addWidget(self.tableWidget)
        self.tab1.setLayout(self.tab1.layouttab1)

        self.tabwidget.addTab(self.tab1, "Lawyer")
        self.tabwidget.addTab(self.tab2, "Judge")
        self.tabwidget.addTab(self.tab3, "Party")
        self.tabwidget.addTab(self.tab4, "Court")
        self.tabwidget.addTab(self.tab5, "Case")
        wii.show()


qapp = QApplication(sys.argv)
app = App()
sys.exit(qapp.exec())
