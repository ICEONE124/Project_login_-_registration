# Form implementation generated from reading ui file 'count.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_1(object):
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)

        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1200, 800))

        self.widget.setStyleSheet("QWidget#widget{\n"
                                  "background-color:qlineargradient("
                                  "spread:pad,"
                                  " x1:0.0101244,"
                                  " y1:0, x2:0.71592,"
                                  " y2:0.875,"
                                  " stop:0 rgba(0, 0, 255, 255),"
                                  " stop:1 rgba(255, 85, 0, 255))}")

        self.widget.setObjectName("widget")

        self.label = QtWidgets.QLabel(parent=self.widget)

        self.label.setGeometry(QtCore.QRect(380, 120, 461, 81))
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";\n"
                                 "color:rgb(255, 255, 255)")

        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent=self.widget)

        self.label_2.setGeometry(QtCore.QRect(420, 210, 511, 61))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
                                   "color:rgb(255, 255, 255)")

        self.label_2.setObjectName("label_2")

        self.hesap_olus = QtWidgets.QPushButton(parent=self.widget)

        self.hesap_olus.setGeometry(QtCore.QRect(430, 620, 331, 51))
        self.hesap_olus.setStyleSheet("border-radius:20px;\n"
                                      "color:rgb(0, 0, 0);\n"
                                      "background-color:rgb(0, 238, 238);\n"
                                      "font: 14pt \"MS Shell Dlg 2\";")

        self.hesap_olus.setObjectName("hesap_olus")

        self.user = QtWidgets.QLineEdit(parent=self.widget)

        self.user.setGeometry(QtCore.QRect(440, 300, 321, 51))
        self.user.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                "font: 12pt \"MS Shell Dlg 2\";")

        self.user.setObjectName("user")

        self.passwordfield = QtWidgets.QLineEdit(parent=self.widget)

        self.passwordfield.setGeometry(QtCore.QRect(440, 410, 321, 51))
        self.passwordfield.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                         "font: 12pt \"MS Shell Dlg 2\";")

        self.passwordfield.setObjectName("passwordfield")

        self.label_5 = QtWidgets.QLabel(parent=self.widget)

        self.label_5.setGeometry(QtCore.QRect(440, 270, 121, 21))
        self.label_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")

        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(parent=self.widget)

        self.label_6.setGeometry(QtCore.QRect(440, 380, 121, 21))
        self.label_6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")

        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(parent=self.widget)

        self.label_7.setGeometry(QtCore.QRect(440, 590, 321, 21))
        self.label_7.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
                                   "color:rgb(255, 0, 0);")
        self.label_7.setText("")

        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(parent=self.widget)

        self.label_8.setGeometry(QtCore.QRect(440, 490, 121, 21))
        self.label_8.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")

        self.label_8.setObjectName("label_8")

        self.passwordfield_2 = QtWidgets.QLineEdit(parent=self.widget)

        self.passwordfield_2.setGeometry(QtCore.QRect(440, 520, 321, 51))
        self.passwordfield_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                           "font: 12pt \"MS Shell Dlg 2\";")

        self.passwordfield_2.setObjectName("passwordfield_2")

        self.pushButton = QtWidgets.QPushButton(parent=self.widget)

        self.pushButton.setGeometry(QtCore.QRect(990, 717, 91, 31))
        self.pushButton.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
                                      "color:rgb(170, 85, 0);\n"
                                      "border-radius:10px;\n"
                                      "background-color:rgb(85, 255, 127)")

        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate

        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        self.label.setText(_translate("Dialog", "Регистрация"))
        self.label_2.setText(_translate("Dialog", "Создайте запись с вашей личной информацией"))
        self.hesap_olus.setText(_translate("Dialog", "ЗАРЕГИСТРИРОВАТЬСЯ"))
        self.label_5.setText(_translate("Dialog", "Имя пользователя"))
        self.label_6.setText(_translate("Dialog", "Пароль"))
        self.label_8.setText(_translate("Dialog", "пароль еще раз"))
        self.pushButton.setText(_translate("Dialog", "ВЫХОД"))
