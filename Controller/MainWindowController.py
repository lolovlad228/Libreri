from Model.DataModel.Book import Book
from View.MainWindowView import MainWindowView
from Class.DataContext import DataContext
from Model.UserWindowModel import UserWindowModel
from Model.RegWindowModel import RegWindowModel
from Controller.UserWindowController import UserWindowController
from Controller.RegWindowController import RegWindowController
from Controller.DopInfoController import DopInfoController


class MainWindowController:
    def __init__(self, model):
        self.__model = model
        self.__view = MainWindowView(self, self.__model)
        self.__view.show()

    def set_name(self):
        name = self.__view.ui.Name.text()
        self.__model.name = name

    def set_author(self):
        author = self.__view.ui.Author.text()
        self.__model.author = author

    def set_data(self):
        data = self.__view.ui.Date.text()
        self.__model.data = data

    def set_number(self):
        number = self.__view.ui.Number.text()
        self.__model.number = number

    def set_state(self):
        state = self.__view.ui.State.text()
        self.__model.state = state

    def delate(self):
        self.__model.books = DataContext().Book.delite(self.__model.select_book).save_change().load().list_model()
        self.__model.select_book = Book(["", "", "", "", "", "", ""])

    def insert(self):
        self.__model.books = DataContext().Book.add(self.__model.select_book).save_change().load().list_model()
        self.__model.select_book = Book(["", "", "", "", "", "", ""])

    def update(self):
        self.__model.books = DataContext().Book.update(self.__model.select_book).save_change().load().list_model()
        self.__model.select_book = Book(["", "", "", "", "", "", ""])

    def item_changed(self, item):
        row = item.row()
        self.__view.ui.table_book.selectRow(row)
        self.__model.select_book = DataContext().Book.list_model()[row]

    def student(self):
        model = UserWindowModel()
        controller = UserWindowController(model)

    def registration(self):
        model = RegWindowModel()
        controller = RegWindowController(model)

    def exit(self):
        pass

    def dop_info(self, model):
        controller = DopInfoController(model)