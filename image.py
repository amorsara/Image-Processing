from random import *
from tkinter import messagebox
import cv2 as cv
import imageio
import numpy as np


class MyImage:

    # ctor- image function :
    def __init__(self, nativ, nameWindow):
        global noChange
        self.__file_name = nativ
        self.__nameWindow = nameWindow
        self.__img = imageio.imread(nativ)
        self.__img = cv.cvtColor(self.__img, cv.COLOR_BGR2RGB)
        self.positionImg()
        noChange = self.__img
        self.showImage(self.__nameWindow, noChange)
        cv.setMouseCallback(self.__nameWindow, self.randomColorImg)

    # position function :
    def positionImg(self):
        height, width, channels = self.__img.shape
        height = int(height * 20 / 50)
        width = int(width * 20 / 50)
        dim = (width, height)
        self.__img = cv.resize(self.__img, dim)

    # show image function :
    def showImage(self, nameWin, image):
        self.__img = image
        self.__nameWindow = nameWin
        cv.imshow(nameWin, image)
        cv.setMouseCallback(self.__nameWindow, self.disable)

    # help function & call to put text function :
    def funcText(self, txt):
        cv.setMouseCallback(self.__nameWindow, self.insertText, txt)

    # put text function :
    def insertText(self, event, x, y, params, txt="NULL"):
        global ix, iy
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        if event == cv.EVENT_LBUTTONDOWN:
            ix = x
            iy = y
            cv.putText(self.__img, str(txt), (ix, iy), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, color, 3)
            self.showImage(self.__nameWindow, self.__img)
            cv.setMouseCallback(self.__nameWindow, self.disable)

    #  functions filters :

    #  functions design- black & colorful image:
    def design1(self):
        self.__img=noChange
        sharpen_filter = np.array([[0, -2, 0],
                                   [-2, 8, -2],
                                   [0, -2, 0]])
        image = cv.filter2D(self.__img, 0, sharpen_filter)
        self.showImage(self.__nameWindow, image)

    #  functions design- blurry image :
    def design2(self):
        self.__img = noChange
        image = self.__img
        image_blurred = cv.blur(src=image, ksize=(20, 10))
        self.showImage(self.__nameWindow, image_blurred)

    #  functions design- colorful image :
    def design3(self):
        self.__img = noChange
        image = cv.cvtColor(self.__img, cv.COLOR_RGB2HSV)
        self.showImage(self.__nameWindow, image)

    #  functions design- black & white image :
    def design4(self):
        self.__img = noChange
        grayImage = cv.cvtColor(self.__img, cv.COLOR_BGR2GRAY)
        (thresh, blackAndWhiteImage) = cv.threshold(grayImage, 127, 255, cv.THRESH_BINARY)
        self.showImage(self.__nameWindow, blackAndWhiteImage)

    #  functions design- rotate image :
    def design5(self):
        self.__img = noChange
        (h, w) = self.__img.shape[:2]
        (cX, cY) = (w // 2, h // 2)
        M = cv.getRotationMatrix2D((cX, cY), 45, 1.0)
        rotated = cv.warpAffine(self.__img, M, (w, h))
        self.showImage(self.__nameWindow, rotated)

    #  functions design- light colorful image :
    def design6(self):
        self.__img = noChange
        (thresh, blackAndWhiteImage) = cv.threshold(self.__img, 127, 255, cv.THRESH_BINARY)
        self.showImage(self.__nameWindow, blackAndWhiteImage)

    #  functions design- lines image :
    def design7(self):
        self.__img = noChange
        image = cv.Canny(self.__img, 50, 300)
        self.showImage(self.__nameWindow, image)

    #  functions design- sharp image :
    def design8(self):
        self.__img = noChange
        sharpen_filter = np.array([[0, -1, 0],
                                   [-1, 5, -1],
                                   [0, -1, 0]])
        image = cv.filter2D(self.__img, 0, sharpen_filter)
        self.showImage(self.__nameWindow, image)

    #  functions design- border image :
    def design9(self):
        self.__img = noChange
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        image = cv.copyMakeBorder(self.__img, 15, 15, 15, 15, cv.BORDER_CONSTANT, None, color)
        self.showImage(self.__nameWindow, image)

    #  end functions filters

    #  function show original image (after cropping):
    def ImgNoChange(self):
        self.showImage(self.__nameWindow, noChange)

    # function to save the changes:
    @staticmethod
    def saveChange(win):
        return messagebox.askyesno(win, "Do you want to save the changes?")

    #  functions shapes & cut image:
    def drawOrCut(self, event, x, y, flags, param):
        global ix, iy, drawing
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        if event == cv.EVENT_LBUTTONDOWN:
            drawing = True
            ix = x
            iy = y
        elif event == cv.EVENT_LBUTTONUP:
            drawing = False
            centerSh = (int((ix + x) / 2), int((iy + y) / 2))
            if param == "circle":
                cv.circle(self.__img, centerSh, int(abs(x - ix) / 2), color, 3)
            elif param == "line":
                cv.line(self.__img, (ix, iy), (x, y), color, 8, cv.LINE_AA)
            elif param == "rectangle":
                cv.rectangle(self.__img, (ix, iy), (x, y), color, 3)
            elif param == "triangular":
                p1 = (ix, iy)
                p2 = (x, y)
                p3 = (x + 150, y + 20)
                cv.line(self.__img, p1, p2, color, 8, cv.LINE_AA)
                cv.line(self.__img, p2, p3, color, 8, cv.LINE_AA)
                cv.line(self.__img, p1, p3, color, 8, cv.LINE_AA)
            elif param == "ellipse":
                cv.ellipse(self.__img, centerSh, (ix, iy), int(abs(x - ix) / 2), 360, 0, color, 3, cv.LINE_AA)
            # if param == "cut":
            else:
                self.image = self.__img[iy:y, ix:x]
                newWindow = "newImg"
                cv.imshow(newWindow, self.image)
                cv.setMouseCallback(self.__nameWindow, self.disable)
                if self.saveChange("save") is True:
                    self.showImage(self.__nameWindow, self.image)
                    global noChange
                    noChange = self.image
                    cv.setMouseCallback(self.__nameWindow, self.disable)
                cv.destroyWindow(newWindow)
            self.showImage(self.__nameWindow, self.__img)

    #  end functions shapes & cut image

    # help functions shapes & cut image :
    def getType(self, selectType):
        ix = 0
        iy = 0
        drawing = False
        cv.setMouseCallback(self.__nameWindow, self.drawOrCut, selectType)

    # change the color of image - random - challenge:
    def randomColorImg(self, event, x, y, flags, param):
        if event == cv.EVENT_RBUTTONDOWN:
            r = self.__img[:, :, 2] + randint(0, 255)
            g = self.__img[:, :, 1] + randint(0, 255)
            b = self.__img[:, :, 0] + randint(0, 255)
            self.__img = cv.merge((r, g, b))
            cv.imshow(self.__nameWindow, self.__img)

    # function call change random color :
    def disable(self, event, x, y, flags, param):
        cv.setMouseCallback(self.__nameWindow, self.randomColorImg)

    # save image function :
    def saveImg(self):
        cv.imwrite("pic.jpg", self.__img)
