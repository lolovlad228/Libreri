from functools import partial

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog
from View.MainWindow import Ui_Dialog
from Interfase.IObserver import Observer


class MainWindowView(QDialog):
    __metaclass__ = Observer

    def __init__(self, controller, model):
        super(QDialog, self).__init__()

        self.__model = model
        self.__controller = controller
        self.__ui = Ui_Dialog()
        self.__ui.setupUi(self)

        self.__model.attach(self)

        self.__ui.Name.editingFinished.connect(self.__controller.set_name)
        self.__ui.Author.editingFinished.connect(self.__controller.set_author)
        self.__ui.Date.editingFinished.connect(self.__controller.set_data)
        self.__ui.Number.editingFinished.connect(self.__controller.set_number)
        self.__ui.State.editingFinished.connect(self.__controller.set_state)

        self.__ui.del_btn.clicked.connect(self.__controller.delate)
        self.__ui.ins_btn.clicked.connect(self.__controller.insert)
        self.__ui.upd_btn.clicked.connect(self.__controller.update)

        self.__ui.stu_btn.clicked.connect(self.__controller.student)
        self.__ui.reg_str.clicked.connect(self.__controller.registration)
        self.__ui.dop_info.clicked.connect(partial(self.__controller.dop_info, model))

        self.__ui.table_book.itemClicked.connect(self.__controller.item_changed)

        self.update()

    @property
    def ui(self):
        return self.__ui

    def update(self):
        self.__ui.table_book.setRowCount(0)
        for i, row in enumerate(self.__model.books):
            self.__ui.table_book.setRowCount(self.__ui.table_book.rowCount() + 1)
            for j, elem in enumerate(row.get_list_interfase()[:6]):
                self.__ui.table_book.setItem(i, j, QTableWidgetItem(elem))

        self.__ui.Name.setText(self.__model.name)
        self.__ui.Author.setText(self.__model.author)
        self.__ui.Date.setText(str(self.__model.data))
        self.__ui.State.setText(self.__model.state)
        self.__ui.Number.setText(str(self.__model.number))
