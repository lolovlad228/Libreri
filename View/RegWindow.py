# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Regestration(object):
    def setupUi(self, Regestration):
        Regestration.setObjectName("Regestration")
        Regestration.resize(1129, 599)
        self.verticalLayout = QtWidgets.QVBoxLayout(Regestration)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(Regestration)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 90))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.load_book = QtWidgets.QPushButton(self.frame_2)
        self.load_book.setGeometry(QtCore.QRect(740, 20, 221, 51))
        self.load_book.setObjectName("load_book")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(60, 20, 371, 53))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.search = QtWidgets.QPushButton(self.widget)
        self.search.setObjectName("search")
        self.verticalLayout_2.addWidget(self.search)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(Regestration)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.table_user = QtWidgets.QTableWidget(self.frame)
        self.table_user.setObjectName("table_user")
        self.table_user.setColumnCount(12)
        self.table_user.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_user.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_user.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_user.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_user.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_user.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_user.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_user.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_user.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_user.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_user.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_user.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_user.setHorizontalHeaderItem(11, item)
        self.horizontalLayout.addWidget(self.table_user)
        self.table_book = QtWidgets.QTableWidget(self.frame)
        self.table_book.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.table_book.setWordWrap(True)
        self.table_book.setRowCount(0)
        self.table_book.setColumnCount(6)
        self.table_book.setObjectName("table_book")
        item = QtWidgets.QTableWidgetItem()
        self.table_book.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_book.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_book.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_book.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_book.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_book.setHorizontalHeaderItem(5, item)
        self.horizontalLayout.addWidget(self.table_book)
        self.verticalLayout.addWidget(self.frame)
        self.load_list_book = QtWidgets.QPushButton(Regestration)
        self.load_list_book.setMinimumSize(QtCore.QSize(0, 63))
        self.load_list_book.setObjectName("load_list_book")
        self.verticalLayout.addWidget(self.load_list_book)

        self.retranslateUi(Regestration)
        QtCore.QMetaObject.connectSlotsByName(Regestration)

    def retranslateUi(self, Regestration):
        _translate = QtCore.QCoreApplication.translate
        Regestration.setWindowTitle(_translate("Regestration", "Reg_Book"))
        self.load_book.setText(_translate("Regestration", "Загрузить книги"))
        self.search.setText(_translate("Regestration", "Найти"))
        item = self.table_user.horizontalHeaderItem(0)
        item.setText(_translate("Regestration", "ID"))
        item = self.table_user.horizontalHeaderItem(1)
        item.setText(_translate("Regestration", "Логин"))
        item = self.table_user.horizontalHeaderItem(2)
        item.setText(_translate("Regestration", "Пароль"))
        item = self.table_user.horizontalHeaderItem(3)
        item.setText(_translate("Regestration", "Имя"))
        item = self.table_user.horizontalHeaderItem(4)
        item.setText(_translate("Regestration", "Фамилия"))
        item = self.table_user.horizontalHeaderItem(5)
        item.setText(_translate("Regestration", "Очество"))
        item = self.table_user.horizontalHeaderItem(6)
        item.setText(_translate("Regestration", "Тип"))
        item = self.table_user.horizontalHeaderItem(7)
        item.setText(_translate("Regestration", "Почта"))
        item = self.table_user.horizontalHeaderItem(8)
        item.setText(_translate("Regestration", "Телефон"))
        item = self.table_user.horizontalHeaderItem(9)
        item.setText(_translate("Regestration", "Коментарии"))
        item = self.table_user.horizontalHeaderItem(10)
        item.setText(_translate("Regestration", "Класс"))
        item = self.table_user.horizontalHeaderItem(11)
        item.setText(_translate("Regestration", "ТипКласса"))
        item = self.table_book.horizontalHeaderItem(0)
        item.setText(_translate("Regestration", "Id"))
        item = self.table_book.horizontalHeaderItem(1)
        item.setText(_translate("Regestration", "Название"))
        item = self.table_book.horizontalHeaderItem(2)
        item.setText(_translate("Regestration", "Автор"))
        item = self.table_book.horizontalHeaderItem(3)
        item.setText(_translate("Regestration", "Дата поступления"))
        item = self.table_book.horizontalHeaderItem(4)
        item.setText(_translate("Regestration", "Номер"))
        item = self.table_book.horizontalHeaderItem(5)
        item.setText(_translate("Regestration", "Статус"))
        self.load_list_book.setText(_translate("Regestration", "Загрузить"))
