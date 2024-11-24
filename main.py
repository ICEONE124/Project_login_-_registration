import sys

from PyQt6.uic import loadUi
from PyQt6 import QtWidgets

from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.QtWidgets import QWidget, QStackedWidget

from count_ui import Ui_Dialog_1
from enter_ui import Ui_Dialog_2
from login_ui import Ui_Dialog_3

import sqlite3


class welcome(QDialog, Ui_Dialog_3):
    def __init__(self):
        super(QDialog, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.func1)
        self.hesapolustur.clicked.connect(self.func2)
        self.pushButton_2.clicked.connect(self.exit)

    def exit(self):
        QApplication.exit()

    def func1(self):
        login = Log()

        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def func2(self):
        hesap_olustur = Reg()

        widget.addWidget(hesap_olustur)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Reg(QDialog, Ui_Dialog_1):
    def __init__(self):
        super(Reg, self).__init__()
        self.setupUi(self)

        self.b()
        self.hesap_olus.clicked.connect(self.c)
        self.pushButton.clicked.connect(self.a)

    def a(self):

        o = welcome()

        widget.addWidget(o)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def b(self):

        self.con = sqlite3.connect(r"infos.db")
        self.cursor = self.con.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS bilgiler(user TEXT,password TEXT)")

    def c(self):

        user = self.user.text()

        a = self.passwordfield.text()
        a1 = self.passwordfield_2.text()

        if len(a) == 0 or len(a1) == 0 or len(user) == 0:
            self.label_7.setText("Есть незаполненные поля!")

        elif a != a1:
            self.label_7.setText("Пароли не совпадают!")

        else:
            self.cursor.execute("INSERT into bilgiler values(?,?)", (user, a))

            self.con.commit()
            self.label_7.setText("Аккаунт создан")


class Log(QDialog, Ui_Dialog_2):
    def __init__(self):

        super(Log, self).__init__()
        self.setupUi(self)

        self.pushButton_3.clicked.connect(self.c)
        self.pushButton.clicked.connect(self.a)

    def a(self):

        o = welcome()

        widget.addWidget(o)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def c(self):

        user = self.lineEdit.text()
        password = self.passwordfield.text()

        if user == "" or len(password) == 0:
            self.label_7.setText("Остались поля пустыми!")

        else:
            con = sqlite3.connect(r"infos.db")
            cur = con.cursor()
            s = "SELECT password from bilgiler WHERE user = \'" + user + "\'"
            cur.execute(s)
            sonuc = cur.fetchall()

            a = sonuc[0]

            if a[0] == password:
                self.label_7.setText("Успешный вход")
                print("Успешный вход")

            else:
                print(a)

                self.label_7.setText("Неверная информация!")
                print("Неправильная попытка.")


app = QApplication(sys.argv)
welcome1 = welcome()
widget = QStackedWidget()

widget.addWidget(welcome1)

widget.setFixedHeight(800)
widget.setFixedWidth(1200)

widget.show()

try:
    sys.exit(app.exec())

except:
    print("выход")
