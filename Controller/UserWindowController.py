from Model.DataModel.User import User
from View.UserWindowView import UserWindowView
from Class.DataContext import DataContext


class UserWindowController:
    def __init__(self, model):
        self.__model = model
        self.__view = UserWindowView(self, self.__model)
        self.__view.show()

    def set_login(self):
        login = self.__view.ui.Name.text()
        self.__model.login = login

    def set_password(self):
        password = self.__view.ui.Password.text()
        self.__model.password = password

    def set_name_2(self):
        name = self.__view.ui.Name_2.text()
        self.__model.name = name

    def set_sename(self):
        sename = self.__view.ui.Sename.text()
        self.__model.sename = sename

    def set_midname(self):
        midname = self.__view.ui.MIdname.text()
        self.__model.midname = midname

    def set_type(self):
        _type = self.__view.ui.Type.text()
        self.__model.type = _type

    def set_mail(self):
        mail = self.__view.ui.Mail.text()
        self.__model.mail = mail

    def set_phone(self):
        phone = self.__view.ui.Phone.text()
        self.__model.phone = phone

    def set_comment(self):
        comment = self.__view.ui.Comment.text()
        self.__model.comment = comment

    def set_class(self):
        _class = self.__view.ui.Class.text()
        self.__model._class = _class

    def set_type_class(self):
        type_class = self.__view.ui.TypeClass.text()
        self.__model.type_class = type_class

    def delate(self):
        self.__model.users = DataContext().User.delite(self.__model.select_user).save_change().load().list_model()
        self.__model.select_user = User(["", "", "", "", "", "", "", "", "", "", "", ""])

    def insert(self):
        self.__model.users = DataContext().User.add(self.__model.select_user).save_change().load().list_model()
        self.__model.select_user = User(["", "", "", "", "", "", "", "", "", "", "", ""])

    def update(self):
        self.__model.users = DataContext().User.update(self.__model.select_user).save_change().load().list_model()
        self.__model.select_user = User(["", "", "", "", "", "", "", "", "", "", "", ""])

    def item_changed(self, item):
        row = item.row()
        self.__view.ui.table_user.selectRow(row)
        self.__model.select_user = DataContext().User.list_model()[row]

    #def student(self):
    #    model = MainWindowModel()
    #    controller = MainWindowController(model)
    #    self.__view.close()
