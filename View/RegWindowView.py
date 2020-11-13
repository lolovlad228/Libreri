from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog
from PyQt5 import QtWidgets
from View.RegWindow import Ui_Regestration
from Interfase.IObserver import Observer


class RegWindowView(QDialog):
    __metaclass__ = Observer

    def __init__(self, controller, model):
        super(QDialog, self).__init__()

        self.__model = model
        self.__controller = controller
        self.__ui = Ui_Regestration()
        self.__ui.setupUi(self)

        self.__model.attach(self)

        self.__ui.lineEdit.editingFinished.connect(self.__controller.set_sename)
        self.__ui.search.clicked.connect(self.__controller.search)
        self.__ui.load_book.clicked.connect(self.__controller.load_book)
        self.__ui.load_list_book.clicked.connect(self.__controller.load_list_book)

        self.__ui.table_user.itemClicked.connect(self.__controller.item_changed)

        self.update()

    @property
    def ui(self):
        return self.__ui

    def update(self):
        self.__ui.table_user.setRowCount(0)
        for i, row in enumerate(self.__model.users):
            self.__ui.table_user.setRowCount(self.__ui.table_user.rowCount() + 1)
            for j, elem in enumerate(row.get_list_interfase()):
                self.__ui.table_user.setItem(i, j, QTableWidgetItem(elem))
        try:
            self.__ui.table_book.setRowCount(0)
            for i, row in enumerate(self.__model.list_book):
                self.__ui.table_book.setRowCount(self.__ui.table_book.rowCount() + 1)
                model = row.get_list_interfase()
                for j, elem in enumerate(model):
                    self.__ui.table_book.setItem(i, j, QTableWidgetItem(elem))
        except Exception:
            pass

        self.__ui.lineEdit.setText(self.__model.search_sename)

