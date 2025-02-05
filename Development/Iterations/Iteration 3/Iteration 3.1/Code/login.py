# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(800, 600)
        loginWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.btnLoginPVis = QtWidgets.QPushButton(parent=loginWindow)
        self.btnLoginPVis.setGeometry(QtCore.QRect(473, 294, 32, 32))
        self.btnLoginPVis.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border-color: rgba(255, 255, 255, 0);\n"
"}")
        self.btnLoginPVis.setText("")
        self.btnLoginPVis.setCheckable(True)
        self.btnLoginPVis.setObjectName("btnLoginPVis")
        self.txtLoginPWord = QtWidgets.QLineEdit(parent=loginWindow)
        self.txtLoginPWord.setGeometry(QtCore.QRect(280, 290, 231, 31))
        self.txtLoginPWord.setStyleSheet("")
        self.txtLoginPWord.setText("")
        self.txtLoginPWord.setObjectName("txtLoginPWord")
        self.btnLoginCancel = QtWidgets.QPushButton(parent=loginWindow)
        self.btnLoginCancel.setGeometry(QtCore.QRect(310, 430, 161, 24))
        self.btnLoginCancel.setObjectName("btnLoginCancel")
        self.gVLogin = QtWidgets.QGraphicsView(parent=loginWindow)
        self.gVLogin.setGeometry(QtCore.QRect(170, 30, 450, 550))
        self.gVLogin.setMinimumSize(QtCore.QSize(450, 550))
        self.gVLogin.setMaximumSize(QtCore.QSize(450, 550))
        self.gVLogin.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.gVLogin.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.gVLogin.setObjectName("gVLogin")
        self.lblLogin = QtWidgets.QLabel(parent=loginWindow)
        self.lblLogin.setGeometry(QtCore.QRect(270, 60, 251, 171))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lblLogin.setFont(font)
        self.lblLogin.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblLogin.setObjectName("lblLogin")
        self.btnLoginRegister = QtWidgets.QPushButton(parent=loginWindow)
        self.btnLoginRegister.setGeometry(QtCore.QRect(310, 480, 161, 24))
        self.btnLoginRegister.setObjectName("btnLoginRegister")
        self.btnLoginFPword = QtWidgets.QPushButton(parent=loginWindow)
        self.btnLoginFPword.setGeometry(QtCore.QRect(340, 340, 111, 24))
        self.btnLoginFPword.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.btnLoginFPword.setObjectName("btnLoginFPword")
        self.txtLoginUname = QtWidgets.QLineEdit(parent=loginWindow)
        self.txtLoginUname.setGeometry(QtCore.QRect(280, 220, 231, 31))
        self.txtLoginUname.setStyleSheet("")
        self.txtLoginUname.setObjectName("txtLoginUname")
        self.btnLogin = QtWidgets.QPushButton(parent=loginWindow)
        self.btnLogin.setGeometry(QtCore.QRect(310, 380, 161, 24))
        self.btnLogin.setObjectName("btnLogin")
        self.gVLogin.raise_()
        self.txtLoginUname.raise_()
        self.btnLoginFPword.raise_()
        self.btnLoginRegister.raise_()
        self.txtLoginPWord.raise_()
        self.btnLoginCancel.raise_()
        self.btnLogin.raise_()
        self.lblLogin.raise_()
        self.btnLoginPVis.raise_()

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "Dialog"))
        self.txtLoginPWord.setPlaceholderText(_translate("loginWindow", "Enter Password:"))
        self.btnLoginCancel.setText(_translate("loginWindow", "Cancel"))
        self.lblLogin.setText(_translate("loginWindow", "Login"))
        self.btnLoginRegister.setText(_translate("loginWindow", "Register"))
        self.btnLoginFPword.setText(_translate("loginWindow", "Forgot Password?"))
        self.txtLoginUname.setPlaceholderText(_translate("loginWindow", "Enter Username:"))
        self.btnLogin.setText(_translate("loginWindow", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QDialog()
    ui = Ui_loginWindow()
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec())
