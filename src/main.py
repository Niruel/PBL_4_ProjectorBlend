#!/usr/bin/env python
# -*- coding: utf-8 -*-

from image_rw import ImageRW
from config_reader import ConfigReader
from main_stitcher import MainStitcher

leftImage, rightImage = ImageRW().getLeftRightImage()

leftUnmaskArea = ImageRW().writeLeftCropped(leftImage)
leftMaskArea = ImageRW().writeLeftMask(leftImage)

rightUnmaskArea = ImageRW().writeRightCropped(rightImage)
rightMaskArea = ImageRW().writeRightMask(rightImage)

maskLeft = ImageRW().gammaCorrectLeft(leftMaskArea)
maskRight = ImageRW().gammaCorrectRight(rightMaskArea)

finalLeft = MainStitcher().stitchImage(leftUnmaskArea, maskLeft)
finalRight = MainStitcher().stitchImage(maskRight, rightUnmaskArea)

MainStitcher().Display(finalLeft, finalRight)

ImageRW().writeFinalImage(finalLeft, "Masked_Left.jpg")
ImageRW().writeFinalImage(finalRight, "Masked_Right.jpg")