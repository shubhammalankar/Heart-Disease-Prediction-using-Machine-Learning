# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondpage2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import numpy as np
import pandas as pd

from PyQt5 import QtCore, QtGui, QtWidgets

import os

class Ui_OtherWindow(object):

    def openWindow2(self):

        def __init__(self):
            super().__init__()
            self.ui = Ui_OtherWindow()
            self.ui.setupUi(self)
            self.ui.pushButton.clicked.connect(self.formsubmit)
            self.dataset = pd.read_csv("C:/Users/Karan Kalla/Desktop/Datasets/dicot_processed.csv")
            self.X = self.dataset.iloc[:, 0:10].values
            self.y = self.dataset.iloc[:, 10].values
            self.classifier = None

        def formsubmit(self):

            val1 = self.ui.lineEdit.text()
            age = int(val1)
            print(age)
            if self.ui.radioButton.isChecked() == True:
                sex = 1
            else:
                sex = 0
            print(sex)

            cp = self.ui.comboBox.currentIndex()
            cp = cp + 1
            print(cp)

            val1 = self.ui.lineEdit_2.text()
            maxhr = int(val1)

            if self.ui.radioButton_3.isChecked() == True:
                eia = 1
            else:
                eia = 0

            val1 = self.ui.lineEdit_3.text()
            stdep = float(val1)
            print(stdep)

            slope = self.ui.comboBox_2.currentIndex()
            slope = slope + 1
            print(slope)

            mv = self.ui.spinBox.value()
            print(mv)

            thal = self.ui.comboBox_3.currentIndex()
            if thal == 0:
                thal = 3
            elif thal == 1:
                thal = 6
            else:
                thal = 7
            print(thal)

            val1 = self.ui.lineEdit_4.text()
            restecg = int(val1)
#################################################################################  RANDOM FOREST
            from sklearn.model_selection import train_test_split
            X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=3)
            from sklearn.ensemble import RandomForestClassifier
            self.classifier = RandomForestClassifier(n_estimators=20, random_state=3)
            self.classifier.fit(X_train, y_train)
            y_pred = self.classifier.predict(X_test)
            # classifierBuild()
            input = np.array([[thal, cp, mv, stdep, eia, maxhr, slope, age, sex, restecg]])
            prediction = self.classifier.predict(input)

##################################################################################  SVM
            from sklearn.model_selection import train_test_split
            X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=3)
            from sklearn.svm import SVC
            self.svclassifier = SVC(kernel='linear')
            self.svclassifier.fit(X_train, y_train)
            y_pred = self.svclassifier.predict(X_test)
            # classifierBuild()
            input = np.array([[thal, cp, mv, stdep, eia, maxhr, slope, age, sex, restecg]])
            prediction1 = self.svclassifier.predict(input)


        os.system('python app.py')


    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 9, 531, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 22pt \"Segoe MDL2 Assets\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(159, 125, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(159, 152, 29, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(159, 183, 88, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(159, 214, 259, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(159, 245, 195, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(159, 276, 119, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(159, 307, 217, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(159, 338, 211, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(159, 369, 103, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setMouseTracking(False)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(159, 400, 81, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(510, 183, 120, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(510, 125, 120, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(510, 214, 120, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(510, 276, 120, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(510, 307, 120, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(510, 338, 120, 21))
        self.spinBox.setMaximum(3)
        self.spinBox.setObjectName("spinBox")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(510, 369, 120, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(510, 400, 120, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(510, 150, 191, 31))
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(120, 10, 61, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(510, 240, 191, 31))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(120, 10, 41, 16))
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 480, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(160, 60, 391, 41))
        self.label_12.setMaximumSize(QtCore.QSize(391, 16777215))
        self.label_12.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
                                    "font: 14pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        OtherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OtherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        OtherWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "Patient Details"))
        self.label.setText(_translate("OtherWindow", "Heart Disease Prediction Using ML"))
        self.label_2.setText(_translate("OtherWindow", "Age"))
        self.label_3.setText(_translate("OtherWindow", "Sex"))
        self.label_4.setText(_translate("OtherWindow", "Chest Pain"))
        self.label_5.setText(_translate("OtherWindow", "Maximum Heart Rate Achieved"))
        self.label_6.setText(_translate("OtherWindow", "Exercise Induced Agina"))
        self.label_7.setText(_translate("OtherWindow", "ST Depression"))
        self.label_8.setText(_translate("OtherWindow", "Slope of ST Peak Segment"))
        self.label_9.setText(_translate("OtherWindow", "Number of Major Vessels"))
        self.label_10.setText(_translate("OtherWindow", "Thalassemia"))
        self.label_11.setText(_translate("OtherWindow", "Rest ECG"))
        self.comboBox.setItemText(0, _translate("OtherWindow", "1 - Typical Angina"))
        self.comboBox.setItemText(1, _translate("OtherWindow", "2 - Atypical Angina"))
        self.comboBox.setItemText(2, _translate("OtherWindow", "3 - Nonanginal Pain"))
        self.comboBox.setItemText(3, _translate("OtherWindow", "4 - Asymptotic Angina"))
        self.comboBox_2.setItemText(0, _translate("OtherWindow", "Upsloping"))
        self.comboBox_2.setItemText(1, _translate("OtherWindow", "Flat"))
        self.comboBox_2.setItemText(2, _translate("OtherWindow", "DownSloping"))
        self.comboBox_3.setItemText(0, _translate("OtherWindow", "Normal"))
        self.comboBox_3.setItemText(1, _translate("OtherWindow", "Fixed Defect"))
        self.comboBox_3.setItemText(2, _translate("OtherWindow", "Reversed Defect"))
        self.radioButton.setText(_translate("OtherWindow", "Male"))
        self.radioButton_2.setText(_translate("OtherWindow", "Female"))
        self.radioButton_3.setText(_translate("OtherWindow", "Yes"))
        self.radioButton_4.setText(_translate("OtherWindow", "No"))
        self.pushButton.setText(_translate("OtherWindow", "Predict !"))
        self.label_12.setText(_translate("OtherWindow", "Please Enter Patient Details"))
        self.pushButton.clicked.connect(self.openWindow2)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())
