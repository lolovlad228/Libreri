import sys
from PyQt5.QtWidgets import QApplication
from View.LoginView import LoginView
from Class.DataContext import DataContext
from Model.MainWindowModel import MainWindowModel
from Controller.MainWindowController import MainWindowController


class LoginController:

    def __init__(self, model):
        self.__model = model
        self.__view = LoginView(self, self.__model)
        self.__view.show()

    def set_mail(self):
        mail = self.__view.ui.lineEdit.text()
        self.__model.mail = mail

    def set_password(self):
        password = self.__view.ui.lineEdit_2.text()
        self.__model.password = password

    def login(self):
        users = DataContext().User.load()
        mail = users.where(lambda x: x.email == self.__model.mail).first_of_default()
        if mail is not False:
            password = users.where(lambda x: x.password == self.__model.password).first_of_default()
            if password is not False:
                model = MainWindowModel()
                controller = MainWindowController(model)
                self.__view.close()
            else:
                self.__model.error = "Неправельный пароль"
        else:
            self.__model.error = "неправельная почта"

