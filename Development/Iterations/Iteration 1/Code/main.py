# Importing the external PyQt interface classes I have created.
import sys

from PyQt5.QtCore import Qt
from matplotlib.backend_tools import cursors

from login import Ui_loginWindow
from registration import Ui_regWindow
from mainWindow import Ui_mainPage

# Importing python libraries.
from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QMessageBox, QDialog
from PyQt6.QtGui import QIcon, QWindow
from PyQt6.QtCore import Qt
import pyodbc
import re

# Creates the database connection string.
conStr = (r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
          r"DBQ=..\programFiles.accdb;")

# Stores the user's account.
account = []

# Creating the login page class.
class loginWindow(QDialog):#
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
        self.ui.btnLoginFPword.clicked.connect(self.forgotPassword)

        # Sets up the function to open the registration page.
        self.ui.btnLoginRegister.clicked.connect(self.toReg)

        # Sets up the cancel button.
        self.ui.btnLoginCancel.clicked.connect(self.toHome)

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
                    # Stores the users account.
                    account.append(self.account)
                    # Sends the user to the home page.
                    self.toHome()
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

    # Defines the function to open the registration page.
    def toReg(self):
        # Closes the login window.
        self.close()
        # Instantiates a new dialog object.
        dialog = QDialog()
        # Instantiates a new registration window.
        reg = regWindow()
        # Shows the registration window.
        reg.show()
        # Executes the registration window.
        reg.exec()

    # Defines the function to open the home page.
    def toHome(self):
        # Closes the login page.
        self.close()
        # Shows the main window.
        mainPage.show()

# Defines the registration window class.
class regWindow(QDialog):
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

        # Sets up the register button.
        self.ui.btnRegister.clicked.connect(self.register)

        # Sets up the cancel button.
        self.ui.btnRegCancel.clicked.connect(self.toHome)

        # Sets up the password toggle functionality.
        self.ui.btnRegPVis.clicked.connect(self.togglePassword)

        # Initialises the password visibility variable.
        self.regPVis = False

        # Sets the default visibility of the passwords.
        self.ui.txtRegPword.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.txtRegConPword.setEchoMode(QLineEdit.EchoMode.Password)

        # Sets the icon of the password visibility button.
        self.ui.btnRegPVis.setIcon(QIcon("../Images/togglePassword.png"))

    # Defines the toggle password function.
    def togglePassword(self):
        # Checks if the passwords are visible.
        if self.regPVis == True:
            # Toggles the password visibility variable.
            self.regPVis = False
            # Changes the icon of the password visibility button.
            self.ui.btnRegPVis.setIcon(QIcon("../Images/togglePassword.png"))
            # Hides the passwords.
            self.ui.txtRegPword.setEchoMode(QLineEdit.EchoMode.Password)
            self.ui.txtRegConPword.setEchoMode(QLineEdit.EchoMode.Password)
        else:
            # Toggles the password visibility variable.
            self.regPVis = True
            # Changes the icon of the password visibility button.
            self.ui.btnRegPVis.setIcon(QIcon("../Images/togglePassword2.png"))
            # Hides the passwords.
            self.ui.txtRegPword.setEchoMode(QLineEdit.EchoMode.Normal)
            self.ui.txtRegConPword.setEchoMode(QLineEdit.EchoMode.Normal)

    # Defines the function that takes the user to the login page.
    def toLogin(self):
        # Closes the registration window.
        self.close()
        # Instantiates a new dialog object.
        dialog = QDialog()
        # Instantiates a new loginWindow object.
        login = loginWindow()
        # Shows the login window.
        login.show()
        # Executes the login window.
        login.exec()

    # Defines the register function.
    def register(self):
        # Temporarily stores the data entered by the user.
        self.regUname = self.ui.txtRegUname.text().strip()
        self.regPword = self.ui.txtRegPword.text().strip()
        self.regConPword = self.ui.txtRegConPword.text().strip()
        self.regPHint = self.ui.txtRegPHint.text()

        # Checks that none of the data fields are empty.
        if (len(self.regUname) != 0) and (len(self.regPword) != 0) and (len(self.regConPword) != 0) and (len(self.regPHint) != 0):

            # Checks that the password fields match.
            if (self.regPword == self.regConPword):
                # Opens a connection with the database.
                self.conn = pyodbc.connect(conStr)
                # Creates a cursor to navigate the database.
                self.cursor = self.conn.cursor()
                # Attempts to find an account with the username the user has entered.
                self.cursor.execute(f"SELECT * FROM Accounts WHERE uname = '{self.regUname}'")
                # Attempts to store any accounts retrieved.
                self.results = self.cursor.fetchone()
                # Checks that there were no accounts retrieved.

                if not self.results:
                    # Searches the password to check it meets the required criteria.
                    # Searches for any lower case letters and temporarily stores them.
                    self.lower = re.findall(r"[a-z]", self.regPword)
                    # Searches for any upper case letters and temporarily stores them.
                    self.upper = re.findall(r"[A-Z]", self.regPword)
                    # Searches for any numbers and temporarily stores them.
                    self.num = re.findall(r"[0-9]", self.regPword)
                    # Searches for any special characters and temporarily stores them.
                    self.specialChar = re.findall(r"[\!\"\£\$\%\^\&\*\(\)\+\=\¬\`\|\:\;\@\#\~\,\.\<\>\/\?\{\}\[\]\'-]", self.regPword)

                    # Checks that the password contains at least 1 of each of the required characters.
                    if (len(self.lower) > 0) and (len(self.upper) > 0) and (len(self.num) > 0) and (len(self.specialChar) > 0):
                        # Inserts a new account record into the database.
                        self.cursor.execute(f"INSERT INTO Accounts (uname, pword, pwordHint) VALUES ('{self.regUname}', '{self.regPword}', '{self.regPHint}')")
                        # Commits the changes to the database.
                        self.conn.commit()
                        # Closes the database connection.
                        self.conn.close()
                        # Displays a success message.
                        QMessageBox.information(self, "Account Creation Success", "Account Created Successfully!")
                        # Closes the registration page.
                        self.close()
                        # Opens the login page.
                        self.toLogin()

                    else:
                        # Displays an error message.
                        QMessageBox.critical(self, "Error", "Password Must Contain at Least 1 Upper, 1 Lower Case Letter, 1 Number and 1 Special Character.")

                # If any were retrieved.
                else:
                    # Displays an error message.
                    QMessageBox.critical(self, "Error", "An account with that username already exists!")

            else:
                # Displays an error message.
                QMessageBox.critical(self, "Error", "Passwords do not match!")

        # Checks if the username is empty.
        elif (len(self.regUname) == 0):
            # Displays an error message.
            QMessageBox.critical(self, "Error", "Please Enter a Username!")

        # Checks if the password is empty.
        elif (len(self.regPword) == 0):
            # Displays an error message.
            QMessageBox.critical(self, "Error", "Please Enter a Password!")

        # Checks if the confirm password box is empty.
        elif (len(self.regConPword)) == 0:
            # Displays an error message.
            QMessageBox.critical(self, "Error", "Please Confirm your Password!")

        # Checks if the forgot password hint box is empty.
        elif (len(self.regPHint)) == 0:
            # Displays an error message.
            QMessageBox.critical(self, "Error", "Please Enter a Forgot Password Hint!")

        # Checks if the username is too long.
        elif (len(self.regUname) > 20):
            # Displays an error message.
            QMessageBox.critical(self, "Error", "Username is too long!")

        # Checks the password is not too long.
        elif (len(self.regPword) > 20) or (len(self.regConPword) > 20):
            # Displays an error message.
            QMessageBox.critical(self, "Error", "Password is too long!")

    # Defines the function to open the home page.
    def toHome(self):
        # Closes the login page.
        self.close()
        # Shows the main window.
        mainPage.show()

# Defines the main menu class.
class mainPage(QMainWindow):
    # Defines the constructor method.
    def __init__(self):
        # Accesses the parent class constructor method.
        super().__init__()
        # Instantiates the window's ui as an instance of the Ui_mainPage class.
        self.ui = Ui_mainPage()
        # Sets up the ui.
        self.ui.setupUi(self)

        # Sets up the login button.
        self.ui.btnMainLogin.clicked.connect(self.toLogin)

        # Adds the stylesheet.
        with open("../Stylesheets/mainPageStylesheet.css", "r") as f:
            style = f.read()
            self.setStyleSheet(style)

        # Aligns the text inside the labels.
        self.ui.lblMainFunc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui.lblMainData.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Hides the dropdown buttons.
        self.ui.frameAcc.setVisible(False)
        self.ui.frameSci.setVisible(False)

        # Sets up the dropdown menu toggle buttons.
        self.ui.btnMainSciDrp.clicked.connect(self.sciFuncDropdown)
        self.ui.btnMainAccDrp.clicked.connect(self.accountDropdown)

        # Sets up the logout button.
        self.ui.btnMainLogout.clicked.connect(self.logout)

        # Creates the dropdown flag variables.
        self.mainSciDrpdwn = False
        self.mainAccDrpdwn = False

    # Defines the function that takes the user to the login page.
    def toLogin(self):
        # Hides the main menu.
        self.hide()
        # Instantiates a new dialog object.
        dialog = QDialog()
        # Instantiates a new loginWindow object.
        login = loginWindow()
        # Shows the login window.
        login.show()
        # Executes the login window.
        login.exec()

    # Defines a new show event function.
    def showEvent(self, a0):
        # Checks if the user is logged in.
        self.accountCheck()
        print(account)

    # Defines a function to check if the user is logged in.
    def accountCheck(self):
        # Checks if the user is logged in.
        if account == []:
            # Makes the login button the visible button.
            self.ui.btnMainAccDrp.setHidden(True)
            self.ui.btnMainLogin.setHidden(False)
            self.ui.btnMainAccDrp.setText("Account v")
            self.mainLoggedIn = False
        else:
            # Makes the account text and dropdown the only visible parts.
            self.ui.btnMainLogin.setHidden(True)
            self.ui.btnMainAccDrp.setHidden(False)
            self.ui.btnMainAccDrp.setText(f"Hello, {account[0][1]} v")
            self.mainLoggedIn = True

    # Defines the account dropdown function.
    def accountDropdown(self):
        # Checks if the dropdown menu is not visible.
        if self.mainAccDrpdwn == False:
            # Makes the menu visible.
            self.mainAccDrpdwn = True
            self.ui.frameAcc.setVisible(True)
            self.ui.btnMainAccDrp.setText(f"Hello, {account[0][1]} ^")
            # Checks if the menu is not visible.
        elif self.mainAccDrpdwn == True:
            # Hides the menu.
            self.mainAccDrpdwn = False
            self.ui.frameAcc.setVisible(False)
            self.ui.btnMainAccDrp.setText(f"Account v")

    # Defines the scientific functions dropdown function.
    def sciFuncDropdown(self):
        # Checks if the dropdown menu is not visible.
        if self.mainSciDrpdwn == False:
            # Makes the menu visible.
            self.mainSciDrpdwn = True
            self.ui.frameSci.setVisible(True)
            self.ui.btnMainSciDrp.setText("Scientific Functions ^")
        # Checks if the dropdown menu is visible.
        elif self.mainSciDrpdwn == True:
            # Hides the menu.
            self.mainSciDrpdwn = False
            self.ui.frameSci.setVisible(False)
            self.ui.btnMainSciDrp.setText("Scientific Functions v")

    #Defines the logout function.
    def logout(self):
        # Clears the stored account.
        account.clear()
        # Calls the account check function to alter the main page.
        self.accountCheck()
        # Calls the account dropdown function to hide the account dropdown.
        self.accountDropdown()

# Runs the program if the file ran is the main file.
if __name__ == "__main__":
    # Instantiates the application.
    app = QApplication([])
    # Instantiates a new loginWindow instance.
    mainPage = mainPage()
    # Shows the login window.
    mainPage.show()
    # Executes the application.
    app.exec()
