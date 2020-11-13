from Interfase.IObserver import Subject


class LoginModel(Subject):
    def __init__(self):
        self.__password = ""
        self.__mail = ""
        self.__error = ""

        self.__observers = []

    @property
    def password(self):
        return self.__password

    @property
    def mail(self):
        return self.__mail

    @property
    def error(self):
        return self.__error

    @error.setter
    def error(self, val):
        self.__error = val
        self.notify()

    @password.setter
    def password(self, val):
        self.__password = val
        self.notify()

    @mail.setter
    def mail(self, val):
        self.__mail = val
        self.notify()

    def detach(self, observer):
        self.__observers.remove(observer)

    def notify(self):
        for i in self.__observers:
            i.update()

    def attach(self, observer):
        self.__observers.append(observer)