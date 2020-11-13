from Class.DataContext import DataContext
from Interfase.IObserver import Subject
from Model.DataModel.User import User
from Model.DataModel.Book import Book


class RegWindowModel(Subject):
    def __init__(self):
        self.__select_user = User([1, "", "", "", "", "", "", "", "", "", "", ""])
        self.users = DataContext().User.load().list_model()
        self.__list_book = []
        self.__search_sename = ""

        self.__observers = []

    @property
    def select_user(self):
        return self.__select_user

    @property
    def list_book(self):
        return self.__list_book

    @property
    def search_sename(self):
        return self.__search_sename

    @search_sename.setter
    def search_sename(self, val):
        self.__search_sename = val
        self.notify()

    @select_user.setter
    def select_user(self, val):
        self.__select_user = val
        self.__search_sename = val.sename
        self.notify()

    @list_book.setter
    def list_book(self, val):
        self.__list_book = val
        self.notify()

    def detach(self, observer):
        self.__observers.remove(observer)

    def notify(self):
        for i in self.__observers:
            i.update()

    def attach(self, observer):
        self.__observers.append(observer)