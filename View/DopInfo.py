# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DopInfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dop_info(object):
    def setupUi(self, Dop_info):
        Dop_info.setObjectName("Dop_info")
        Dop_info.resize(749, 405)
        self.img_book = QtWidgets.QLabel(Dop_info)
        self.img_book.setGeometry(QtCore.QRect(40, 20, 300, 300))
        self.img_book.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.img_book.setText("")
        self.img_book.setObjectName("img_book")
        self.Load_img_book = QtWidgets.QPushButton(Dop_info)
        self.Load_img_book.setGeometry(QtCore.QRect(40, 350, 301, 23))
        self.Load_img_book.setObjectName("Load_img_book")
        self.img_qr_code = QtWidgets.QLabel(Dop_info)
        self.img_qr_code.setGeometry(QtCore.QRect(390, 20, 300, 300))
        self.img_qr_code.setStyleSheet("background-color: rgb(159, 159, 159);")
        self.img_qr_code.setText("")
        self.img_qr_code.setObjectName("img_qr_code")
        self.Load_img_qr = QtWidgets.QPushButton(Dop_info)
        self.Load_img_qr.setGeometry(QtCore.QRect(390, 350, 301, 23))
        self.Load_img_qr.setObjectName("Load_img_qr")

        self.retranslateUi(Dop_info)
        QtCore.QMetaObject.connectSlotsByName(Dop_info)

    def retranslateUi(self, Dop_info):
        _translate = QtCore.QCoreApplication.translate
        Dop_info.setWindowTitle(_translate("Dop_info", "Dialog"))
        self.Load_img_book.setText(_translate("Dop_info", "Загрузить фото"))
        self.Load_img_qr.setText(_translate("Dop_info", "Скачать qrcode"))
