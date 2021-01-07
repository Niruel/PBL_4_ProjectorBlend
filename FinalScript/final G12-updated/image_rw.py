##Documentation for the main class rw(read and write class)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅

##importing of external libraries
#
#

from config_reader import ConfigReader
import numpy as np
import cv2


##The main class ImageRW
#The class is for reading and writing the image, reading in image values and writing in new values to variables
class ImageRW:
    
    ## main class
    # The constructor, defining all the methods of the main class
    # @param self object pointer
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

## The class is used to retrieve the divided parts of the original image after being divided
# @param self is the object pointer, points to the class itself
    def getLeftRightImage(self):
        leftImage = self.originalImage[0:self.img_height, 0:self.img_width]
        rightImage = self.originalImage[0:self.img_height, self.img_width - self.maskArea:self.img_width*2 - self.maskArea]
        return leftImage, rightImage

##Documentation for the class writeLeftMask
#This class is to mask the left part of divided image, specifically the left part after being divide
    def writeLeftMask(self, leftImage):
        leftMaskArea = leftImage[0:self.img_height, self.img_width - self.maskArea:self.img_width] 
        return leftMaskArea
        
## Documentation for the class writeleftCropped
# This class is to get the left part of unmask area of the iamge
    def writeLeftCropped (self, leftImage):
        leftUnmaskArea = leftImage[0:self.img_height, 0:self.img_width - self.maskArea]
        return leftUnmaskArea

##Documentation for the class writeRightMask
#This class is to mask the left part of divided image, specifically the right part after being divided
    def writeRightMask(self, rightImage):
        rightMaskArea = rightImage[0:self.img_height, 0:self.maskArea]
        return rightMaskArea

## Documentation for the class writeRightCropped
# This class is to get the right part of unmask area of the iamge
    def writeRightCropped(self, rightImage):
        rightUnmaskArea = rightImage[0:self.img_height, self.maskArea:self.img_width]
        return rightUnmaskArea

##Documentation for the class gammaCorrectLeft
#This class is to correct the gamma value(brightness, contrast of the image details) specifically the left part after being divided
    def gammaCorrectLeft(self, leftMaskArea):
        maskLeft = np.tile(np.linspace(1, 0, self.maskArea), (self.img_height, 1))
        maskLeft = maskLeft ** (1/self.gammaRate)
        maskLeft = cv2.merge([maskLeft, maskLeft, maskLeft])
        maskLeft = np.uint8(leftMaskArea * maskLeft)
        maskLeft = np.clip((maskLeft), 0, 255)
        return maskLeft

##Documentation for the class gammaCorrectRight
#This class is to correct the gamma value(brightness, contrast of the image details) specifically the right part after being divided
    def gammaCorrectRight(self, rightMaskArea):
        maskRight = np.tile(np.linspace(0, 1, self.maskArea), (self.img_height, 1))
        maskRight = maskRight ** (1/self.gammaRate)
        maskRight = cv2.merge([maskRight, maskRight, maskRight])
        maskRight = np.uint8(rightMaskArea * maskRight)
        maskRight = np.clip((maskRight), 0, 255)
        return maskRight
##Documentation for the class writeFinalImage
# the final image after the execution of all previous processes. write the final image in and update/replace the old unprocessed image
    def writeFinalImage(self, image, filename):
        cv2.imwrite(filename, image)
