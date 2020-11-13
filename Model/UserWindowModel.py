from Class.DataContext import DataContext
from Interfase.IObserver import Subject
from Model.DataModel.User import User
from Model.DataModel.Book import Book


class UserWindowModel(Subject):
    def __init__(self):
        self.__login = ""
        self.__password = ""
        self.__name = ""
        self.__sename = ""
        self.__midname = ""
        self.__type = ""
        self.__email = ""
        self.__phone = ""
        self.__comment = ""
        self.__class = ""
        self.__class_type = ""

        self.__select_user = User([1, "", "", "", "", "", "", "", "", "", "", ""])

        self.users = DataContext().User.load().list_model()

        self.bilet_user = DataContext().Bilet.join(Book(), User(), [-4, -3, 1, 9, -1])

        self.__observers = []

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @property
    def name(self):
        return self.__name

    @property
    def sename(self):
        return self.__sename

    @property
    def midname(self):
        return self.__midname

    @property
    def type(self):
        return self.__type

    @property
    def email(self):
        return self.__email

    @property
    def phone(self):
        return self.__phone

    @property
    def comment(self):
        return self.__comment

    @property
    def _class(self):
        return self.__class

    @property
    def class_type(self):
        return self.__class_type

    @property
    def select_user(self):
        return self.__select_user

    @select_user.setter
    def select_user(self, val):
        self.__select_user = val
        self.bilet_user = DataContext().Bilet.where(lambda x: x.id_user == val.id).list_model()
        self.login = val.login
        self.password = val.password
        self.name = val.name
        self.sename = val.sename
        self.midname = val.midname
        self.type = val.type
        self.email = val.email
        self.phone = val.phone
        self.comment = val.comment
        self._class = val._class
        self.class_type = val.class_type

    @login.setter
    def login(self, val):
        self.__login = val
        self.__select_user.login = val
        self.notify()

    @password.setter
    def password(self, val):
        self.__password = val
        self.__select_user.password = val
        self.notify()

    @name.setter
    def name(self, val):
        self.__name = val
        self.__select_user.name = val
        self.notify()

    @sename.setter
    def sename(self, val):
        self.__sename = val
        self.__select_user.sename= val
        self.notify()

    @midname.setter
    def midname(self, val):
        self.__midname = val
        self.__select_user.midname = val
        self.notify()

    @type.setter
    def type(self, val):
        self.__type = val
        self.__select_user.type = val
        self.notify()

    @email.setter
    def email(self, val):
        self.__email = val
        self.__select_user.email = val
        self.notify()

    @phone.setter
    def phone(self, val):
        self.__phone = val
        self.__select_user.phone = val
        self.notify()

    @comment.setter
    def comment(self, val):
        self.__comment = val
        self.__select_user.comment = val
        self.notify()

    @_class.setter
    def _class(self, val):
        self.__class = val
        self.__select_user._class = val
        self.notify()

    @class_type.setter
    def class_type(self, val):
        self.__class_type = val
        self.__select_user.class_type = val
        self.notify()

    def detach(self, observer):
        self.__observers.remove(observer)

    def notify(self):
        for i in self.__observers:
            i.update()

    def attach(self, observer):
        self.__observers.append(observer)