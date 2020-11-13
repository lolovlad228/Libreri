import pyodbc
from Interfase.Fluent import Fluent
from Interfase.IModel import IModel


class EntityModel(Fluent):
    def __init__(self, model_info, db, link):
        self.__model_info = model_info
        self.__list_model = []
        self.__content = db
        self.__link = link
        self.__hash_table = None
        self.__list_save = []

    def load(self):
        self.__list_model.clear()
        self.__content.execute("Select * From \"" + self.__model_info.name_model() + "\"")
        result = self.__content.fetchall()
        self.__link.commit()
        for i in result:
            self.__list_model.append(self.__model_info(i))

    def where(self, lmd):
        self.__hash_table = list(filter(lmd, self.__list_model))

    def first_of_default(self):
        if self.__hash_table is not None:
            if len(self.__hash_table) > 0:
                return self.__hash_table[0]
            else:
                return False
        else:
            return self.__list_model[0]

    def delite(self, model=None):
        if isinstance(model, IModel):
            self.__list_save.append((model, "delite"))
        elif model is None:
            for i in self.__hash_table:
                self.__list_save.append((i, "delite"))
        else:
            for i in list(filter(model, self.__list_model)):
                self.__list_save.append((i, "delite"))

    def add(self, model):
        self.__list_save.append((model, "add"))

    def update(self, model):
        if isinstance(model, IModel):
            self.__list_save.append((model, "update"))

    def save_change(self):
        cl_name = self.__column_name()
        for i in self.__list_save:
            if i[1] == "delite":
                sql = "DELETE FROM \"" + self.__model_info.name_model() + "\" WHERE  Id = ?"
                self.__content.execute(sql, (i[0].id, ))
                self.__link.commit()
            elif i[1] == "add":
                str_cl_name = ", ".join(cl_name[1:],)
                value = ""
                for k in range(len(i[0].get_list_interfase()[1:])):
                    value += "?, "
                sql = "INSERT INTO \"" + self.__model_info.name_model() + "\" (" + str_cl_name + ") VALUES " \
                      + "(" + value[:len(value) - 2] + ")"
                self.__content.execute(sql, tuple(i[0].get_list_interfase()[1:]))
                self.__link.commit()
            elif i[1] == "update":
                value = ""
                for k in range(1, len(i[0].get_list_interfase())):
                    value += cl_name[k] + " = ?, "
                sql = "UPDATE \"" + self.__model_info.name_model() + "\" SET " + value[:len(value) - 2] + \
                      " WHERE Id = ?"
                args = i[0].get_list_interfase()[1:] + [i[0].get_list_interfase()[0]]
                self.__content.execute(sql, tuple(args))
                self.__link.commit()
        self.__list_save.clear()

    def list_model(self):
        if self.__hash_table is None:
            return self.__list_model
        else:
            return self.__hash_table

    def join(self, model_one, model_two, arg):
        self.__list_model.clear()
        name_model_one = model_one.name_model()
        name_model_two = model_two.name_model()
        sql_text = "Select bo.*, u.*, bi.* from \"" + self.__model_info.name_model() + "\" bi " \
                   "Inner Join \"" + name_model_two + "\" u on bi.Id_" + name_model_two + " = u.Id " \
                   "Inner Join \"" + name_model_one + "\" bo on bi.Id_" + name_model_one + " = bo.Id"
        self.__content.execute(sql_text)
        result = self.__content.fetchall()
        self.__link.commit()
        for i in result:
            list_arg = []
            for j in arg:
                list_arg.append(i[j])
            self.__list_model.append(self.__model_info(list_arg))

    def get_name(self):
        return self.__model_info.name_model()

    def __column_name(self):
        self.__content.execute("EXEC sp_columns \"" + self.__model_info.name_model() + "\"")
        result = list(map(lambda x: x[3], self.__content.fetchall()))
        return result


