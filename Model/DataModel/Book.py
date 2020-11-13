from Interfase.IModel import IModel


class Book(IModel):
    def __init__(self, args=None):
        if args is not None:
            self.id = args[0]
            self.name = args[1]
            self.author = args[2]
            self.data = args[3]
            self.number = args[4]
            self.state = args[5]
            self.photo = args[6]

    def __str__(self):
        return f"Book {self.id}"

    def __repr__(self):
        return f"Book {self.id}"

    def __deepcopy__(self):
        return self

    def __call__(self, args, **kwargs):
        return Book(args).__deepcopy__()

    def get_list_interfase(self):
        return [str(self.id), str(self.name),
                str(self.author), str(self.data),
                str(self.number), str(self.state),
                self.photo]

    def name_model(self):
        return self.__class__.__name__
