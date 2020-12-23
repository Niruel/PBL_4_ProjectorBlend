#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅

from config_reader import ConfigReader
from image_rw import ImageRW
import cv2
import numpy as np

# ˄

class MainStitcher(object):
    

    def Display_left(self):
        completeLeft = np.hstack((self.unmasked_left[0:self.img_height,0:self.img_width-self.maskArea],self.masked_left[0:self.img_height,0 :self.maskArea]))
        return completeLeft

    def Display_right(self):
        completeRight = np.hstack((self.masked_right[0:self.img_height,0:self.maskArea], self.unmasked_right[0:self.img_height,0:self.img_width-self.maskArea]))
        return completeRight

    def __init__(self):


        self.__imageRW = ImageRW()
        self.masked_left = self.___imageRW.writeLeftMask()
        self.unmasked_left = self.__imageRW.writeLeftCroped()
        self.masked_right = self.__imageRW.writeRightMask()
        self.unmasked_right = self.__imageRW.writeRightCroped()
        
        self.__configReader = ConfigReader("config.ini")
        self.filename = self.__configReader.getIMGName()
        self.img_width = self.__configReader.getIMGWidth()
        self.img_height = self.__configReader.getIMGHeight()
        self.distance = self.__configReader.getDistance()
        self.projector = self.__configReader.getWidth()
        self.originalImage = cv2.imread(self.filename)
        self.maskArea = self.img_width - int(self.img_width*((self.distance/2)/self.projector))
        self.gammaRate = self.__configReader.getGamma()


