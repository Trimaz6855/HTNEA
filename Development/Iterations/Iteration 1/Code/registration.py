# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_regWindow(object):
    def setupUi(self, regWindow):
        regWindow.setObjectName("regWindow")
        regWindow.resize(800, 600)
        self.lblRegTitle = QtWidgets.QLabel(parent=regWindow)
        self.lblRegTitle.setGeometry(QtCore.QRect(300, 70, 191, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.lblRegTitle.setFont(font)
        self.lblRegTitle.setObjectName("lblRegTitle")
        self.txtRegConPword = QtWidgets.QLineEdit(parent=regWindow)
        self.txtRegConPword.setGeometry(QtCore.QRect(280, 280, 231, 31))
        self.txtRegConPword.setObjectName("txtRegConPword")
        self.btnRegCancel = QtWidgets.QPushButton(parent=regWindow)
        self.btnRegCancel.setGeometry(QtCore.QRect(310, 420, 181, 24))
        self.btnRegCancel.setObjectName("btnRegCancel")
        self.graphicsView = QtWidgets.QGraphicsView(parent=regWindow)
        self.graphicsView.setGeometry(QtCore.QRect(180, 40, 431, 521))
        self.graphicsView.setObjectName("graphicsView")
        self.btnRegPVis = QtWidgets.QPushButton(parent=regWindow)
        self.btnRegPVis.setGeometry(QtCore.QRect(472, 243, 32, 32))
        self.btnRegPVis.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border-color: rgba(255, 255, 255, 0);\n"
"}")
        self.btnRegPVis.setText("")
        self.btnRegPVis.setObjectName("btnRegPVis")
        self.txtRegUname = QtWidgets.QLineEdit(parent=regWindow)
        self.txtRegUname.setGeometry(QtCore.QRect(280, 200, 231, 31))
        self.txtRegUname.setObjectName("txtRegUname")
        self.btnRegLogin = QtWidgets.QPushButton(parent=regWindow)
        self.btnRegLogin.setGeometry(QtCore.QRect(310, 460, 181, 24))
        self.btnRegLogin.setObjectName("btnRegLogin")
        self.txtRegPHint = QtWidgets.QLineEdit(parent=regWindow)
        self.txtRegPHint.setGeometry(QtCore.QRect(280, 320, 231, 31))
        self.txtRegPHint.setObjectName("txtRegPHint")
        self.txtRegPword = QtWidgets.QLineEdit(parent=regWindow)
        self.txtRegPword.setGeometry(QtCore.QRect(280, 240, 231, 31))
        self.txtRegPword.setObjectName("txtRegPword")
        self.btnRegister = QtWidgets.QPushButton(parent=regWindow)
        self.btnRegister.setGeometry(QtCore.QRect(310, 380, 181, 24))
        self.btnRegister.setObjectName("btnRegister")
        self.graphicsView.raise_()
        self.txtRegUname.raise_()
        self.txtRegPHint.raise_()
        self.txtRegConPword.raise_()
        self.lblRegTitle.raise_()
        self.txtRegPword.raise_()
        self.btnRegCancel.raise_()
        self.btnRegister.raise_()
        self.btnRegLogin.raise_()
        self.btnRegPVis.raise_()

        self.retranslateUi(regWindow)
        QtCore.QMetaObject.connectSlotsByName(regWindow)

    def retranslateUi(self, regWindow):
        _translate = QtCore.QCoreApplication.translate
        regWindow.setWindowTitle(_translate("regWindow", "Dialog"))
        self.lblRegTitle.setText(_translate("regWindow", "Register"))
        self.txtRegConPword.setPlaceholderText(_translate("regWindow", "Confirm Password:"))
        self.btnRegCancel.setText(_translate("regWindow", "Cancel"))
        self.txtRegUname.setPlaceholderText(_translate("regWindow", "Enter Username:"))
        self.btnRegLogin.setText(_translate("regWindow", "Login"))
        self.txtRegPHint.setPlaceholderText(_translate("regWindow", "Forgot Password Hint:"))
        self.txtRegPword.setPlaceholderText(_translate("regWindow", "Enter Password:"))
        self.btnRegister.setText(_translate("regWindow", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    regWindow = QtWidgets.QDialog()
    ui = Ui_regWindow()
    ui.setupUi(regWindow)
    regWindow.show()
    sys.exit(app.exec())
