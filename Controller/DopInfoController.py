import os

from PyQt5.QtWidgets import QFileDialog
from View.DopInfoView import DopInfoView
import PIL as pil
import io


class DopInfoController:

    def __init__(self, model):
        self.__model = model
        self.__view = DopInfoView(self, self.__model)
        self.__view.show()

    def load_img_book(self):
        try:
            fname = QFileDialog.getOpenFileName(caption='Open file', directory='/home', filter="Images (*.png *.jpg)")[0]
            img = pil.Image.open(fname)
            img = img.resize((200, 300))
            buf = io.BytesIO()
            img.save(buf, format='PNG')
            byte_im = buf.getvalue()
            self.__model.photo = byte_im
        except Exception:
            pass

    def load_img_qr(self):
        path = "C:/Users/Vlad/Pictures"
        name_img = f"num-{str(self.__model.number)}.png"
        self.__model.photo_qr.save(os.path.join(path, name_img), "PNG")
