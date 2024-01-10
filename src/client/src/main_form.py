import sys
sys.path.append("../../../src")


from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt6.QtCore import pyqtSignal
from client.ui.ui_main_form import Ui_MainWindow as Ui_MainForm
from .base_worker import BaseWorker, User, Login, Books_out

class MainForm(QMainWindow, Ui_MainForm):
    def __init__(self, base_worker: BaseWorker, login: Login):
        super().__init__()
        self.setupUi(self)
        self.login = login
        self.base_worker = base_worker
        self.load_booksName()
        self.load_books_out()
        self.btnAdd.clicked.connect(self.add_new_books_out)
        self.btnReset.clicked.connect(self.reset_booksOut)
        self.show()

    def load_books_out(self) -> None:
        row = 0
        self.table_book_out.setRowCount(0)
        books = self.base_worker.get_books_out_list()
        for book in books:
            self.table_book_out.insertRow(row)
            self.table_book_out.setItem(row, 0, QTableWidgetItem(str(book.id)))
            self.table_book_out.setItem(row, 1, QTableWidgetItem(str(book.id_book)))
            self.table_book_out.setItem(row, 2, QTableWidgetItem(str(book.date_out)))
            self.table_book_out.setItem(row, 3, QTableWidgetItem(str(book.date_in)))
            self.table_book_out.resizeColumnsToContents()
            self.table_book_out.horizontalHeader().setStretchLastSection(True)
            row += 1

    def reset_booksOut(self) -> None:
        self.cb_BookName.setCurrentIndex(0)
        self.lineDateOut.setText('')
        self.lineDateIN.setText('')

    def load_booksName(self) -> None:
        books = self.base_worker.get_booksName()
        self.cb_BookName.addItem('-')
        for book in books:
            self.cb_BookName.addItem(book.name_book, book.id)

    def add_new_books_out(self) -> None:
        if not self.check_books_out_fields():
            return

        book = Books_out(id_book=self.cb_BookName.currentData(), date_out=self.lineDateOut.text(), date_in=self.lineDateIN.text())
        res = self.base_worker.add_new_books_out(book)
        self.load_books_out()
        print(res)

    def check_books_out_fields(self) -> bool:
        if self.cb_BookName.currentIndex() != 0 and self.lineDateOut.text() != '' and self.lineDateIN.text() != '':
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "Все поля должны быть заполнены")
            return False

