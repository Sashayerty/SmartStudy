import io
import sqlite3
import sys

import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QTableWidgetItem,
    QWidget,
)
from templates import (
    template,
    template2,
    template3,
    template_calc_of_marks,
    template_calculator,
    template_of_formuls,
    template_of_graphs,
    template_of_theoremes,
    template_roots,
)


# Backend для приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init()

    def initUI(self):
        f = io.StringIO(template.template)
        uic.loadUi(f, self)

    def init(self):
        self.pushButton.clicked.connect(self.run_btn)
        self.pushButton_2.clicked.connect(self.run_btn2)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.run_btn2()

    def run_btn(self):
        self.w = AboutUs()
        self.w.show()

    def run_btn2(self):
        self.w = MenuWindow()
        self.w.show()
        self.hide()


class AboutUs(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        f2 = io.StringIO(template2.template2)
        uic.loadUi(f2, self)


class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init()

    def initUI(self):
        f3 = io.StringIO(template3.template3)
        uic.loadUi(f3, self)

    def init(self):
        self.pushButton.clicked.connect(self.run_btn1)
        self.pushButton_2.clicked.connect(self.run_btn2)
        self.pushButton_3.clicked.connect(self.run_btn3)
        self.pushButton_4.clicked.connect(self.run_btn4)
        self.pushButton_5.clicked.connect(self.run_btn5)
        self.pushButton_6.clicked.connect(self.run_btn6)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            self.run_btn1()
        elif event.key() == Qt.Key_2:
            self.run_btn2()
        elif event.key() == Qt.Key_3:
            self.run_btn3()
        elif event.key() == Qt.Key_4:
            self.run_btn4()
        elif event.key() == Qt.Key_5:
            self.run_btn5()
        elif event.key() == Qt.Key_6:
            self.run_btn6()

    def run_btn1(self):
        self.w = Calculator()
        self.w.show()

    def run_btn2(self):
        self.w = CalculatorOfMarks()
        self.w.show()

    def run_btn3(self):
        self.w = Theoremes()
        self.w.show()

    def run_btn4(self):
        self.w = Graphs()
        self.w.show()

    def run_btn5(self):
        self.w = Formuls()
        self.w.show()

    def run_btn6(self):
        self.w = Roots()
        self.w.show()


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init()

    def initUI(self):
        f = io.StringIO(template_calculator.template_calculator)
        uic.loadUi(f, self)

    def init(self):
        self.doing = ""
        self.num1 = ""
        self.num2 = ""
        self.is_num2 = False
        self.btn_0.clicked.connect(lambda: self.psh_btn_num("0"))
        self.btn_1.clicked.connect(lambda: self.psh_btn_num("1"))
        self.btn_2.clicked.connect(lambda: self.psh_btn_num("2"))
        self.btn_3.clicked.connect(lambda: self.psh_btn_num("3"))
        self.btn_4.clicked.connect(lambda: self.psh_btn_num("4"))
        self.btn_5.clicked.connect(lambda: self.psh_btn_num("5"))
        self.btn_6.clicked.connect(lambda: self.psh_btn_num("6"))
        self.btn_7.clicked.connect(lambda: self.psh_btn_num("7"))
        self.btn_8.clicked.connect(lambda: self.psh_btn_num("8"))
        self.btn_9.clicked.connect(lambda: self.psh_btn_num("9"))
        self.btn_plus.clicked.connect(lambda: self.psh_doing("+"))
        self.btn_minus.clicked.connect(lambda: self.psh_doing("-"))
        self.btn_div.clicked.connect(lambda: self.psh_doing("/"))
        self.btn_mul.clicked.connect(lambda: self.psh_doing("*"))
        self.btn_eq.clicked.connect(self.psh_eq)
        self.btn_clear.clicked.connect(self.psh_clear)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_0:
            self.btn_0.click()
        elif event.key() == Qt.Key_1:
            self.btn_1.click()
        elif event.key() == Qt.Key_2:
            self.btn_2.click()
        elif event.key() == Qt.Key_3:
            self.btn_3.click()
        elif event.key() == Qt.Key_4:
            self.btn_4.click()
        elif event.key() == Qt.Key_5:
            self.btn_5.click()
        elif event.key() == Qt.Key_6:
            self.btn_6.click()
        elif event.key() == Qt.Key_7:
            self.btn_7.click()
        elif event.key() == Qt.Key_8:
            self.btn_8.click()
        elif event.key() == Qt.Key_9:
            self.btn_9.click()
        elif event.key() == Qt.Key_Minus:
            self.btn_minus.click()
        elif event.key() == Qt.Key_Plus:
            self.btn_plus.click()
        elif event.key() == Qt.Key_Equal or event.key() == Qt.Key_Return:
            self.btn_eq.click()
        elif event.key() == Qt.Key_C or event.key() == Qt.Key_Backspace:
            self.btn_clear.click()

    def psh_btn_num(self, btn_text):
        global is_num2
        if not self.is_num2:
            if (
                self.table.text() == "0"
                or self.table.text() == "Error"
                or self.table.text() == "None"
            ):
                self.table.setText(btn_text)
            else:
                self.table.setText(self.table.text() + btn_text)
        else:
            self.is_num2 = False
            self.table.setText("" + btn_text)

    def psh_doing(self, btn_text):
        global doing
        global num1
        global is_num2
        self.doing = ""
        self.num1 = self.table.text()
        self.is_num2 = True
        self.doing += btn_text

    def psh_eq(self):
        global is_num2
        global doing
        global num1
        global num2
        self.num2 += self.table.text()
        if self.num2 == "0" and self.doing == "/":
            self.table.setText("Error")
        else:
            self.table.setText(
                str(eval(f"{self.num1} {self.doing} {self.num2}"))
            )  # noqa
        self.num2 = ""
        self.num1 = ""
        self.doing = ""
        self.is_num2 = False

    def psh_clear(self):
        global is_num2
        global doing
        global num1
        global num2
        self.num2 = ""
        self.num1 = ""
        self.doing = ""
        self.is_num2 = False
        self.table.setText("0")


class CalculatorOfMarks(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init()

    def initUI(self):
        f = io.StringIO(template_calc_of_marks.template_calc_of_marks)
        uic.loadUi(f, self)

    def init(self):
        self.marks = []
        self.btn_1.clicked.connect(lambda: self.add_mark("1"))
        self.btn_2.clicked.connect(lambda: self.add_mark("2"))
        self.btn_3.clicked.connect(lambda: self.add_mark("3"))
        self.btn_4.clicked.connect(lambda: self.add_mark("4"))
        self.btn_5.clicked.connect(lambda: self.add_mark("5"))
        self.btn_res.clicked.connect(self.psh_res)
        self.btn_clear.clicked.connect(self.psh_clear)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            self.btn_1.click()
        elif event.key() == Qt.Key_2:
            self.btn_2.click()
        elif event.key() == Qt.Key_3:
            self.btn_3.click()
        elif event.key() == Qt.Key_4:
            self.btn_4.click()
        elif event.key() == Qt.Key_5:
            self.btn_5.click()
        elif event.key() == Qt.Key_Equal or event.key() == Qt.Key_Return:
            self.btn_res.click()
        elif event.key() == Qt.Key_C:
            self.btn_clear.click()
        elif event.key() == Qt.Key_Backspace:
            self.btn_clear.click()

    def add_mark(self, mark):
        global marks
        self.marks.append(int(mark))
        if not self.lineEdit.text():
            self.lineEdit.setText(mark)
        else:
            self.lineEdit.setText(self.lineEdit.text() + "," + " " + mark)

    def psh_res(self):
        global marks
        if not self.lineEdit.text():
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("Введите хотя бы одну оценку!")
            msg_box.exec()
        else:
            self.table.setText(
                str(round((sum(self.marks) / len(self.marks)), ndigits=2))
            )

    def psh_clear(self):
        global marks
        self.marks = []
        self.table.setText("0")
        self.lineEdit.setText("")


class Roots(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init()

    def initUI(self):
        f = io.StringIO(template_roots.template_roots)
        uic.loadUi(f, self)

    def init(self):
        self.btn_roots.clicked.connect(self.psh_res)
        self.btn_clear.clicked.connect(self.btn_clean)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Equal or event.key() == Qt.Key_Return:
            self.btn_roots.click()
        elif event.key() == Qt.Key_C or event.key() == Qt.Key_Backspace:
            self.btn_clear.click()

    def btn_clean(self):
        self.set_text()

    def psh_res(self):
        self.zeros()
        self.a, self.b, self.c = self.checking_float()
        self.num_a, self.num_b, self.num_c = (
            self.line_a.text(),
            self.line_b.text(),
            self.line_c.text(),
        )
        if not self.num_a or not self.num_b or not self.num_c:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("Введите все значения!")
            msg_box.exec()
        elif self.checking_alphas():
            self.set_text()
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("Программа принимает только числа!")
            msg_box.exec()
        elif self.a == True or self.b == True or self.c == True:
            self.set_text()
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("Программа принимает только целые числа!")
            msg_box.exec()
        else:
            if self.num_a == "0" or self.num_b == "0" or self.num_c == "0":
                if self.num_a == "0" and self.num_b == "0" and int(self.num_c) != 0:
                    self.set_text()
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Ошибка")
                    msg_box.setText(f"К сожалению {self.num_c} не равно 0")
                    msg_box.exec()
                elif (
                    self.num_a[0] == "0"
                    and self.num_b[0] == "0"
                    and self.num_c[0] == "0"
                ):
                    self.set_text()
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Ошибка")
                    msg_box.setText("Не делай так больше!")
                    msg_box.exec()
                elif self.num_b == "0" and self.num_c == "0":
                    self.line_D.setText("Один корень")
                    self.line_r1.setText("0")
                    self.line_r2.setText("0")
                elif self.num_a == "0":
                    self.line_D.setText("Один корень")
                    if self.num_c == "0":
                        self.line_r1.setText("0")
                        self.line_r2.setText("0")
                    else:
                        self.line_r1.setText(
                            str((int(self.num_c) / int(self.num_b)) * -1)
                        )
                        self.line_r2.setText(
                            str((int(self.num_c) / int(self.num_b)) * -1)
                        )
                elif self.num_b == "0":
                    self.line_D.setText("2 корня")
                    self.line_r1.setText(
                        str((((int(self.num_c) / int(self.num_a)) * -1) ** 0.5) * -1)
                    )
                    self.line_r2.setText(
                        str(((int(self.num_c) / int(self.num_a)) * -1) ** 0.5)
                    )
                elif self.num_c == "0":
                    self.line_D.setText("2 корня")
                    self.line_r1.setText(str((int(self.num_b) / int(self.num_a)) * -1))
                    self.line_r2.setText("0")
            else:
                self.line_D.setText(
                    str(int(self.num_b) ** 2 + (-4 * int(self.num_a) * int(self.num_c)))
                )
                if int(self.line_D.text()) < 0:
                    self.line_r1.setText("Нет корней")
                    self.line_r2.setText("Нет корней")
                elif int(self.line_D.text()) == 0:
                    self.line_r1.setText(
                        str(
                            round(
                                (
                                    ((-1 * int(self.num_b)) - int(self.line_D.text()))
                                    / (2 * int(self.num_a))
                                ),
                                ndigits=4,
                            )
                        )
                    )
                    self.line_r2.setText(
                        str(
                            round(
                                (
                                    ((-1 * int(self.num_b)) - int(self.line_D.text()))
                                    / (2 * int(self.num_a))
                                ),
                                ndigits=4,
                            )
                        )
                    )
                else:
                    self.line_r1.setText(
                        str(
                            round(
                                (
                                    ((-1 * int(self.num_b)) - int(self.line_D.text()))
                                    / (2 * int(self.num_a))
                                ),
                                ndigits=4,
                            )
                        )
                    )
                    self.line_r2.setText(
                        str(
                            round(
                                (
                                    ((-1 * int(self.num_b)) + int(self.line_D.text()))
                                    / (2 * int(self.num_a))
                                ),
                                ndigits=4,
                            )
                        )
                    )

    def set_text(self):
        self.line_a.setText("")
        self.line_b.setText("")
        self.line_c.setText("")
        self.line_D.setText("")
        self.line_r1.setText("")
        self.line_r2.setText("")

    def zeros(self):
        for i, data in enumerate(
            [self.line_a.text(), self.line_b.text(), self.line_c.text()]
        ):
            if data and data.isdigit():
                if float(data) == 0.0:
                    if i == 0:
                        self.line_a.setText("0")
                    elif i == 1:
                        self.line_b.setText("0")
                    elif i == 2:
                        self.line_c.setText("0")
                elif data == "-0":
                    if i == 0:
                        self.line_a.setText("0")
                    elif i == 1:
                        self.line_b.setText("0")
                    elif i == 2:
                        self.line_c.setText("0")
                elif len(set(data)) == 1:
                    if list(set(data))[0] == "0":
                        if i == 0:
                            self.line_a.setText("0")
                        elif i == 1:
                            self.line_b.setText("0")
                        elif i == 2:
                            self.line_c.setText("0")

    def checking_alphas(self):
        for i in self.line_a.text(), self.line_b.text(), self.line_c.text():
            for j in i:
                if not j.isdigit():
                    return True

    def checking_float(self):
        self.a_is_float = False
        self.b_is_float = False
        self.c_is_float = False
        for i, data in enumerate(
            [self.line_a.text(), self.line_b.text(), self.line_c.text()]
        ):
            if "." in data:
                if data[1] == ".":
                    if i == 0:
                        self.a_is_float = True
                    elif i == 1:
                        self.b_is_float = True
                    elif i == 2:
                        self.c_is_float = True
        return self.a_is_float, self.b_is_float, self.c_is_float


class Theoremes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init()

    def initUI(self):
        f = io.StringIO(template_of_theoremes.template_of_theoremes)
        uic.loadUi(f, self)

    def init(self):
        self.con = sqlite3.connect("DataBaseOfApp.db")
        cur = self.con.cursor()
        self.combo_filtr.addItems(
            [
                i[0]
                for i in cur.execute("SELECT DISTINCT Предмет FROM Теоремы").fetchall()
                if i[0] != "Нет"
            ]
        )
        self.combo_filtr.addItem("Нет")
        self.btn_search.clicked.connect(self.psh_search)
        self.btn_add.clicked.connect(
            lambda: self.psh_add(
                self.line_name.text(), self.line_theorem.text(), self.line_subj.text()
            )
        )
        self.btn_save.clicked.connect(self.psh_save)
        self.btn_del.clicked.connect(self.psh_del)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.btn_search.click()

    def psh_search(self):
        cur = self.con.cursor()
        if self.combo_filtr.currentText() == "Нет":
            if self.line_search.text():
                res = cur.execute(
                    f"""SELECT id, Название, Теорема FROM Теоремы WHERE Название = '{self.line_search.text()}' """
                ).fetchall()
            else:
                res = cur.execute(
                    f"""SELECT id, Название, Теорема FROM Теоремы"""
                ).fetchall()
        else:
            if self.line_search.text():
                res = cur.execute(
                    f"""SELECT id, Название, Теорема FROM Теоремы WHERE Название = '{self.line_search.text()}' AND Предмет = '{str(self.combo_filtr.currentText())}' """
                ).fetchall()
            else:
                res = cur.execute(
                    f"""SELECT id, Название, Теорема FROM Теоремы WHERE Предмет = '{str(self.combo_filtr.currentText())}' """
                ).fetchall()
        if res:
            self.tableWidget.setRowCount(len(res))
            self.tableWidget.setColumnCount(len(res[0]))
            for i, elem in enumerate(res):
                for j, vol in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(vol)))
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("Ничего не найдено! Попробуйте снова.")
            msg_box.exec()

    def psh_add(self, name, theorem, subject):
        if not self.line_name.text():
            name = "Теорема"
        if not self.line_theorem.text():
            theorem = "Не добавлено"
        if not self.line_subj.text():
            subject = "Нет"
        valid = QMessageBox.question(
            self,
            "",
            f"Действительно добавить элемент {str(name)}?",
            QMessageBox.Yes,
            QMessageBox.No,
        )
        cur = self.con.cursor()
        if valid == QMessageBox.Yes:
            cur.execute(
                f"""INSERT INTO Теоремы (Название, Теорема, Предмет) VALUES ('{str(name)}', '{str(theorem)}', '{str(subject)}')"""
            )

    def psh_save(self):
        self.con.commit()

    def psh_del(self):
        cur = self.con.cursor()
        ids = cur.execute(f"""SELECT id FROM Теоремы""").fetchall()
        ids = [str(i)[1:-2] for i in ids]
        if not self.line_del.text().isdigit():
            self.line_del.setText("")
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("id это число")
            msg_box.exec()
        elif self.line_del.text() not in ids:
            self.line_del.setText("")
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("Такого id нет!")
            msg_box.exec()
        elif self.line_del.text():
            name = cur.execute(
                f"""SELECT DISTINCT Название FROM Теоремы WHERE id={int(self.line_del.text())}"""
            ).fetchall()
            valid = QMessageBox.question(
                self,
                "",
                f"Действительно удалить элемент {name[:][0][0][:]}?",
                QMessageBox.Yes,
                QMessageBox.No,
            )
            if valid == QMessageBox.Yes:
                cur.execute(
                    f"""DELETE FROM Теоремы WHERE id = {int(self.line_del.text())}"""
                )


class Formuls(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init()

    def initUI(self):
        f = io.StringIO(template_of_formuls.template_of_formuls)
        uic.loadUi(f, self)

    def init(self):
        self.con = sqlite3.connect("DataBaseOfApp.db")
        cur = self.con.cursor()
        self.combo_filtr.addItems(
            [
                i[0]
                for i in cur.execute("SELECT DISTINCT Предмет FROM Формулы").fetchall()
                if i[0] != "Нет"
            ]
        )
        self.combo_filtr.addItem("Нет")
        self.btn_search.clicked.connect(self.psh_search)
        self.btn_add.clicked.connect(
            lambda: self.psh_add(
                self.line_name.text(), self.line_theorem.text(), self.line_subj.text()
            )
        )
        self.btn_save.clicked.connect(self.psh_save)
        self.btn_del.clicked.connect(self.psh_del)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.btn_search.click()

    def psh_search(self):
        cur = self.con.cursor()
        if self.combo_filtr.currentText() == "Нет":
            if self.line_search.text():
                res = cur.execute(
                    f"""SELECT id, Название, Формула FROM Формулы WHERE Название = '{self.line_search.text()}' """
                ).fetchall()
            else:
                res = cur.execute(
                    f"""SELECT id, Название, Формула FROM Формулы"""
                ).fetchall()
        else:
            if self.line_search.text():
                res = cur.execute(
                    f"""SELECT id, Название, Формула FROM Формулы WHERE Название = '{self.line_search.text()}' AND Предмет = '{str(self.combo_filtr.currentText())}' """
                ).fetchall()
            else:
                res = cur.execute(
                    f"""SELECT id, Название, Формула FROM Формулы WHERE Предмет = '{str(self.combo_filtr.currentText())}' """
                ).fetchall()
        if res:
            self.tableWidget.setRowCount(len(res))
            self.tableWidget.setColumnCount(len(res[0]))
            for i, elem in enumerate(res):
                for j, vol in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(vol)))
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("Ничего не найдено! Попробуйте снова.")
            msg_box.exec()

    def psh_add(self, name, formul, subject):
        if not self.line_name.text():
            name = "Формула"
        if not self.line_theorem.text():
            formul = "Не добавлено"
        if not self.line_subj.text():
            subject = "Нет"
        valid = QMessageBox.question(
            self,
            "",
            f"Действительно добавить элемент {str(name)}?",
            QMessageBox.Yes,
            QMessageBox.No,
        )
        cur = self.con.cursor()
        if valid == QMessageBox.Yes:
            cur.execute(
                f"""INSERT INTO Формулы (Название, Формула, Предмет) VALUES ('{str(name)}', '{str(formul)}', '{str(subject)}')"""
            )

    def psh_save(self):
        self.con.commit()

    def psh_del(self):
        cur = self.con.cursor()
        ids = cur.execute(f"""SELECT id FROM Формулы""").fetchall()
        ids = [str(i)[1:-2] for i in ids]
        if not self.line_del.text().isdigit():
            self.line_del.setText("")
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("id это число")
            msg_box.exec()
        elif self.line_del.text() not in ids:
            self.line_del.setText("")
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("Такого id нет!")
            msg_box.exec()
        elif self.line_del.text():
            name = cur.execute(
                f"""SELECT DISTINCT Название FROM Формулы WHERE id={int(self.line_del.text())}"""
            ).fetchall()
            valid = QMessageBox.question(
                self,
                "",
                f"Действительно удалить элемент {name[:][0][0][:]}?",
                QMessageBox.Yes,
                QMessageBox.No,
            )
            if valid == QMessageBox.Yes:
                cur.execute(
                    f"""DELETE FROM Формулы WHERE id = {int(self.line_del.text())}"""
                )


class Graphs(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init()

    def initUI(self):
        f = io.StringIO(template_of_graphs.template_of_graphs)
        uic.loadUi(f, self)

    def init(self):
        self.pushButton.clicked.connect(self.do_graph)
        self.btn_open.clicked.connect(self.btn_op)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.pushButton.click()

    def do_graph(self):
        doing = self.normal_function(self.lineEdit.text())
        if "x" not in doing:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("Введите функцию типа y = x!")
            msg_box.exec()
        else:
            if self.lineEdit.text():
                fig, ax = plt.subplots()
                ax.set_title(f"График {self.lineEdit.text()}")
                ax.set_xlabel("x")
                ax.set_ylabel("y")
                ax.grid()
                x = np.linspace(-100, 100, 1000)
                flag = False
                if doing == "x":
                    y = x
                else:
                    try:
                        y = eval(doing)
                    except NameError:
                        self.lineEdit.setText("")
                        flag = True
                        msg_box = QMessageBox()
                        msg_box.setWindowTitle("Ошибка")
                        msg_box.setText("Введите функцию типа y = x!")
                        msg_box.exec()
                    except SyntaxError:
                        self.lineEdit.setText("")
                        flag = True
                        msg_box = QMessageBox()
                        msg_box.setWindowTitle("Ошибка")
                        msg_box.setText("Вводите только математические действия!")
                        msg_box.exec()
                    except ValueError:
                        self.lineEdit.setText("")
                        flag = True
                        msg_box = QMessageBox()
                        msg_box.setWindowTitle("Ошибка")
                        msg_box.setText("Вводите только математические действия!")
                        msg_box.exec()
                    except TypeError:
                        self.lineEdit.setText("")
                        flag = True
                        msg_box = QMessageBox()
                        msg_box.setWindowTitle("Ошибка")
                        msg_box.setText(
                            "Не используй log(), sin(), cos() и т.д., пожалуйста, моя программа так пока что не умеет..."
                        )
                        msg_box.exec()
                if not flag:
                    ax.plot(x, y)
                    plt.show()
            else:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Ошибка")
                msg_box.setText("Сначала введите функцию!")
                msg_box.exec()

    def btn_op(self):
        fname = QFileDialog.getOpenFileName(
            self, "Выбрать картинку", "", "Картинка (*.png);;Все файлы (*)"
        )[0]
        self.pixmap = QPixmap(fname)
        self.label_img.setPixmap(self.pixmap)

    def normal_function(self, function: str):
        flag = False
        li = []
        for i in function:
            if flag:
                li.append(i)
            if i == "=":
                flag = True
        doing = "".join(li)
        return doing


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
