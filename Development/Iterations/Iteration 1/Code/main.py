#Importing the external PyQt interface classes I have created.
from matplotlib.backend_tools import cursors

from Login import Ui_loginWindow

#Importing python libraries.
from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QMessageBox
from PyQt6.QtGui import QIcon
import pyodbc

#Creates the database connection string.
conStr = (r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
          r"DBQ=..\programFiles.accdb;")

#Creating the login page class.
class loginWindow(QMainWindow):#
    #Login window constructor method.
    def __init__(self):
        #Accesses the parent classes constructor method.
        super().__init__()
        #Sets the user interface of the new class to be Ui_loginWindow.
        self.ui = Ui_loginWindow()
        #Sets up the ui.
        self.ui.setupUi(self)

        #Adds the external stylesheet.
        with open("../Stylesheets/mainStylesheet.css", "r") as f:
            style = f.read()
            self.setStyleSheet(style)

        #Sets up the password visibility toggle button.
        self.ui.btnLoginPVis.setIcon(QIcon("../Images/togglePassword.png"))
        self.ui.txtLoginPWord.setEchoMode(QLineEdit.EchoMode.Password)
        self.loginPVis = False
        self.ui.btnLoginPVis.clicked.connect(self.togglePVis)

        #Sets up login function.
        self.ui.btnLogin.clicked.connect(self.login)

        #Sets up the forgot password function.
        self.ui.btnFPword.clicked.connect(self.forgotPassword)

    #Defines the password toggle function.
    def togglePVis(self):
        #Checks the value of loginPVis
        if self.loginPVis == True:
            #Toggles loginPVis.
            self.loginPVis = False
            #Makes the password invisible and the icon of the toggle button.
            self.ui.txtLoginPWord.setEchoMode(QLineEdit.EchoMode.Password)
            self.ui.btnLoginPVis.setIcon(QIcon("../Images/togglePassword.png"))
        elif self.loginPVis == False:
            #Toggles loginPVis
            self.loginPVis = True
            #Makes the password visible and changes the toggle button icon.
            self.ui.txtLoginPWord.setEchoMode(QLineEdit.EchoMode.Normal)
            self.ui.btnLoginPVis.setIcon(QIcon("../Images/togglePassword2.png"))

    #Defines the login function.
    def login(self):
        #Opens a connection to the database.
        self.conn = pyodbc.connect(conStr)
        #Creates a cursor to navigate the database.
        self.cursor = self.conn.cursor()
        #Temporarily stores the username and password entered by the user.
        self.loginUname = self.ui.txtLoginUname.text()
        self.loginPWord = self.ui.txtLoginPWord.text()
        #Checks the input meets the required validation rules.
        if (len(self.loginUname) > 0 and len(self.loginUname) <= 20) and (len(self.loginPWord) > 0 and len(self.loginPWord) <= 20):
            #Searches the database for accounts with the username entered.
            self.cursor.execute(f"SELECT * FROM Accounts WHERE uname = '{self.loginUname}'")
            #Stores the retrieved account.
            self.account = self.cursor.fetchone()
            #Closes the database connection.
            self.conn.close()
            #Checks if an account exists with that username.
            if self.account:
                #Checks that the passwords match.
                if self.account[2] == self.loginPWord:
                    #Displays a welcome message to the user.
                    QMessageBox.information(self, "Login Success!", f"Welcome, {self.loginUname}")
                else:
                    #Displays an error message.
                    QMessageBox.critical(self, "Error", "Incorrect Password!")
            else:
                #Displays an error message to the user.
                QMessageBox.critical(self, "Error", "Incorrect Username!")
        elif len(self.loginUname) == 0:
            #Displays an error message.
            QMessageBox.critical(self, "Error", "Username is empty!")
        elif len(self.loginUname) > 20:
            #Displays an error message.
            QMessageBox.critical(self, "Error", "Username is too long!")
        elif len(self.loginPWord) == 0:
            #Displays an error message.
            QMessageBox.critical(self, "Error", "Password is empty!")
        elif len(self.loginPWord) > 20:
            #Displays an error message.
            QMessageBox.critical(self, "Error", "Password is too long!")

    #Defines the forgot password function.
    def forgotPassword(self):
        pass




if __name__ == '__main__':
    app = QApplication([])
    window = loginWindow()
    window.show()
    app.exec()
