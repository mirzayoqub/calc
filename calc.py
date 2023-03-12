# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from sdf import Neuron

class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.robot = Neuron('jack')
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 628)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 400, 80))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 120, 0);\n"
"color: rgb(246, 245, 244);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 80, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("selection-background-color: rgb(255, 120, 0);\n"
"background-color: rgb(28, 113, 216);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 80, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(53, 132, 228);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 80, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(53, 132, 228);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 180, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(53, 132, 228);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 180, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(53, 132, 228);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 180, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(53, 132, 228);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(300, 180, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(53, 132, 228);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(300, 80, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(53, 132, 228);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 280, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(53, 132, 228);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(100, 280, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(53, 132, 228);")
        self.pushButton_10.setObjectName("pushButton_10")
        # self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_11.setGeometry(QtCore.QRect(200, 280, 100, 100))
        # font = QtGui.QFont()
        # font.setPointSize(20)
        # self.pushButton_11.setFont(font)
        # self.pushButton_11.setStyleSheet("background-color: rgb(53, 132, 228);")
        # self.pushButton_11.setObjectName("pushButton_11")
        # self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_12.setGeometry(QtCore.QRect(300, 280, 100, 100))
        # font = QtGui.QFont()
        # font.setPointSize(20)
        # self.pushButton_12.setFont(font)
        # self.pushButton_12.setStyleSheet("background-color: rgb(53, 132, 228);")
        # self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(0, 380, 201, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background-color: rgb(53, 132, 228);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(200, 280, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(53, 132, 228);\n" "color: rgb(224, 27, 36);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(0, 480, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("background-color: rgb(53, 132, 228);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(100, 480, 100, 100))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("background-color: rgb(53, 132, 228);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(200, 480, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("background-color: rgb(53, 132, 228);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(300, 480, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("border-color: rgb(237, 51, 59);\n"
"background-color: rgb(53, 132, 228);\n"
"color: rgb(224, 27, 36);")
        self.pushButton_18.setObjectName("pushButton_18")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "0"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_4.setText(_translate("MainWindow", "5"))
        self.pushButton_5.setText(_translate("MainWindow", "6"))
        self.pushButton_6.setText(_translate("MainWindow", "7"))
        self.pushButton_7.setText(_translate("MainWindow", "8"))
        self.pushButton_8.setText(_translate("MainWindow", "4"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_10.setText(_translate("MainWindow", "0"))
        self.pushButton_13.setText(_translate("MainWindow", "+"))
        self.pushButton_14.setText(_translate("MainWindow", "="))
        self.pushButton_15.setText(_translate("MainWindow", "-"))
        self.pushButton_16.setText(_translate("MainWindow", "/"))
        self.pushButton_17.setText(_translate("MainWindow", "*"))
        self.pushButton_18.setText(_translate("MainWindow", "C"))


    def write_number(self):
        self.robot.says()
        self.pushButton.clicked.connect(lambda: self.ret_number(self.pushButton.text()))
        self.pushButton_2.clicked.connect(lambda: self.ret_number(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.ret_number(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda: self.ret_number(self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(lambda: self.ret_number(self.pushButton_5.text()))
        self.pushButton_6.clicked.connect(lambda: self.ret_number(self.pushButton_6.text()))
        self.pushButton_7.clicked.connect(lambda: self.ret_number(self.pushButton_7.text()))
        self.pushButton_8.clicked.connect(lambda: self.ret_number(self.pushButton_8.text()))
        self.pushButton_9.clicked.connect(lambda: self.ret_number(self.pushButton_9.text()))
        self.pushButton_14.clicked.connect(lambda: self.result())
        self.pushButton_15.clicked.connect(lambda: self.ret_number(self.pushButton_15.text()))
        self.pushButton_16.clicked.connect(lambda: self.ret_number(self.pushButton_16.text()))
        self.pushButton_13.clicked.connect(lambda: self.ret_number(self.pushButton_13.text()))
        self.pushButton_17.clicked.connect(lambda: self.ret_number(self.pushButton_17.text()))
        self.pushButton_18.clicked.connect(lambda: self.operator(self.pushButton_18.text()))
        self.pushButton_10.clicked.connect(lambda: self.ret_number(self.pushButton_10.text()))

    def ret_number(self, number):
        if self.label.text() == "0":
            self.label.setText(number)

        else:
            self.label.setText(self.label.text() + number)

    def result(self):
        self.label.setText(str(eval(self.label.text())))
        print(self.label.text())
        self.robot.how(f"{self.label.text()}")


    def operator(self, op):
        if op == "C":
            self.label.setText("0")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.write_number()
    MainWindow.show()
    sys.exit(app.exec_())
