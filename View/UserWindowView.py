from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog
from View.UserWindow import Ui_UserWindow
from Interfase.IObserver import Observer


class UserWindowView(QDialog):
    __metaclass__ = Observer

    def __init__(self, controller, model):
        super(QDialog, self).__init__()

        self.__model = model
        self.__controller = controller
        self.__ui = Ui_UserWindow()
        self.__ui.setupUi(self)

        self.__model.attach(self)

        self.__ui.Name.editingFinished.connect(self.__controller.set_login)
        self.__ui.Password.editingFinished.connect(self.__controller.set_password)
        self.__ui.Name_2.editingFinished.connect(self.__controller.set_name_2)
        self.__ui.Sename.editingFinished.connect(self.__controller.set_sename)
        self.__ui.MIdname.editingFinished.connect(self.__controller.set_midname)
        self.__ui.Type.editingFinished.connect(self.__controller.set_type)
        self.__ui.Mail.editingFinished.connect(self.__controller.set_mail)
        self.__ui.Phone.editingFinished.connect(self.__controller.set_phone)
        self.__ui.Comment.editingFinished.connect(self.__controller.set_comment)
        self.__ui.Class.editingFinished.connect(self.__controller.set_class)
        self.__ui.TypeClass.editingFinished.connect(self.__controller.set_type_class)

        self.__ui.del_btn.clicked.connect(self.__controller.delate)
        self.__ui.ins_btn.clicked.connect(self.__controller.insert)
        self.__ui.edt_btn.clicked.connect(self.__controller.update)

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
            self.__ui.table_bilet.setRowCount(0)
            for i, row in enumerate(self.__model.bilet_user):
                self.__ui.table_bilet.setRowCount(self.__ui.table_bilet.rowCount() + 1)
                model = row.get_list_interfase()
                model = [model[3], model[2], model[4]]
                for j, elem in enumerate(model):
                    self.__ui.table_bilet.setItem(i, j, QTableWidgetItem(elem))
        except Exception:
            pass

        self.__ui.Name.setText(self.__model.login)
        self.__ui.Password.setText(self.__model.password)
        self.__ui.Name_2.setText(self.__model.name)
        self.__ui.Sename.setText(self.__model.sename)
        self.__ui.MIdname.setText(self.__model.midname)
        self.__ui.Type.setText(self.__model.type)
        self.__ui.Mail.setText(self.__model.email)
        self.__ui.Phone.setText(self.__model.phone)
        self.__ui.Comment.setText(self.__model.comment)
        self.__ui.Class.setText(str(self.__model._class))
        self.__ui.TypeClass.setText(self.__model.class_type)
