#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from config_reader import ConfigReader
import cv2

# ˄


class ImageRW:


    def getLeftRightImage(self):
        self.originalImage = cv2.imread(self.filename)
        self.leftImage = self.originalImage[0:self.img_height, 0:self.img_width]
        self.rightImage = self.originalImage[0:self.img_height, 976:976+self.img_width]
        cv2.imshow('Original', self.originalImage)
        cv2.imshow('Original Left', self.leftImage)
        cv2.imshow('Original Right', self.rightImage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def writeRightMask(self, image, name):
        # ˅
        pass
        # ˄

    def writeLeftMask(self, image, name):
        # ˅
        pass
        # ˄

    def writeLeftImage(self, image, filename):
        # ˅
        pass
        # ˄

    def writeRightImage(self, image, filename):
        # ˅
        pass
        # ˄

    def __init__(self):

        self.__configReader = ConfigReader("config.ini")
        self.filename = self.__configReader.getIMGName()
        self.img_width = self.__configReader.getIMGWidth()
        self.img_height = self.__configReader.getIMGHeight()
        self.originalImage = None
        self.leftImage = None
        self.rightImage = None


    # ˅
    
    # ˄


# ˅
# ˄
