# Form implementation generated from reading ui file 'ui/main_form.ui'
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
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.cb_BookName = QtWidgets.QComboBox(parent=self.groupBox)
        self.cb_BookName.setObjectName("cb_BookName")
        self.horizontalLayout.addWidget(self.cb_BookName)
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineDateOut = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineDateOut.setObjectName("lineDateOut")
        self.horizontalLayout.addWidget(self.lineDateOut)
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineDateIN = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineDateIN.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineDateIN.setObjectName("lineDateIN")
        self.horizontalLayout.addWidget(self.lineDateIN)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAdd = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnAdd.setObjectName("btnAdd")
        self.verticalLayout.addWidget(self.btnAdd)
        self.btnReset = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnReset.setObjectName("btnReset")
        self.verticalLayout.addWidget(self.btnReset)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.table_book_out = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.table_book_out.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_book_out.setAlternatingRowColors(True)
        self.table_book_out.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.table_book_out.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_book_out.setObjectName("table_book_out")
        self.table_book_out.setColumnCount(4)
        self.table_book_out.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_book_out.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_book_out.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_book_out.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_book_out.setHorizontalHeaderItem(3, item)
        self.table_book_out.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_4.addWidget(self.table_book_out)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Список выдачей"))
        self.label_3.setText(_translate("MainWindow", "Название книги"))
        self.label.setText(_translate("MainWindow", "Дата выдачи"))
        self.label_2.setText(_translate("MainWindow", "Дата возврата"))
        self.btnAdd.setText(_translate("MainWindow", "Добавить"))
        self.btnReset.setText(_translate("MainWindow", "Очистить"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Список выдачей"))
        item = self.table_book_out.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.table_book_out.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "id книги"))
        item = self.table_book_out.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дата выдачи"))
        item = self.table_book_out.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Дата возврата"))
