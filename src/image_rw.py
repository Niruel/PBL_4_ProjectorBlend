#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from config_reader import ConfigReader
import cv2
import numpy as np

# ˄


class ImageRW:

    def __init__(self):
        self.__configReader = ConfigReader("config.ini")
        self.filename = self.__configReader.getIMGName()
        self.img_width = self.__configReader.getIMGWidth()
        self.img_height = self.__configReader.getIMGHeight()
        self.distance = self.__configReader.getDistance()
        self.projector = self.__configReader.getWidth()
        self.originalImage = cv2.imread(self.filename)
        self.maskArea = self.img_width - int(self.img_width*((self.distance/2)/self.projector))
        self.gammaRate = self.__configReader.getGamma()

    def getLeftRightImage(self):
        leftImage = self.originalImage[0:self.img_height, 0:self.img_width]
        rightImage = self.originalImage[0:self.img_height, self.img_width - self.maskArea:self.img_width*2 - self.maskArea]
        return leftImage, rightImage

    def writeLeftMask(self, leftImage):
        leftMaskArea = leftImage[0:self.img_height, self.img_width - self.maskArea:self.img_width] 
        return leftMaskArea

    def writeLeftCroped (self, leftImage):
        leftUnmaskArea = leftImage[0:self.img_height, 0:self.img_width - self.maskArea]
        return leftUnmaskArea

    def writeRightMask(self, rightImage):
        rightMaskArea = rightImage[0:self.img_height, 0:self.maskArea]
        
        return rightMaskArea

    def writeRightCroped(self, rightImage):
        rightUnmaskArea = rightImage[0:self.img_height, self.maskArea:self.img_width]
        return rightUnmaskArea

    def gammaCorrectLeft(self, leftMaskArea):
        maskLeft = np.tile(np.linspace(1, 0, self.maskArea), (self.img_height, 1))
        maskLeft = maskLeft ** (1/self.gammaRate)
        maskLeft = cv2.merge([maskLeft, maskLeft, maskLeft])
        maskLeft = np.uint8(leftMaskArea * maskLeft)
        maskLeft = np.clip((maskLeft), 0, 255)
        return maskLeft

    def gammaCorrectRight(self, rightMaskArea):
        maskRight = np.tile(np.linspace(0, 1, self.maskArea), (self.img_height, 1))
        maskRight = maskRight ** (1/self.gammaRate)
        maskRight = cv2.merge([maskRight, maskRight, maskRight])
        maskRight = np.uint8(rightMaskArea * maskRight)
        maskRight = np.clip((maskRight), 0, 255)
        return maskRight

    def writeFinalImage(self, image, filename):
        cv2.imwrite(filename, image)
