# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserWindow(object):
    def setupUi(self, UserWindow):
        UserWindow.setObjectName("UserWindow")
        UserWindow.resize(1042, 596)
        self.horizontalLayout = QtWidgets.QHBoxLayout(UserWindow)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(UserWindow)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.verticalLayout.addWidget(self.table_user)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.Name = QtWidgets.QLineEdit(self.frame_3)
        self.Name.setObjectName("Name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Name)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.Password = QtWidgets.QLineEdit(self.frame_3)
        self.Password.setObjectName("Password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Password)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.Name_2 = QtWidgets.QLineEdit(self.frame_3)
        self.Name_2.setObjectName("Name_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Name_2)
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.Sename = QtWidgets.QLineEdit(self.frame_3)
        self.Sename.setObjectName("Sename")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Sename)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.MIdname = QtWidgets.QLineEdit(self.frame_3)
        self.MIdname.setObjectName("MIdname")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.MIdname)
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.Type = QtWidgets.QLineEdit(self.frame_3)
        self.Type.setObjectName("Type")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Type)
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.Mail = QtWidgets.QLineEdit(self.frame_3)
        self.Mail.setObjectName("Mail")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.Mail)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.Phone = QtWidgets.QLineEdit(self.frame_3)
        self.Phone.setObjectName("Phone")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.Phone)
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.Comment = QtWidgets.QLineEdit(self.frame_3)
        self.Comment.setObjectName("Comment")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.Comment)
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.Class = QtWidgets.QLineEdit(self.frame_3)
        self.Class.setObjectName("Class")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.Class)
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.TypeClass = QtWidgets.QLineEdit(self.frame_3)
        self.TypeClass.setObjectName("TypeClass")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.TypeClass)
        self.horizontalLayout_2.addLayout(self.formLayout)
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setMinimumSize(QtCore.QSize(209, 0))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.del_btn = QtWidgets.QPushButton(self.frame_4)
        self.del_btn.setObjectName("del_btn")
        self.verticalLayout_2.addWidget(self.del_btn)
        self.ins_btn = QtWidgets.QPushButton(self.frame_4)
        self.ins_btn.setObjectName("ins_btn")
        self.verticalLayout_2.addWidget(self.ins_btn)
        self.edt_btn = QtWidgets.QPushButton(self.frame_4)
        self.edt_btn.setObjectName("edt_btn")
        self.verticalLayout_2.addWidget(self.edt_btn)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(UserWindow)
        self.frame_2.setMinimumSize(QtCore.QSize(471, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.table_bilet = QtWidgets.QTableWidget(self.frame_2)
        self.table_bilet.setGeometry(QtCore.QRect(15, 11, 441, 571))
        self.table_bilet.setObjectName("table_bilet")
        self.table_bilet.setColumnCount(3)
        self.table_bilet.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_bilet.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_bilet.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_bilet.setHorizontalHeaderItem(2, item)
        self.horizontalLayout.addWidget(self.frame_2)

        self.retranslateUi(UserWindow)
        QtCore.QMetaObject.connectSlotsByName(UserWindow)

    def retranslateUi(self, UserWindow):
        _translate = QtCore.QCoreApplication.translate
        UserWindow.setWindowTitle(_translate("UserWindow", "Dialog"))
        item = self.table_user.horizontalHeaderItem(0)
        item.setText(_translate("UserWindow", "ID"))
        item = self.table_user.horizontalHeaderItem(1)
        item.setText(_translate("UserWindow", "Логин"))
        item = self.table_user.horizontalHeaderItem(2)
        item.setText(_translate("UserWindow", "Пароль"))
        item = self.table_user.horizontalHeaderItem(3)
        item.setText(_translate("UserWindow", "Имя"))
        item = self.table_user.horizontalHeaderItem(4)
        item.setText(_translate("UserWindow", "Фамилия"))
        item = self.table_user.horizontalHeaderItem(5)
        item.setText(_translate("UserWindow", "Очество"))
        item = self.table_user.horizontalHeaderItem(6)
        item.setText(_translate("UserWindow", "Тип"))
        item = self.table_user.horizontalHeaderItem(7)
        item.setText(_translate("UserWindow", "Почта"))
        item = self.table_user.horizontalHeaderItem(8)
        item.setText(_translate("UserWindow", "Телефон"))
        item = self.table_user.horizontalHeaderItem(9)
        item.setText(_translate("UserWindow", "Коментарии"))
        item = self.table_user.horizontalHeaderItem(10)
        item.setText(_translate("UserWindow", "Класс"))
        item = self.table_user.horizontalHeaderItem(11)
        item.setText(_translate("UserWindow", "ТипКласса"))
        self.label.setText(_translate("UserWindow", "Логин"))
        self.label_6.setText(_translate("UserWindow", "Пароль"))
        self.label_2.setText(_translate("UserWindow", "Имя"))
        self.label_7.setText(_translate("UserWindow", "Фамилия"))
        self.label_3.setText(_translate("UserWindow", "Очество"))
        self.label_8.setText(_translate("UserWindow", "Тип"))
        self.label_9.setText(_translate("UserWindow", "Почта"))
        self.label_4.setText(_translate("UserWindow", "Телефон"))
        self.label_10.setText(_translate("UserWindow", "Соментарий"))
        self.label_5.setText(_translate("UserWindow", "Класс"))
        self.label_11.setText(_translate("UserWindow", "Буква Класса"))
        self.del_btn.setText(_translate("UserWindow", "Удалить"))
        self.ins_btn.setText(_translate("UserWindow", "Добавить"))
        self.edt_btn.setText(_translate("UserWindow", "Сохранить"))
        item = self.table_bilet.horizontalHeaderItem(0)
        item.setText(_translate("UserWindow", "Имя пользователя"))
        item = self.table_bilet.horizontalHeaderItem(1)
        item.setText(_translate("UserWindow", "Название книги"))
        item = self.table_bilet.horizontalHeaderItem(2)
        item.setText(_translate("UserWindow", "Дата выдачи"))
