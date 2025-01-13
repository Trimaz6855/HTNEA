# Importing the external PyQt interface classes I have created.
from matplotlib.backend_tools import cursors

from Login import Ui_loginWindow
from registration import Ui_regWindow

# Importing python libraries.
from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QMessageBox, QDialog
from PyQt6.QtGui import QIcon, QWindow
import pyodbc

# Creates the database connection string.
conStr = (r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
          r"DBQ=..\programFiles.accdb;")

# Creates a global variable to keep track of which windows are open.
windows = []

# Creating the login page class.
class loginWindow(QMainWindow):# 
    # Login window constructor method.
    def __init__(self):
        # Accesses the parent classes constructor method.
        super().__init__()
        # Sets the user interface of the new class to be Ui_loginWindow.
        self.ui = Ui_loginWindow()
        # Sets up the ui.
        self.ui.setupUi(self)

        # Adds the external stylesheet.
        with open("../Stylesheets/mainStylesheet.css", "r") as f:
            style = f.read()
            self.setStyleSheet(style)

        # Sets up the password visibility toggle button.
        self.ui.btnLoginPVis.setIcon(QIcon("../Images/togglePassword.png"))
        self.ui.txtLoginPWord.setEchoMode(QLineEdit.EchoMode.Password)
        self.loginPVis = False
        self.ui.btnLoginPVis.clicked.connect(self.togglePVis)

        # Sets up login function.
        self.ui.btnLogin.clicked.connect(self.login)

        # Sets up the forgot password function.
        self.ui.btnFPword.clicked.connect(self.forgotPassword)

        # Sets up the function to open the registration page.
        self.ui.btnLoginRegister.clicked.connect(self.toReg)

    # Defines the password toggle function.
    def togglePVis(self):
        # Checks the value of loginPVis
        if self.loginPVis == True:
            # Toggles loginPVis.
            self.loginPVis = False
            # Makes the password invisible and the icon of the toggle button.
            self.ui.txtLoginPWord.setEchoMode(QLineEdit.EchoMode.Password)
            self.ui.btnLoginPVis.setIcon(QIcon("../Images/togglePassword.png"))
        elif self.loginPVis == False:
            # Toggles loginPVis
            self.loginPVis = True
            # Makes the password visible and changes the toggle button icon.
            self.ui.txtLoginPWord.setEchoMode(QLineEdit.EchoMode.Normal)
            self.ui.btnLoginPVis.setIcon(QIcon("../Images/togglePassword2.png"))

    # Defines the login function.
    def login(self):
        # Temporarily stores the username and password entered by the user.
        self.loginUname = self.ui.txtLoginUname.text().strip()
        self.loginPWord = self.ui.txtLoginPWord.text().strip()
        # Checks the input meets the required validation rules.
        if (0 < len(self.loginUname) <= 20) and (0 < len(self.loginPWord) <= 20):
            # Opens a connection to the database.
            self.conn = pyodbc.connect(conStr)
            # Creates a cursor to navigate the database.
            self.cursor = self.conn.cursor()
            # Searches the database for accounts with the username entered.
            self.cursor.execute(f"SELECT * FROM Accounts WHERE uname = '{self.loginUname}'")
            # Stores the retrieved account.
            self.account = self.cursor.fetchone()
            # Closes the database connection.
            self.conn.close()
            # Checks if an account exists with that username.
            if self.account:
                # Checks that the passwords match.
                if self.account[2] == self.loginPWord:
                    # Displays a welcome message to the user.
                    QMessageBox.information(self, "Login Success!", f"Welcome, {self.loginUname}")
                else:
                    # Displays an error message.
                    QMessageBox.critical(self, "Error", "Incorrect Password!")
            else:
                # Displays an error message to the user.
                QMessageBox.critical(self, "Error", "Invalid Username!")
        # Checks the username is not empty.
        elif len(self.loginUname) == 0:
            # Displays an error message.
            QMessageBox.critical(self, "Error", "Username is empty!")
        elif len(self.loginUname) > 20:
            # Displays an error message.
            QMessageBox.critical(self, "Error", "Username is too long!")
        elif len(self.loginPWord) == 0:
            # Displays an error message.
            QMessageBox.critical(self, "Error", "Password is empty!")
        elif len(self.loginPWord) > 20:
            # Displays an error message.
            QMessageBox.critical(self, "Error", "Password is too long!")

    # Defines the forgot password function.
    def forgotPassword(self):
        # Temporarily stores the entered username.
        self.loginUname = self.ui.txtLoginUname.text().strip()
        # Checks the username box is not empty.
        if len(self.loginUname) != 0:
            # Opens a connection to the database.
            self.conn = pyodbc.connect(conStr)
            # Creates a cursor to navigate through the database.
            self.cursor = self.conn.cursor()
            # Checks the database for an account with a username matching the one entered by the user and returns the users forgot password hint.
            self.cursor.execute(f"SELECT pwordHint FROM Accounts WHERE uname = '{self.loginUname}'")
            # Stores the forgot password hint.
            self.loginPwordHint = self.cursor.fetchone()
            # Closes the database connection.
            self.conn.close()
            # Displays the users forgot password hint to them if one was found.
            if self.loginPwordHint:
                # Displays the information popup with their hint.
                QMessageBox.information(self, "Forgot Password Hint", f"Your Forgot Password Hint is: {self.loginPwordHint[0]}")
            else:
                # Displays an error popup.
                QMessageBox.critical(self, "Error", "Invalid Username!")
        # Checks the username entered is not invalid.
        elif len(self.loginUname) > 20:
            # Displays an error popup.
            QMessageBox.critical(self, "Error", "Invalid Username!")
        else:
            # Asks the user to enter a username.
            QMessageBox.critical(self, "Error", "Please Enter a Username!")

    # Defines the to registration function.
    def toReg(self):
        self.hide()
        registration = regWindow()
        registration.show()
        windows.append(registration)

    # Overrides the close event to hide the window rather than closing it.
    def closeEvent(self, event):
        self.hide()

# Defines the registration window class.
class regWindow(QMainWindow):
    # Defines the constructor method.
    def __init__(self):
        # Accesses the parent class' constructor method.
        super().__init__()
        # Instantiates the window's ui as an instance of the Ui_regWindow class.
        self.ui = Ui_regWindow()
        # Sets up the ui.
        self.ui.setupUi(self)
        # Sets the stylesheet of the window.
        with open("../Stylesheets/mainStylesheet.css", "r") as f:
            style = f.read()
            self.setStyleSheet(style)
        # Sets up the login button.
        self.ui.btnRegLogin.clicked.connect(self.toLogin)

    # Defines the function that takes the user to the login page.
    def toLogin(self):
        self.hide()
        login.show()

    # Overrides the close event to hide the window rather than close it.
    def closeEvent(self, event):
        self.hide()

if __name__ == '__main__':
    app = QApplication([])
    login = loginWindow()
    login.show()
    app.exec()
