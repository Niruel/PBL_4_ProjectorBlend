#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from config_reader import ConfigReader
import cv2

# ˄


class ImageRW:


    def getLeftRightImage(self):
        self.originalImage = cv2.imread('Whole.jpg')
        self.leftImage = self.originalImage[0:800, 0:1280]
        self.rightImage = self.originalImage[0:800, 976:2256]
        cv2.imshow('test', self.originalImage)
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

        self.__configReader = None
        self.originalImage = None
        self.leftImage = None
        self.rightImage = None


    # ˅
    
    # ˄


# ˅
# ˄
