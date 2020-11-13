import io
from pickle import loads
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from View.DopInfo import Ui_Dop_info
from Interfase.IObserver import Observer
from PIL import Image


class DopInfoView(QMainWindow):
    __metaclass__ = Observer

    def __init__(self, controller, model):
        super(QMainWindow, self).__init__()

        self.__model = model
        self.__controller = controller
        self.__ui = Ui_Dop_info()
        self.__ui.setupUi(self)

        self.__model.attach(self)

        self.__ui.Load_img_book.clicked.connect(self.__controller.load_img_book)
        self.__ui.Load_img_qr.clicked.connect(self.__controller.load_img_qr)
        self.update()

    @property
    def ui(self):
        return self.__ui

    def conver_img(self, img):
        img_now = img.convert("RGBA")
        data = img_now.tobytes("raw", "RGBA")
        qim = QImage(data, img_now.size[0], img_now.size[1], QImage.Format_RGBA8888)
        pixmap = QPixmap.fromImage(qim)
        return pixmap

    def update(self):
        try:
            image = Image.open(io.BytesIO(self.__model.photo))
            self.__ui.img_book.setPixmap(self.conver_img(image))
        except Exception:
            pass
        self.__ui.img_qr_code.setPixmap(self.conver_img(self.__model.photo_qr))
