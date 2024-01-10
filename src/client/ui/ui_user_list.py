# Form implementation generated from reading ui file 'ui/user_list.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 704)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineLogin = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineLogin.setObjectName("lineLogin")
        self.horizontalLayout.addWidget(self.lineLogin)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.linePassword = QtWidgets.QLineEdit(parent=self.groupBox)
        self.linePassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.linePassword.setObjectName("linePassword")
        self.horizontalLayout_2.addWidget(self.linePassword)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.cbRole = QtWidgets.QComboBox(parent=self.groupBox)
        self.cbRole.setObjectName("cbRole")
        self.horizontalLayout_3.addWidget(self.cbRole)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAdd = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnAdd.setObjectName("btnAdd")
        self.verticalLayout.addWidget(self.btnAdd)
        self.btnReset = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnReset.setObjectName("btnReset")
        self.verticalLayout.addWidget(self.btnReset)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.table_user_list = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.table_user_list.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_user_list.setAlternatingRowColors(True)
        self.table_user_list.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.table_user_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_user_list.setObjectName("table_user_list")
        self.table_user_list.setColumnCount(3)
        self.table_user_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_user_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_user_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_user_list.setHorizontalHeaderItem(2, item)
        self.table_user_list.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_4.addWidget(self.table_user_list)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnDelete = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.btnDelete.setObjectName("btnDelete")
        self.verticalLayout_3.addWidget(self.btnDelete)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Список пользователей"))
        self.groupBox.setTitle(_translate("MainWindow", "Пользователь"))
        self.label.setText(_translate("MainWindow", "Логин"))
        self.label_2.setText(_translate("MainWindow", "Пароль"))
        self.label_3.setText(_translate("MainWindow", "Роль"))
        self.btnAdd.setText(_translate("MainWindow", "Добавить"))
        self.btnReset.setText(_translate("MainWindow", "Очистить"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Список пользователей"))
        item = self.table_user_list.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.table_user_list.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Логин"))
        item = self.table_user_list.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ID_Роли"))
        self.btnDelete.setText(_translate("MainWindow", "Удалить"))
