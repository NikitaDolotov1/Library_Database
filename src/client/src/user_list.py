import sys

sys.path.append("../../../src")

from typing import List

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from client.ui.ui_user_list import Ui_MainWindow as Ui_UserList
from .base_worker import BaseWorker, Login, User



class UserList(QMainWindow, Ui_UserList):
    def __init__(self, base_worker: BaseWorker, login: Login):
        super().__init__()
        self.setupUi(self)
        self.login = login
        self.base_worker = base_worker
        self.load_roles()
        self.load_users()
        self.btnReset.clicked.connect(self.reset_users)
        self.btnAdd.clicked.connect(self.add_new_user)
        self.btnDelete.clicked.connect(self.delete_user)
        self.show()

    def load_roles(self) -> None:
        roles = self.base_worker.get_roles_list()
        self.cbRole.addItem('-')
        for role in roles:
            self.cbRole.addItem(role.role_name, role.role_id)

    def load_users(self) -> None:
        row = 0
        self.table_user_list.setRowCount(0)
        users = self.base_worker.get_users_list()
        for user in users:
            self.table_user_list.insertRow(row)
            self.table_user_list.setItem(row, 0, QTableWidgetItem(str(user.user_id)))
            self.table_user_list.setItem(row, 1, QTableWidgetItem(str(user.login)))
            self.table_user_list.setItem(row, 2, QTableWidgetItem(str(user.role_id)))
            self.table_user_list.resizeColumnsToContents()
            self.table_user_list.horizontalHeader().setStretchLastSection(True)
            row += 1

    def reset_users(self) -> None:
        self.lineLogin.setText('')
        self.linePassword.setText('')
        self.cbRole.setCurrentIndex(0)

    def add_new_user(self) -> None:
        if not self.check_user_fields():
            return

        user = User(login=self.lineLogin.text(), password=self.linePassword.text(), role_id=self.cbRole.currentData())
        res = self.base_worker.add_new_user(user)
        self.load_users()
        print(res)

    def check_user_fields(self) -> bool:
        if self.lineLogin.text() != '' and self.linePassword.text() != '' and self.cbRole.currentIndex() != 0:
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "Все поля должны быть заполнены")
            return False

    def check_admin(self, role_id):
        if role_id == "1":
            QMessageBox.information(self, "Ошибка", "Этого пользователя удалить нельзя")
            return True
        return False

    def delete_user(self):

        if not self.table_user_list.selectionModel().hasSelection():
            return

        role_id = self.table_user_list.item(self.table_user_list.currentRow(), 2).text()
        user_id = self.table_user_list.item(self.table_user_list.currentRow(), 0).text()

        if self.check_admin(role_id):
            return


        answer = QMessageBox.question(self, "Удаление пользователя", "Вы действительно хотите удалить выбранного "
                                                                     "пользователя?")

        if answer == QMessageBox.StandardButton.No:
            return

        resp = self.base_worker.delete_user(user_id)
        print(resp)
        self.load_users()

