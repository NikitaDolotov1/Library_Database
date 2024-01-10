from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow
import sys

sys.path.append("../../../src")
from client.ui.ui_login_form import Ui_MainWindow as Ui_LoginForm
from .user_list import UserList
from .main_form import MainForm
from .base_worker import BaseWorker, Login, User


class LoginForm(QMainWindow, Ui_LoginForm):
    login_correct = pyqtSignal(int, int)
    main_window: QMainWindow

    def __init__(self, base_worker: BaseWorker):
        super().__init__()
        self.base_worker = base_worker
        self.setupUi(self)
        self.btn_vhod.clicked.connect(self.check_login)
        self.btn_cancel.clicked.connect(self.exit)

    def check_login(self):
        user = self.base_worker.check_user_login(User(login=self.line_login.text(), password=self.line_password.text()))
        if not user.user_id:
            self.L_error.setVisible(True)
            return
        else:
            self.start_main_window(user)

    def start_main_window(self, login: Login):
        if login.role_id == 1:
            self.main_window = UserList(self.base_worker, login)

        else:
            self.main_window = MainForm(self.base_worker, login)

        self.main_window.show()
        self.close()

    def exit(self):
        self.close()
