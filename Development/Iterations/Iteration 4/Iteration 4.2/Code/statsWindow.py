# Form implementation generated from reading ui file 'statsWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_statisticsWindow(object):
    def setupUi(self, statisticsWindow):
        statisticsWindow.setObjectName("statisticsWindow")
        statisticsWindow.resize(800, 600)
        statisticsWindow.setMinimumSize(QtCore.QSize(800, 600))
        statisticsWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.swStats = QtWidgets.QStackedWidget(parent=statisticsWindow)
        self.swStats.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.swStats.setObjectName("swStats")
        self.statsMain = QtWidgets.QWidget()
        self.statsMain.setObjectName("statsMain")
        self.lblStatsTitle = QtWidgets.QLabel(parent=self.statsMain)
        self.lblStatsTitle.setGeometry(QtCore.QRect(280, 100, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.lblStatsTitle.setFont(font)
        self.lblStatsTitle.setObjectName("lblStatsTitle")
        self.btnStatsPPD = QtWidgets.QPushButton(parent=self.statsMain)
        self.btnStatsPPD.setGeometry(QtCore.QRect(300, 380, 200, 30))
        self.btnStatsPPD.setObjectName("btnStatsPPD")
        self.btnStatsBPD = QtWidgets.QPushButton(parent=self.statsMain)
        self.btnStatsBPD.setGeometry(QtCore.QRect(300, 260, 200, 30))
        self.btnStatsBPD.setObjectName("btnStatsBPD")
        self.btnStatsPCD = QtWidgets.QPushButton(parent=self.statsMain)
        self.btnStatsPCD.setGeometry(QtCore.QRect(300, 320, 200, 30))
        self.btnStatsPCD.setObjectName("btnStatsPCD")
        self.btnStatsHome = QtWidgets.QPushButton(parent=self.statsMain)
        self.btnStatsHome.setGeometry(QtCore.QRect(325, 520, 150, 30))
        self.btnStatsHome.setObjectName("btnStatsHome")
        self.btnStatsBCD = QtWidgets.QPushButton(parent=self.statsMain)
        self.btnStatsBCD.setGeometry(QtCore.QRect(300, 200, 200, 30))
        self.btnStatsBCD.setObjectName("btnStatsBCD")
        self.gVStats = QtWidgets.QGraphicsView(parent=self.statsMain)
        self.gVStats.setGeometry(QtCore.QRect(120, 60, 560, 421))
        self.gVStats.setObjectName("gVStats")
        self.gVStats.raise_()
        self.lblStatsTitle.raise_()
        self.btnStatsPPD.raise_()
        self.btnStatsBPD.raise_()
        self.btnStatsPCD.raise_()
        self.btnStatsHome.raise_()
        self.btnStatsBCD.raise_()
        self.swStats.addWidget(self.statsMain)
        self.statsBin = QtWidgets.QWidget()
        self.statsBin.setObjectName("statsBin")
        self.btnBinCalc = QtWidgets.QPushButton(parent=self.statsBin)
        self.btnBinCalc.setGeometry(QtCore.QRect(220, 400, 150, 30))
        self.btnBinCalc.setObjectName("btnBinCalc")
        self.txtBinPValue = QtWidgets.QLineEdit(parent=self.statsBin)
        self.txtBinPValue.setGeometry(QtCore.QRect(250, 240, 300, 30))
        self.txtBinPValue.setObjectName("txtBinPValue")
        self.gVBin = QtWidgets.QGraphicsView(parent=self.statsBin)
        self.gVBin.setGeometry(QtCore.QRect(95, 91, 611, 411))
        self.gVBin.setObjectName("gVBin")
        self.txtBinTrials = QtWidgets.QLineEdit(parent=self.statsBin)
        self.txtBinTrials.setGeometry(QtCore.QRect(250, 170, 300, 30))
        self.txtBinTrials.setObjectName("txtBinTrials")
        self.btnBinHome = QtWidgets.QPushButton(parent=self.statsBin)
        self.btnBinHome.setGeometry(QtCore.QRect(430, 400, 150, 30))
        self.btnBinHome.setObjectName("btnBinHome")
        self.txtBinSuccesses = QtWidgets.QLineEdit(parent=self.statsBin)
        self.txtBinSuccesses.setGeometry(QtCore.QRect(250, 310, 300, 30))
        self.txtBinSuccesses.setObjectName("txtBinSuccesses")
        self.gVBin.raise_()
        self.btnBinCalc.raise_()
        self.txtBinPValue.raise_()
        self.txtBinTrials.raise_()
        self.btnBinHome.raise_()
        self.txtBinSuccesses.raise_()
        self.swStats.addWidget(self.statsBin)
        self.statsPoi = QtWidgets.QWidget()
        self.statsPoi.setObjectName("statsPoi")
        self.gVPoi = QtWidgets.QGraphicsView(parent=self.statsPoi)
        self.gVPoi.setGeometry(QtCore.QRect(95, 81, 611, 411))
        self.gVPoi.setObjectName("gVPoi")
        self.txtPoiRate = QtWidgets.QLineEdit(parent=self.statsPoi)
        self.txtPoiRate.setGeometry(QtCore.QRect(250, 200, 300, 30))
        self.txtPoiRate.setObjectName("txtPoiRate")
        self.txtPoiSuccesses = QtWidgets.QLineEdit(parent=self.statsPoi)
        self.txtPoiSuccesses.setGeometry(QtCore.QRect(250, 280, 300, 30))
        self.txtPoiSuccesses.setObjectName("txtPoiSuccesses")
        self.btnPoiCalculate = QtWidgets.QPushButton(parent=self.statsPoi)
        self.btnPoiCalculate.setGeometry(QtCore.QRect(220, 390, 150, 30))
        self.btnPoiCalculate.setObjectName("btnPoiCalculate")
        self.btnPoiCancel = QtWidgets.QPushButton(parent=self.statsPoi)
        self.btnPoiCancel.setGeometry(QtCore.QRect(430, 390, 150, 30))
        self.btnPoiCancel.setObjectName("btnPoiCancel")
        self.swStats.addWidget(self.statsPoi)

        self.retranslateUi(statisticsWindow)
        self.swStats.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(statisticsWindow)

    def retranslateUi(self, statisticsWindow):
        _translate = QtCore.QCoreApplication.translate
        statisticsWindow.setWindowTitle(_translate("statisticsWindow", "Dialog"))
        self.lblStatsTitle.setText(_translate("statisticsWindow", "Statistical Functions"))
        self.btnStatsPPD.setText(_translate("statisticsWindow", "Poisson Probability Distribution"))
        self.btnStatsBPD.setText(_translate("statisticsWindow", "Binomial Probability Distribution"))
        self.btnStatsPCD.setText(_translate("statisticsWindow", "Poisson Cumulative Distribution"))
        self.btnStatsHome.setText(_translate("statisticsWindow", "Home"))
        self.btnStatsBCD.setText(_translate("statisticsWindow", "Binomial Cumulative Distribution"))
        self.btnBinCalc.setText(_translate("statisticsWindow", "Calculate"))
        self.txtBinPValue.setPlaceholderText(_translate("statisticsWindow", "Probability of Success:"))
        self.txtBinTrials.setPlaceholderText(_translate("statisticsWindow", "Number of Trials:"))
        self.btnBinHome.setText(_translate("statisticsWindow", "Home"))
        self.txtBinSuccesses.setPlaceholderText(_translate("statisticsWindow", "Number of Successes:"))
        self.txtPoiRate.setPlaceholderText(_translate("statisticsWindow", "Average Rate:"))
        self.txtPoiSuccesses.setPlaceholderText(_translate("statisticsWindow", "Number of Successes:"))
        self.btnPoiCalculate.setText(_translate("statisticsWindow", "Calculate"))
        self.btnPoiCancel.setText(_translate("statisticsWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    statisticsWindow = QtWidgets.QDialog()
    ui = Ui_statisticsWindow()
    ui.setupUi(statisticsWindow)
    statisticsWindow.show()
    sys.exit(app.exec())
