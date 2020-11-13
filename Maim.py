import sys
from PyQt5.QtWidgets import QApplication
from Model.LoginModel import LoginModel
from Controller.LoginController import LoginController


def main():
    app = QApplication(sys.argv)
    model = LoginModel()
    controller = LoginController(model)
    app.exec()


if __name__ == '__main__':
    sys.exit(main())