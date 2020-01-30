from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
import MySQLdb as mdb


class Window(QDialog):
    def __init__(self):
        super().__init__()

        # Creating the main window
        self.title = "PyQt5 Inserting Data MySQL"
        self.top = 400
        self.left = 300
        self.width = 400
        self.height = 100

        self.initWindow()

    def initWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()  # Creating a Vertical Box Layout

        # Crating a LineEdit to contain the name information
        self.name = QLineEdit()
        self.name.setPlaceholderText("Enter your Name: ")
        self.name.setStyleSheet("background: lightblue")
        self.name.setFont(QtGui.QFont("Comic Sans MS", 15))
        vbox.addWidget(self.name) # Add to the Vertical Box

        # Crating a LineEdit to contain the email information
        self.email = QLineEdit()
        self.email.setPlaceholderText("Enter your email: ")
        self.email.setStyleSheet("background: lightblue")
        self.email.setFont(QtGui.QFont("Comic Sans MS", 15))
        vbox.addWidget(self.email)  # Add to the Vertical Box

        # Creating the buttons
        self.btnSave = QPushButton("Save Data")
        self.btnSave.clicked.connect(self.saveData)
        vbox.addWidget(self.btnSave)  # Add to the Vertical Box

        self.btnPrint = QPushButton("Print")
        self.btnPrint.clicked.connect(self.printTable)
        vbox.addWidget(self.btnPrint)  # Add to the Vertical Box

        self.btnDelete = QPushButton("Delete All")
        self.btnPrint.clicked.connect(self.deleteAll)
        vbox.addWidget(self.btnDelete)  # Add to the Vertical Box

        # Crating a LineEdit to contain the delete information
        self.delete = QLineEdit()
        self.delete.setPlaceholderText("Delete where name is: ")
        self.delete.setStyleSheet("background: lightblue")
        self.delete.setFont(QtGui.QFont("Comic Sans MS", 15))
        vbox.addWidget(self.delete)  # Add to the Vertical Box

        self.setLayout(vbox)  #Seting the layout page

        self.show()  # Displaying the Window

    def saveData(self):  # Method to save information
        #Make the change bellow to your own information.
        mydb = mdb.connect('type Host', 'type User', 'type Password', 'type DataBase')

        mycursor = mydb.cursor()  # Creating Cursor

        # Get the text from the LineEdit
        name = self.name.text()
        email = self.email.text()

        # Inserting the name in the table call *data* (change the name from the,
        # table for your table name).
        sql = ("INSERT INTO data"
               "(name, email)"
               "VALUES(%s, %s)")
        val = (name, email) # Values

        mycursor.execute(sql, val)

        QMessageBox.about(self, "Inserted", "Data Inserted Successfully")

        self.name.setText("")  # Made the lineEdit blank again
        self.email.setText("")  # Made the lineEdit blank again
        mydb.commit() # Obligatory line

    def printTable(self): # Define the action to print your table in to the console
        mydb = mdb.connect('type Host', 'type User', 'type Password', 'type DataBase')

        mycursorprint = mydb.cursor()
        mycursorprint.execute("SELECT * FROM data")

        myresult = mycursorprint.fetchall()

        for x in myresult:
            print(x)

    def deleteAll(self): # Method to delete information
        mydbdelete = mdb.connect('type Host', 'type User', 'type Password', 'type DataBase')

        mycursordelete = mydbdelete.cursor()

        delete = self.delete.text()

        sql = "DELETE FROM data WHERE name = %s"  # Delete Where the name is...
        val = (delete, )

        mycursordelete.execute(sql, val)

        self.delete.setText("")  # Made the lineEdit blank again
        mydbdelete.commit()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())