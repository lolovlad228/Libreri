from Class.DataContext import DataContext
from Interfase.IObserver import Subject
from Model.DataModel.Book import Book
import qrcode
from pyodbc import Binary


class MainWindowModel(Subject):
    def __init__(self):
        self.__name = ""
        self.__author = ""
        self.__data = ""
        self.__number = ""
        self.__state = ""
        self.__photo = ""
        self.__photo_qr = ""

        self.__select_book = Book([1, "", "", "", "", "", ""])

        self.books = DataContext().Book.load().list_model()

        self.__observers = []

    @property
    def photo_qr(self):
        return self.__photo_qr

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    @property
    def data(self):
        return self.__data

    @property
    def number(self):
        return self.__number

    @property
    def state(self):
        return self.__state

    @property
    def photo(self):
        return self.__photo

    @property
    def select_book(self):
        return self.__select_book

    @select_book.setter
    def select_book(self, val):
        self.__select_book = val
        self.name = val.name
        self.author = val.author
        self.data = val.data
        self.number = val.number
        self.state = val.state
        self.photo = val.photo
        self.photo_qr = qrcode.make("{Number: " + str(val.number) + "}")
        self.notify()

    @photo_qr.setter
    def photo_qr(self, val):
        self.__photo_qr = val

    @name.setter
    def name(self, val):
        self.__name = val
        self.__select_book.name = val

    @author.setter
    def author(self, val):
        self.__author = val
        self.__select_book.author = val

    @photo.setter
    def photo(self, val):
        self.__photo = val if val is not None else None
        self.__select_book.photo = val if val is not None else None
        self.notify()

    @data.setter
    def data(self, val):
        self.__data = val
        self.__select_book.data = val

    @number.setter
    def number(self, val):
        self.__number = val
        self.__select_book.number = val

    @state.setter
    def state(self, val):
        self.__state = val
        self.__select_book.state = val

    def detach(self, observer):
        self.__observers.remove(observer)

    def notify(self):
        for i in self.__observers:
            i.update()

    def attach(self, observer):
        self.__observers.append(observer)