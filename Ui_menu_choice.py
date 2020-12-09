# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\python\test\menu_choice.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(516, 498)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(31, 11, 414, 24))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(41, 376, 205, 50))
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(252, 41, 231, 71))
        self.textEdit.setStyleSheet("font: 12pt \"黑体\";")
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(41, 41, 139, 19))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(252, 175, 231, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(252, 118, 231, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("font: 10pt \"楷体\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(252, 289, 231, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(252, 345, 231, 81))
        self.textEdit_2.setStyleSheet("font: 12pt \"黑体\";")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(147, 80, 60, 231))
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(252, 232, 231, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(41, 80, 67, 258))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 516, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "选择困难症专属吃饭神器"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#5500ff;\">爷专属吃饭神器</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">快来猜猜今天吃什么吧！</span></p><p><span style=\" font-size:12pt; font-weight:600;\">输入序号或者菜名都可以哦~</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">这是今天的菜单哦~</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "\n"
"哼!爷就不猜！\n"
""))
        self.pushButton.setText(_translate("MainWindow", "\n"
"给爷猜！\n"
""))
        self.pushButton_4.setText(_translate("MainWindow", "爷要选自己爱吃的！"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#0055ff;\">11.肯德基</span></p><p><span style=\" font-size:10pt; font-weight:600; color:#aa00ff;\">12.蛋包饭</span></p><p><span style=\" font-size:10pt; font-weight:600; color:#0055ff;\">13.黄焖鸡</span></p><p><span style=\" font-size:10pt; font-weight:600; color:#aa00ff;\">14.烤肉</span></p><p><span style=\" font-size:10pt; font-weight:600; color:#0055ff;\">15.烧烤</span></p><p><span style=\" font-size:10pt; font-weight:600; color:#aa00ff;\">16.小龙虾</span></p><p><span style=\" font-size:10pt; font-weight:600; color:#0055ff;\">17.寿司</span></p><p><span style=\" font-size:10pt; font-weight:600; color:#aa00ff;\">18.粉面</span></p><p><span style=\" font-size:10pt; font-weight:600; color:#0055ff;\">19.小笼包</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "\n"
"爷不满意！给爷重新上菜！\n"
""))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#0055ff;\">1.费大厨</span></p><p><span style=\" font-size:10pt; font-weight:600; color:#aa00ff;\">2.胖哥俩</span></p><p><span style=\" font-size:10pt; font-weight:600; color:#0055ff;\">3.思必客</span></p><p><span style=\" font-size:10pt; font-weight:600; color:#aa00ff;\">4.自煮水饺</span></p><p><span style=\" font-size:10pt; font-weight:600; color:#0055ff;\">5.自煮火锅</span></p><p><span style=\" font-size:10pt; font-weight:600; color:#aa00ff;\">6.蛙来哒</span></p><p><span style=\" font-size:10pt; font-weight:600; color:#0055ff;\">7.汴京炸鸡</span></p><p><span style=\" font-size:10pt; font-weight:600; color:#aa00ff;\">8.娟娟</span></p><p><span style=\" font-size:10pt; font-weight:600; color:#0055ff;\">9.椰子鸡</span></p><p><span style=\" font-size:10pt; font-weight:600; color:#aa00ff;\">10.食三姨</span></p></body></html>"))
