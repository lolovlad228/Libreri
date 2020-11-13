import pyodbc
from Interfase.ISolid import Solide
from Class.EntityClass import EntityModel
from Model.DataModel.User import User
from Model.DataModel.Book import Book
from Model.DataModel.Bilet import Bilet


class DataContext(metaclass=Solide):
    __server = 'localhost'
    __database = 'library'
    __connect = pyodbc.connect("DRIVER={ODBC Driver 13 for SQL Server};"
                               "Server=" + __server + ";"
                               "Database=" + __database + ";"
                               "Trusted_Connection=yes;"
                               )
    __link = __connect.cursor()

    User = EntityModel(User(), __link, __connect)
    Book = EntityModel(Book(), __link, __connect)
    Bilet = EntityModel(Bilet(), __link, __connect)



