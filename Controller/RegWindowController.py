from Model.DataModel.Book import Book
from Class.DataContext import DataContext
from View.RegWindowView import RegWindowView
from Class.LoadQrCode import LoadQrCode
from Model.DataModel.BilteOrig import BiletOrig
from Model.DataModel.User import User
import datetime


class RegWindowController:
    def __init__(self, model):
        self.__model = model
        self.__view = RegWindowView(self, self.__model)
        self.__view.show()

    def set_sename(self):
        search_sename = self.__view.ui.lineEdit.text()
        self.__model.search_sename = search_sename

    def search(self):
        self.__model.users = [DataContext().User.load().where(lambda x: x.sename == self.__model.search_sename).
                              first_of_default()]
        self.__model.search_sename = ""

    def load_book(self):
        camera = LoadQrCode(123, (0, 0, 0), (180, 180, 180), "C:/Users/Vlad/PycharmProjects/Libreri/File/num1.png")
        books = camera.load_qr()
        list_book = []
        books_model = DataContext().Book.load()
        for i in books:
            list_book.append(books_model.where(lambda x: x.number == i["Number"]).first_of_default())
        self.__model.list_book = list_book

    def load_list_book(self):
        date = datetime.date.today()
        for i in self.__model.list_book:
            DataContext().Bilet.add(BiletOrig([0, self.__model.select_user.id, i.id, date.strftime("%Y-%m-%d")]))
            i.state = "T"
            DataContext().Book.update(i)
        DataContext().Bilet.save_change()
        DataContext().Book.save_change()
        self.__model.select_user = User([1, "", "", "", "", "", "", "", "", "", "", ""])
        self.__model.list_book = []
        self.__model.search_sename = ""

    def item_changed(self, item):
        row = item.row()
        self.__view.ui.table_user.selectRow(row)
        self.__model.select_user = DataContext().User.list_model()[row]
