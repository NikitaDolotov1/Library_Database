import sys
sys.path.append("../../src")

from PyQt6 import QtWidgets
from client.src.login_form import LoginForm
from client.src.base_worker import BaseWorker
import settings


base_worker = BaseWorker(settings.SERVER_URL)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginForm(base_worker)
    login_window.show()
    app.exec()
