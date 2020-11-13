import os

import numpy as np
import cv2
from pyzbar import pyzbar
from json import loads


class LoadQrCode:
    def __init__(self, port, low, high, img_main):
        self.__port = port
        self.__low = low
        self.__high = high
        self.__img = cv2.imread(img_main)
        self.__height = None
        self.__width = None
        self.__collision_height = 300

    def img_approximation(self, img):
        self.__height = np.size(img, 0)
        self.__width = np.size(img, 1)
        img_new = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        img_new = cv2.medianBlur(img_new, 1)
        low_color = np.array(self.__low, np.uint8)
        high_color = np.array(self.__high, np.uint8)
        img_filter = cv2.inRange(img_new, low_color, high_color)
        not_img = cv2.bitwise_not(img_filter)
        xor = cv2.bitwise_and(img, img, mask=not_img)
        return xor

    def code_decode(self, img):
        decoded = pyzbar.decode(img)
        polygon = []
        for i in decoded:
            points = [(j.x, j.y) for j in i.polygon]
            polygon.append((points, i.data.decode()))
        for i in range(len(polygon)):
            polygon[i] = (polygon[i][0], polygon[i][1], self.collision(polygon[i][0]))
        return polygon

    def view_model(self, img, data):
        text = ""
        for i in data:
            if i[2]:
                color = (200, 1, 1)
            else:
                color = (10, 10, 10)
            for j in range(len(i[0])):
                try:
                    cv2.line(img, i[0][j], i[0][j + 1], color, 2)
                except IndexError:
                    cv2.line(img, i[0][j], i[0][0], color, 2)
            cv2.putText(img, i[1], i[0][0], cv2.QT_FONT_NORMAL, 1, (30, 105, 210), 2)
            text = loads(i[1])
        cv2.line(img, (self.__width,
                       self.__height - self.__collision_height),
                 (0, self.__height - self.__collision_height),
                 (255, 0, 0), 3)
        return img, text

    def collision(self, data):
        if data[0][1] > self.__height - self.__collision_height:
            return True
        else:
            return False

    def test(self):
        points = self.code_decode(self.img_approximation(self.__img))
        img, text = self.view_model(self.__img, points)
        return text

    def load_qr(self):
        list_img = os.listdir("C:/Users/Vlad/PycharmProjects/Libreri/File")
        num_list = []
        for i in list_img:
            self.__img = cv2.imread(f"C:/Users/Vlad/PycharmProjects/Libreri/File/{i}")
            points = self.code_decode(self.img_approximation(self.__img))
            img, text = self.view_model(self.__img, points)
            num_list.append(text)
        return num_list

