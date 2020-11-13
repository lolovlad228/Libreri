from Interfase.IModel import IModel


class BiletOrig(IModel):
    def __init__(self, args=None):
        if args is not None:
            self.id = args[0]
            self.id_user = args[1]
            self.id_book = args[2]
            self.date = args[3]

    def __str__(self):
        return f"Book {self.id}"

    def __repr__(self):
        return f"Book {self.id}"

    def __deepcopy__(self):
        return self

    def __call__(self, args, **kwargs):
        return BiletOrig(args).__deepcopy__()

    def get_list_interfase(self):
        return [str(self.id), str(self.id_user),
                str(self.id_book), str(self.date)]

    def name_model(self):
        return self.__class__.__name__