from Interfase.IModel import IModel


class User(IModel):
    def __init__(self, args=None):
        if args is not None:
            self.id = args[0]
            self.login = args[1]
            self.password = args[2]
            self.name = args[3]
            self.sename = args[4]
            self.midname = args[5]
            self.type = args[6]
            self.email = args[7]
            self.phone = args[8]
            self.comment = args[9]
            self._class = args[10]
            self.class_type = args[11]

    def __str__(self):
        return f"User {self.id}"

    def __repr__(self):
        return f"User {self.id}"

    def __deepcopy__(self):
        return self

    def __call__(self, args, **kwargs):
        return User(args).__deepcopy__()

    def get_list_interfase(self):
        return [str(self.id), str(self.login),
                str(self.password), str(self.name),
                str(self.sename), str(self.midname),
                str(self.type), str(self.email),
                str(self.phone), str(self.comment),
                str(self._class), str(self.class_type)]

    def name_model(self):
        return self.__class__.__name__
