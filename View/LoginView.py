from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from View.Login import Ui_LoginWindow
from Interfase.IObserver import Observer


class LoginView(QMainWindow):
    __metaclass__ = Observer

    def __init__(self, controller, model):
        super(QMainWindow, self).__init__()

        self.__model = model
        self.__controller = controller
        self.__ui = Ui_LoginWindow()
        self.__ui.setupUi(self)

        self.__model.attach(self)

        # connect widgets to controller
        self.__ui.lineEdit.editingFinished.connect(self.__controller.set_mail)
        self.__ui.lineEdit_2.editingFinished.connect(self.__controller.set_password)

        self.__ui.pushButton.clicked.connect(self.__controller.login)

    @property
    def ui(self):
        return self.__ui

    def update(self):
        self.__ui.error_lb.setText(self.__model.error)
