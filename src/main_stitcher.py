#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from calculate_mask import CalculateMask
from config_reader import ConfigReader
from image_rw import ImageRW
import numpy as np
import cv2

# ˄


class MainStitcher:

    def stitchImage(self, leftPart, rightPart):
        finalImage = np.hstack((leftPart[:,:], rightPart[:,:]))
        return finalImage

    def Display(self, finalLeft, finalRight):
        cv2.imshow("Masked Left", finalLeft)
        cv2.imshow("Masked Right", finalRight)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def __init__(self):

        self.__imageRW = None

        self.__configReader = None

        self.__calculateMask = None

        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
