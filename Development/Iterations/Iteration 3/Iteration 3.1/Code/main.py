# Importing the external PyQt interface classes I have created.
from login import Ui_loginWindow
from registration import Ui_regWindow
from mainWindow import Ui_mainPage
from dataWindow import Ui_dataWindow
from catalogueWindow import Ui_catalogueWindow
from graphTransformation import Ui_graphTransformation
from functionWindow import Ui_functionWindow

# Importing PyQt for window functionality.
from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QMessageBox, QDialog, QFileDialog, QTableWidgetItem
from PyQt6.QtGui import QIcon, QWindow
from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex, QSortFilterProxyModel

# Importing pyodbc for database connection.
import pyodbc

# Importing regular expressions.
import re

# Importing matplotlib for graphing.
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as figureCanvas,  NavigationToolbar2QT as navBar
from matplotlib.figure import Figure
from matplotlib import use

# Importing sympy for graphing.
from sympy import plot_implicit, plot, Eq
from sympy.plotting import plot3d

# Importing numpy.
from numpy import polyfit, array, random

# Sets the matplotlib style to be used.
use("QtAgg")

# Creates the database connection string.
conStr = (r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
          r"DBQ=..\programFiles.accdb;")

# Stores the user's account.
currentAccount = []

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
        # Sets the window title.
        self.setWindowTitle("Login Page")

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
        loginUname = self.ui.txtLoginUname.text().strip()
        loginPWord = self.ui.txtLoginPWord.text().strip()
        # Checks the input meets the required validation rules.
        if (0 < len(loginUname) <= 20) and (0 < len(loginPWord) <= 20):
            # Opens a connection to the database.
            conn = pyodbc.connect(conStr)
            # Creates a cursor to navigate the database.
            cursor = conn.cursor()
            # Searches the database for accounts with the username entered.
            cursor.execute(f"SELECT * FROM Accounts WHERE uname = '{loginUname}'")
            # Stores the retrieved account.
            account = cursor.fetchone()
            # Closes the database connection.
            conn.close()
            # Checks if an account exists with that username.
            if account:
                # Checks that the passwords match.
                if account[2] == loginPWord:
                    # Displays a welcome message to the user.
                    QMessageBox.information(self, "Login Success!", f"Welcome, {loginUname}")
                    # Stores the users account.
                    account.append(account)
                    # Sends the user to the home page.
                    self.toHome()
                else:
                    # Displays an error message.
                    QMessageBox.critical(self, "Error", "Incorrect Password!")
            else:
                # Displays an error message to the user.
                QMessageBox.critical(self, "Error", "Invalid Username!")
        # Checks the username is not empty.
        elif len(loginUname) == 0:
            # Displays an error message.
            QMessageBox.critical(self, "Error", "Username is empty!")
        elif len(loginUname) > 20:
            # Displays an error message.
            QMessageBox.critical(self, "Error", "Username is too long!")
        elif len(loginPWord) == 0:
            # Displays an error message.
            QMessageBox.critical(self, "Error", "Password is empty!")
        elif len(loginPWord) > 20:
            # Displays an error message.
            QMessageBox.critical(self, "Error", "Password is too long!")

    # Defines the forgot password function.
    def forgotPassword(self):
        # Temporarily stores the entered username.
        loginUname = self.ui.txtLoginUname.text().strip()
        # Checks the username box is not empty.
        if len(loginUname) != 0:
            # Opens a connection to the database.
            conn = pyodbc.connect(conStr)
            # Creates a cursor to navigate through the database.
            cursor = conn.cursor()
            # Checks the database for an account with a username matching the one entered by the user and returns the users forgot password hint.
            cursor.execute(f"SELECT pwordHint FROM Accounts WHERE uname = '{loginUname}'")
            # Stores the forgot password hint.
            loginPwordHint = cursor.fetchone()
            # Closes the database connection.
            conn.close()
            # Displays the users forgot password hint to them if one was found.
            if loginPwordHint:
                # Displays the information popup with their hint.
                QMessageBox.information(self, "Forgot Password Hint", f"Your Forgot Password Hint is: {loginPwordHint[0]}")
            else:
                # Displays an error popup.
                QMessageBox.critical(self, "Error", "Invalid Username!")
        # Checks the username entered is not invalid.
        elif len(loginUname) > 20:
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
        #Sets the window title.
        self.setWindowTitle("Registration Page")

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
        regUname = self.ui.txtRegUname.text().strip()
        regPword = self.ui.txtRegPword.text().strip()
        regConPword = self.ui.txtRegConPword.text().strip()
        regPHint = self.ui.txtRegPHint.text()

        # Checks the password is not too long.
        if (len(regPword) > 20) or (len(regConPword) > 20):
            # Displays an error message.
            QMessageBox.critical(self, "Error", "Password is too long!")

        # Checks if the username is too long.
        elif (len(regUname) > 20):
            # Displays an error message.
            QMessageBox.critical(self, "Error", "Username is too long!")

        # Checks that none of the data fields are empty.
        elif (len(regUname) != 0) and (len(regPword) != 0) and (len(regConPword) != 0) and (len(regPHint) != 0):

            # Checks that the password fields match.
            if (regPword == regConPword):
                # Opens a connection with the database.
                conn = pyodbc.connect(conStr)
                # Creates a cursor to navigate the database.
                cursor = conn.cursor()
                # Attempts to find an account with the username the user has entered.
                cursor.execute(f"SELECT * FROM Accounts WHERE uname = '{regUname}'")
                # Attempts to store any accounts retrieved.
                results = cursor.fetchone()
                # Checks that there were no accounts retrieved.

                if not results:
                    # Searches the password to check it meets the required criteria.
                    # Searches for any lower case letters and temporarily stores them.
                    lower = re.findall(r"[a-z]", regPword)
                    # Searches for any upper case letters and temporarily stores them.
                    upper = re.findall(r"[A-Z]", regPword)
                    # Searches for any numbers and temporarily stores them.
                    num = re.findall(r"[0-9]", regPword)
                    # Searches for any special characters and temporarily stores them.
                    specialChar = re.findall(r"[\!\"\£\$\%\^\&\*\(\)\+\=\¬\`\|\:\;\@\#\~\,\.\<\>\/\?\{\}\[\]\'-]", regPword)

                    # Checks that the password contains at least 1 of each of the required characters.
                    if (len(lower) > 0) and (len(upper) > 0) and (len(num) > 0) and (len(specialChar) > 0):
                        # Inserts a new account record into the database.
                        cursor.execute(f"INSERT INTO Accounts (uname, pword, pwordHint) VALUES ('{regUname}', '{regPword}', '{regPHint}')")
                        # Commits the changes to the database.
                        conn.commit()
                        # Closes the database connection.
                        conn.close()
                        # Displays a success message.
                        QMessageBox.information(self, "Account Creation Success", "Account Created Successfully!")
                        # Closes the registration page.
                        self.close()
                        # Opens the login page.
                        self.toLogin()

                    # Checks if the password does not contain a lower case letter.
                    elif len(lower) == 0:
                        # Displays an error message.
                        QMessageBox.critical(self, "Error", "Password Must Contain at Least 1 Lower Case Letter!")

                    # Checks if the password does not contain an upper case letter.
                    elif len(upper) == 0:
                        # Displays an error message.
                        QMessageBox.critical(self, "Error", "Password Must Contain at Least 1 Upper Case Letter!")

                    # Checks if the password does not contain a number.
                    elif len(num) == 0:
                        # Displays an error message.
                        QMessageBox.critical(self, "Error", "Password Must Contain at Least 1 Number!")

                    # Checks if the password does not contain a special character.
                    elif len(specialChar) == 0:
                        # Displays an error message.
                        QMessageBox.critical(self, "Error", "Password Must Contain at Least 1 Special Character!")

                    else:
                        # Displays an error message.
                        QMessageBox.critical(self, "Error", "Password Must Contain at Least 1 Upper, 1 Lower Case Letter, 1 Number and 1 Special Character!")

                # If any were retrieved.
                else:
                    # Displays an error message.
                    QMessageBox.critical(self, "Error", "An account with that username already exists!")

            else:
                # Displays an error message.
                QMessageBox.critical(self, "Error", "Passwords do not match!")

        # Checks if the username is empty.
        elif (len(regUname) == 0):
            # Displays an error message.
            QMessageBox.critical(self, "Error", "Please Enter a Username!")

        # Checks if the password is empty.
        elif (len(regPword) == 0):
            # Displays an error message.
            QMessageBox.critical(self, "Error", "Please Enter a Password!")

        # Checks if the confirm password box is empty.
        elif (len(regConPword)) == 0:
            # Displays an error message.
            QMessageBox.critical(self, "Error", "Please Confirm your Password!")

        # Checks if the forgot password hint box is empty.
        elif (len(regPHint)) == 0:
            # Displays an error message.
            QMessageBox.critical(self, "Error", "Please Enter a Forgot Password Hint!")

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
        # Sets the window title.
        self.setWindowTitle("Home Page")

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

        # Sets up the data table button.
        self.ui.btnMainTable.clicked.connect(self.toDataTable)

        # Sets up the random data graph button.
        self.ui.btnMainRandom.clicked.connect(self.toRandomData)

        # Sets up the function catalogue button.
        self.ui.btnMainFunCat.clicked.connect(self.toFunCatalogue)

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

    # Defines a function to check if the user is logged in.
    def accountCheck(self):
        # Checks if the user is logged in.
        if currentAccount == []:
            # Makes the login button the visible button.
            self.ui.btnMainAccDrp.setHidden(True)
            self.ui.btnMainLogin.setHidden(False)
            self.ui.btnMainAccDrp.setText("Account v")
            self.mainLoggedIn = False
        else:
            # Makes the account text and dropdown the only visible parts.
            self.ui.btnMainLogin.setHidden(True)
            self.ui.btnMainAccDrp.setHidden(False)
            self.ui.btnMainAccDrp.setText(f"Hello, {currentAccount[0][1]} v")
            self.mainLoggedIn = True

    # Defines the account dropdown function.
    def accountDropdown(self):
        # Checks if the dropdown menu is not visible.
        if self.mainAccDrpdwn == False:
            # Makes the menu visible.
            self.mainAccDrpdwn = True
            self.ui.frameAcc.setVisible(True)
            self.ui.btnMainAccDrp.setText(f"Hello, {currentAccount[0][1]} ^")
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

    # Defines the logout function.
    def logout(self):
        # Clears the stored account.
        currentAccount.clear()
        # Calls the account check function to alter the main page.
        self.accountCheck()
        # Calls the account dropdown function to hide the account dropdown.
        self.accountDropdown()

    # Defines the function to take the user to the data table page.
    def toDataTable(self):
        # Hides the main window.
        self.hide()
        # Instantiates a new QDialog object.
        dialog = QDialog()
        # Instantiates a dataWindow object.
        data = dataWindow()
        # Opens the data table page.
        data.ui.sWDataWindow.setCurrentIndex(0)
        # Shows the dataWindow object.
        data.show()
        # Executes the dataWindow object.
        data.exec()

    # Defines the function to take the user to the random data graph page.
    def toRandomData(self):
        # Hides the main window.
        self.hide()
        # Instantiates a new QDialog object.
        dialog = QDialog()
        # Instantiates a new dataWindow object.
        data = dataWindow()
        # Opens the random data graphing page.
        data.ui.sWDataWindow.setCurrentIndex(2)
        # Sets the window title.
        data.setWindowTitle("Random Data Graphing")
        # Shows the dataWindow object.
        data.show()
        # Executes the dataWindow object.
        data.exec()

    # Defines the function to take the user to the function catalogue page.
    def toFunCatalogue(self):
        # Opens a connection to the database.
        conn = pyodbc.connect(conStr)
        # Creates a cursor to navigate through the database.
        cursor = conn.cursor()
        # Selects the records stored by the admin account in the 2D Algebraic Graphs table.
        cursor.execute("SELECT type, xTitle, xLb, xUb, yTitle, yLb, yUb, lEquation, rEquation FROM [2D Algebraic Graphs] WHERE uId=1")
        # Stores these records.
        twoDim = cursor.fetchall()
        # Selects the records stored by the admin account in the 3D Algebraic Graphs table.
        cursor.execute("SELECT type, xTitle, xLb, xUb, yTitle, yLb, yUb, rEquation FROM [3D Algebraic Graphs] WHERE uId=1")
        # Stores these results.
        threeDim = cursor.fetchall()
        # Selects the records stored by the admin account in the Implicit Graphs table.
        cursor.execute("SELECT type, xTitle, xLb, xUb, yTitle, yLb, yUb, lEquation, rEquation FROM [Implicit Graphs] WHERE uId=1")
        # Stores these results.
        implicit = cursor.fetchall()
        # Closes the connection to the database.
        conn.close()
        # Stores all the graphs inside the data list.
        data = twoDim + threeDim + implicit
        # Hides the main window.
        self.hide()
        # Instantiates a new QDialog object.
        dialog = QDialog()
        # Instantiates a new instance of the catalogueWindow class, passing in the function records retrieved from the database tables.
        catalogue = catalogueWindow(data)
        # Shows the catalogue window.
        catalogue.show()
        # Executes the catalogue window.
        catalogue.exec()

# Defines the data window class.
class dataWindow(QDialog):
    # Defines the constructor method of the data window class.
    def __init__(self):
        # Accesses the parent class' constructor method.
        super().__init__()
        # Sets the windows ui to be the dataWindow class' ui.
        self.ui = Ui_dataWindow()
        # Sets up the ui.
        self.ui.setupUi(self)
        # Sets the window title.
        self.setWindowTitle("Data Table")

        # Applies the stylesheet to the window.
        with open("../Stylesheets/mainStylesheet.css", "r") as f:
            style = f.read()
            self.setStyleSheet(style)

        ### Data Graph Viewer Setup.

        # Sets the current widget to be the graph viewer.
        self.ui.sWDataWindow.setCurrentIndex(1)

        # Creates the dataCanvas.
        self.ui.dataCanvas = graphCanvas(self, width=5, height=5, dpi=100)

        # Adds the canvas to the window.
        self.ui.lytDataWindowCanvas.addWidget(self.ui.dataCanvas)

        # Adds the toolbar to the graph.
        self.ui.navBarDataWindow = navBar(self.ui.dataCanvas, self)
        self.ui.lytDataWindowBar.addWidget(self.ui.navBarDataWindow)

        # Adds the stylesheet to the navigation bar.
        with open("../Stylesheets/navBarStylesheet.css", "r") as f:
            style = f.read()
            self.ui.frameDataWindowBar.setStyleSheet(style)

        ### Data Table Setup.

        # Sets up the home buttons.
        self.ui.btnTDataHome.clicked.connect(self.toHome)
        self.ui.btnDataWindowHome.clicked.connect(self.toHome)

        # Sets up the add row button.
        self.ui.btnTDataRow.clicked.connect(self.addRow)

        # Sets up the graph data button.
        self.ui.btnTDataGraph.clicked.connect(self.graphData)

        # Sets up the import CSV button.
        self.ui.btnTDataCSV.clicked.connect(self.importCSV)

        ### Random Data Graphing Setup ###

        # Sets up the home button.
        self.ui.btnRDataHome.clicked.connect(self.toHome)

        # Sets up the graph button.
        self.ui.btnRDataGraph.clicked.connect(self.randomGraph)

    # Defines the function to take the user to the home page
    def toHome(self):
        # Closes the window.
        self.close()
        # Opens the main window.
        mainPage.show()

    # Defines the function to add a new row to the table.
    def addRow(self):
        # Stores the number of rows in the table temporarily.
        index = self.ui.tblTDataPoints.rowCount()
        # Inserts a new row at the next available index, using the number of rows.
        self.ui.tblTDataPoints.insertRow(index)

    # Defines the graph data function.
    def graphData(self):
        # Defines a temporary counter variable to keep track of which item is being checked.
        i = 0
        # Defines the lists of x and y values.
        dataXValues = []
        dataYValues = []
        # Checks there is more than 1 row.
        if self.ui.tblTDataPoints.rowCount() == 1:
            # Outputs an error message.
            QMessageBox.critical(self, "Error", "Please enter more co-ordinate values.")
            return ValueError
        else:
            # Checks if the index is within the number of rows.
            while (i < self.ui.tblTDataPoints.rowCount()):
                # Attempts to temporarily store the current x and y values.
                try:
                    tempX = self.ui.tblTDataPoints.item(i, 0).text()
                    tempY = self.ui.tblTDataPoints.item(i, 1).text()
                # Handles an error if the fields are empty.
                except AttributeError:
                    # Outputs an error message.
                    QMessageBox.critical(self, "Error", "Please fill every data field!")
                    return AttributeError
                else:
                    # Checks if the x value entered is a number.
                    try:
                        tempX = float(tempX)
                    # Outputs an error message if not.
                    except ValueError:
                        QMessageBox.critical(self, "Error", "Please enter numerical co-ordinate values!")
                        return ValueError
                    else:
                        # Adds the value to the x value list.
                        dataXValues.append(tempX)

                    # Checks if the y value entered is a number.
                    try:
                        tempY = float(tempY)
                    # Outputs an error message if not.
                    except ValueError:
                        QMessageBox.critical(self, "Error", "Please enter numerical co-ordinate values!")
                        return ValueError
                    else:
                        # Adds the value to the y value list.
                        dataYValues.append(tempY)
                    # Increments the counter variable.
                    i += 1

            # Temporarily stores the table's headers.
            xHeader = self.ui.tblTDataPoints.Qt.HorizontalHeaderItem(0).text()
            yHeader = self.ui.tblTDataPoints.Qt.HorizontalHeaderItem(1).text()
            # Converts the x and y value lists into numpy arrays.
            dataXValues = array(dataXValues)
            dataYValues = array(dataYValues)
            # Calculates the gradient and y intercept of the line of best fit for the data.
            gradient, yInt = polyfit(dataXValues, dataYValues, 1)
            # Plots the data onto the data graph viewer's canvas.
            self.ui.dataCanvas.axes.scatter(dataXValues, dataYValues, marker="o")
            # Plots the line of best fit onto the graph viewer's canvas.
            self.ui.dataCanvas.axes.plot(dataXValues, (gradient * dataXValues) + yInt)
            # Sets the axis titles of the graph.
            self.ui.dataCanvas.axes.set_xlabel(xHeader)
            self.ui.dataCanvas.axes.set_ylabel(yHeader)
            # Changes the window to display the graph.
            self.ui.sWDataWindow.setCurrentIndex(1)
            # Sets the window title.
            self.setWindowTitle("Data Graph Viewer")

    # Defines the function to import a csv file.
    def importCSV(self):
        # Prompts the user to select a csv file from their computer and extracts the file path.
        dataCSVFile = QFileDialog.getOpenFileUrl(self, "Select CSV File", filter="CSV files (*.csv)")[0].toLocalFile()
        # Checks that the user has selected a csv file.
        if dataCSVFile:
            # Opens the csv file to read the data from it.
            with (open(dataCSVFile, "r") as f):
                # Defines a temporary line counter variable
                lineCount = 1
                # Loops through every line in the file
                for line in f:
                   # Removes any whitespace from the line and tries to split it into an x and a y value.
                    try:
                        tempX, tempY = line.strip().split(",")
                    # Outputs an error message if there are not exactly 2 values per line.
                    except ValueError:
                        QMessageBox.critical(self, "Error", "CSV file is not in the correct format, there must be exactly 2 values per line!")
                        # Used to exit out of the function.
                        return ValueError
                    else:
                        # Checks the values on the first line (should be header labels).
                        if lineCount == 1:
                            # Checks if the values read from the file are strings.
                            try:
                                # Checks that the values are not numerical as they must be the header labels.
                                tempX = float(tempX)
                                tempY = float(tempY)
                            # Handles the error raised if the values are not numerical.
                            except ValueError:
                                if type(tempX) == str and type(tempY) == str:
                                    # Sets the table headers to be the input strings.
                                    self.ui.tblTDataPoints.setQt.HorizontalHeaderLabels([tempX, tempY])
                                # Returns an error if they are not strings.
                                else:
                                    QMessageBox.critical(self, "Error", "Please enter header labels on the first line!")
                            else:
                                # Outputs an error message.
                                QMessageBox.critical(self, "Error", "Please enter valid header labels on the first line!")
                                return ValueError

                        else:
                            # Checks if the values are floats.
                            try:
                                tempX = float(tempX)
                                tempY = float(tempY)
                            # If they are not floats, an error message is returned.
                            except ValueError:
                                QMessageBox.critical(self, "Error", "Please enter numerical co-ordinate values!")
                                # Used to exit out of the function.
                                return ValueError
                            else:
                                # Adds a new row to the table if the 1 default row has been filled.
                                if lineCount > 2:
                                    self.addRow()

                                # Sets the items in the new row to be the x and y values from the csv file.
                                self.ui.tblTDataPoints.setItem((lineCount - 2), 0, QTableWidgetItem(str(tempX)))
                                self.ui.tblTDataPoints.setItem((lineCount - 2), 1, QTableWidgetItem(str(tempY)))

                    # Increments the line counter variable.
                    lineCount += 1
        else:
            # Returns an error if the file was not selected.
            QMessageBox.critical(self, "Error", "Please select a valid CSV file!")
            return FileNotFoundError

    # Defines the random graph function.
    def randomGraph(self):
        # Temporarily stores the number of data points the user would like to generate.
        dataPointsNum = self.ui.txtRDataNum.text()
        # Temporarily stores the lower and upper bounds for the user's x values.
        dataXLwr, dataXUpr = self.ui.txtRDataXLwr.text(), self.ui.txtRDataXUpr.text()
        # Temporarily stores the lower and upper bounds for the user's y values.
        dataYLwr, dataYUpr = self.ui.txtRDataYLwr.text(), self.ui.txtRDataYUpr.text()
        # Checks that the number of data points is an integer.
        try:
            dataPointsNum = int(dataPointsNum)
        except ValueError:
            # Outputs an error message if the number of data points is not an integer.
            QMessageBox.critical(self, "Error", "Please enter an integer number of data points to generate!")
            return ValueError
        else:
            # Checks that the number of data points is positive.
            if dataPointsNum <= 0:
                # Outputs an error message if the number of data points is not positive
                QMessageBox.critical(self, "Error", "Please enter a valid number of data points to generate!")
                return ValueError
            # Checks that the upper and lower bounds are all integers.
            try:
                dataXLwr = int(dataXLwr)
                dataXUpr = int(dataXUpr)
                dataYLwr = int(dataYLwr)
                dataYUpr = int(dataYUpr)
            except ValueError:
                # Outputs an error if they are not integers.
                QMessageBox.critical(self, "Error", "Please ensure your upper and lower bounds are integers!")
                return ValueError
            else:
                # Checks if the x lower bound is greater than the x upper bound.
                if dataXLwr > dataXUpr:
                    # Outputs an error message.
                    QMessageBox.critical(self, "Error", "Please ensure the x upper bound is greater than the x lower bound!")
                    return ValueError
                # Checks that the x upper bound does not equal the x lower bound.
                elif dataXLwr == dataXUpr:
                    # Outputs an error message.
                    QMessageBox.critical(self, "Error", "Please ensure your x upper and lower bounds are not equal!")
                    return ValueError
                # Checks if the y lower bound is greater than the y upper bound.
                if dataYLwr > dataYUpr:
                    # Outputs an error message.
                    QMessageBox.critical(self, "Error", "Please ensure the y upper bound is greater than the y lower bound!")
                    return ValueError
                # Checks that the y upper bound does not equal the y lower bound.
                elif dataYLwr == dataYUpr:
                    # Outputs an error message.
                    QMessageBox.critical(self, "Error", "Please ensure the y upper and lower bounds are not equal!")
                    return ValueError

                # Generates the random x values.
                dataXValues = random.randint(dataXLwr, dataXUpr, size=(dataPointsNum))
                # Generates the random y values.
                dataYValues = random.randint(dataYLwr, dataYUpr, size=(dataPointsNum))
                # Calculates the gradient and y-intecept of the line of best fit for the data.
                gradient, yInt = polyfit(dataXValues, dataYValues, 1)
                # Plots the data points on the graph canvas.
                self.ui.dataCanvas.axes.scatter(dataXValues, dataYValues, marker="o")
                # Plots the line of best fit on the graph canvas.
                self.ui.dataCanvas.axes.plot(dataXValues, (gradient * dataXValues) + yInt)
                # Changes the window to display the graph.
                self.ui.sWDataWindow.setCurrentIndex(1)
                # Sets the window title.
                self.setWindowTitle("Data Graph Viewer")

# Defines the graph canvas class.
class graphCanvas(figureCanvas):
    # Defines the constructor method.
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        # Adds the figure to the canvas.
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        # Adds the axes to the figure.
        self.axes = self.fig.add_subplot(111)
        # Accesses the figure class' constructor method.
        super().__init__(self.fig)

# Defines the function catalogue window class.
class catalogueWindow(QDialog):
    # Defines the constructor method.
    def __init__(self, data):
        # Accesses the QDialog class' constructor method.
        super().__init__()
        # Makes the ui of the window an instance of Ui_catalogueWindow.
        self.ui = Ui_catalogueWindow()
        # Sets up the ui.
        self.ui.setupUi(self)
        # Sets the window title.
        self.setWindowTitle("Catalogue Viewer")
        # Stores the data as an attribute.
        self.data = data
        # Instantiates a new instance of catalogueTableModel.
        self.dataModel = catalogueTableModel(self.data)
        # Instantiates a proxy model, allowing the table to be sorted.
        self.proxyModel = QSortFilterProxyModel()
        # Sets the source of the proxy model to be the data model.
        self.proxyModel.setSourceModel(self.dataModel)
        # Makes the sorting case insensitive.
        self.proxyModel.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        # Applies the sorting to the left hand side of the equation.
        self.proxyModel.setFilterKeyColumn(6)
        # Makes it so every time the text in the search bar is changed, the table is sorted.
        self.ui.txtCatSearch.textChanged.connect(self.proxyModel.setFilterRegularExpression)
        # Sets the tables data model.
        self.ui.tblCatFunctions.setModel(self.proxyModel)

        # Applies the stylesheet to the window.
        with open("../Stylesheets/mainStylesheet.css", "r") as f:
            style = f.read()
            self.setStyleSheet(style)

        # Sets up the home button.
        self.ui.btnCatHome.clicked.connect(self.toHome)

        # Sets up the graph button.
        self.ui.btnCatGraph.clicked.connect(self.graph)

    # Defines the function to take the user to the home page.
    def toHome(self):
        # Closes the window.
        self.close()
        # Shows the main window.
        mainPage.show()

    # Defines the graph function.
    def graph(self):
        # Checks that the user has selected a row when the button is clicked.
        selectedRow = self.ui.tblCatFunctions.currentIndex().row()
        # Checks if the user has not selected a row.
        if selectedRow == -1:
            # Outputs an error message to the user.
            QMessageBox.critical(self, "Error", "Please select a function to graph!")
            return IndexError
        # Runs if the user has selected a row.
        else:
            # Loops through the data in the row to temporarily store the function, its range, its domain and its axis titles and the graph type.
            funcToGraph = []
            column = 0
            while column <= 8:
                funcToGraph.append(self.proxyModel.index(selectedRow, column).data())
                column += 1
            # Closes the current window.
            self.close()
            # Instantiates a new QDialog object.
            dialog = QDialog()
            # Instantiates a new instance of the graphTranslation clas.
            graphTWindow = transformWindow(funcToGraph)
            # Shows the new window.
            graphTWindow.show()
            # Executes the window.
            graphTWindow.exec()
            print(funcToGraph)

# Defines the function catalogue table model.
class catalogueTableModel(QAbstractTableModel):
    # Defines the constructor method.
    def __init__(self, data):
        # Accesses the QAbstractTableModel constructor method.
        super().__init__()
        # Stores the input data as a local variable in the class.
        self.data = data

    # Defines a function to determine the number of rows needed.
    def rowCount(self, parent=QModelIndex()):
        # Tries to return the number of 1D arrays inside the 2D array of functions.
        try:
            return len(self.data)
        # Returns 0 as the base case
        except ValueError:
            return 0

    # Defines a function to determine the number of columns needed.
    def columnCount(self, parent=QModelIndex()):
        # Tries to return the maximum number of items inside a 1D array inside the 2D array of functions.
        try:
            return len(max(self.data, key=len))
        # Returns 0 as the base case.
        except ValueError:
            return 0

    # Defines a function to display the data in the table.
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        # Only returns data for this specific role.
        if role == Qt.ItemDataRole.DisplayRole:
            # Tries to return the corresponding piece of data for that row and column.
            try:
                return self.data[index.row()][index.column()]
            # Returns a - if there is no available data.
            except IndexError:
                return "-"

    # Defines a function to give headers to the columns in the table.
    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        # Creates a tuple with the header names.
        columnNames = ("Graph Type", "X Title", "X Lower Bound", "X Upper Bound", "Y Title", "Y Lower Bound", "Y Upper Bound", "Left Equation", "Right Equation")
        # Checks that a header is a column header and that its role is DisplayRole.
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            # Adds the column names.
            return '{}'.format(columnNames[section])
        elif orientation == Qt.Orientation.Vertical and role == Qt.ItemDataRole.DisplayRole:
            # Numbers the rows.
            return '{}'.format(section + 1)

# Defines the graph translation window class.
class transformWindow(QDialog):
    # Defines the constructor method.
    def __init__(self, funcToGraph):
        # Accesses the QDialog class' constructor method.
        super().__init__()
        # Sets the ui of the window to be an instance of the Ui_graphTransformation class.
        self.ui = Ui_graphTransformation()
        # Sets up the ui.
        self.ui.setupUi(self)
        # Sets the window title.
        self.setWindowTitle("Enter Graph Transformations")
        # Applies the stylesheet to the window.
        with open("../Stylesheets/mainStylesheet.css", "r") as f:
            style = f.read()
            self.setStyleSheet(style)

        # Stores the function to graph as an attribute of the class.
        self.funcToGraph = funcToGraph

        # Sets up the graph button.
        self.ui.btnGTGraph.clicked.connect(self.graphClicked)

    def graphClicked(self):
        print("Clicked")
        # Temporarily stores the values in the text fields.
        xSF = self.ui.txtGTXSF.text()
        ySF = self.ui.txtGTYSF.text()
        xTr = self.ui.txtGTXVector.text()
        yTr = self.ui.txtGTYVector.text()
        print(xSF, type(xSF))
        # Checks if an x scale factor has been entered.
        if xSF == "":
            # If none has been entered, it defaults to 1.
            xSF = 1
        # Checks if a y scale factor has been entered.
        if ySF == "":
            # If none has been entered, it defaults to 1.
            ySF = 1
        # Checks if an x translation has been entered.
        if xTr == "":
            # If not, it defaults to 0.
            xTr = 0
        # Checks if a y translation has been entered.
        if yTr == "":
            # If not, it defaults to 0.
            yTr = 0
        # Checks the provided transformations are numbers.
        try:
            xSF = float(xSF)
            ySF = float(ySF)
            xTr = float(xTr)
            yTr = float(yTr)
        # If the transformations are not numbers, output an error message
        except ValueError:
            QMessageBox.critical(self, "Error", "Please enter numerical transformations!")
            return ValueError
        else:
            # Temporarily stores the type of function the function is.
            functionType = self.funcToGraph[0]
            # Checks what type of function it is and runs a section of code based on that.
            match functionType:
                # Runs if the function is a 3D function.
                case "3D":
                    # Applies the input transformations to x.
                    self.funcToGraph[7] = self.funcToGraph[7].replace("x", f"({xSF}*(x-{xTr}))")
                    # Applies the input transformations to x.
                    self.funcToGraph[7] = self.funcToGraph[7].replace("y", f"({ySF}*(y+{yTr}))")
                    # Closes the current window.
                    self.close()
                    # Closes the function catalogue window.
                    #catalogueWindow.close()
                    # Instantiates a new QDialog object.
                    dialog = QDialog()
                    # Instantiates a new object of the functionWindow class.
                    func = functionWindow()
                    # Shows the window.
                    func.show()
                    # Calls the 3D graph plotting function.
                    func.threeDimPlot(self.funcToGraph)
                    # Executes the window.
                    func.exec()

                # Runs if the function is a 2D function.
                case "2D":
                    # Applies the input transformations to y.
                    self.funcToGraph[7] = self.funcToGraph[7].replace("y", f"({ySF}*(y+{yTr}))")
                    # Applies the input transformations to x.
                    self.funcToGraph[8] = self.funcToGraph[8].replace("x", f"({xSF}*(x+{xTr}))")
                # Runs if the function is implicit.
                case "Implicit":
                    # Applies the input transformations to y.
                    self.funcToGraph[7] = self.funcToGraph[7].replace("y", f"({xSF}*({xTr}))")
                    # Applies the input transformations to x.
                    self.funcToGraph[8] = self.funcToGraph[8].replace("x", f"({xSF}*(x+{xTr}))")

# Defines the function window class.
class functionWindow(QDialog):
    # Defines the constructor method.
    def __init__(self):
        # Accesses the QDialog class' constructor method.
        super().__init__()
        # Makes the ui of the window an object of the Ui_functionWindow class.
        self.ui = Ui_functionWindow()
        # Sets up the ui.
        self.ui.setupUi(self)
        # Applies the stylesheet to the ui.
        with open("../Stylesheets/mainStylesheet.css", "r") as f:
            style = f.read()
            self.setStyleSheet(style)

        # Instantiates the canvas widget.
        self.ui.funcCanvas = graphCanvas(self, width=5, height=5, dpi=100)
        # Adds the canvas widget to the window.
        self.ui.lytFuncWindowCanvas.addWidget(self.ui.funcCanvas)
        # Instantiates the toolbar widget.
        self.ui.funcNavBar = navBar(self.ui.funcCanvas, self)
        # Adds the toolbar widget to the window.
        self.ui.lytfuncWindowBar.addWidget(self.ui.funcNavBar)
        # Applies the stylesheet to the toolbar in the window.
        with open("../Stylesheets/navBarStylesheet.css", "r") as f:
            style = f.read()
            self.ui.funcNavBar.setStyleSheet(style)

    # Defines the function to plot 3d graphs.
    def threeDimPlot(self, funcToGraph):
        print(funcToGraph)

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


