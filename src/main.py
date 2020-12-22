from image_rw import ImageRW
from config_reader import ConfigReader
from main_stitcher import MainStitcher
from calculate_mask import CalculateMask

leftImage, rightImage = ImageRW().getLeftRightImage()

leftUnmaskArea, leftMaskArea = ImageRW().writeLeftMask(leftImage)
rightUnmaskArea, rightMaskArea = ImageRW().writeRightMask(rightImage)

maskLeft = ImageRW().gammaCorrectLeft(leftMaskArea)
maskRight = ImageRW().gammaCorrectRight(rightMaskArea)

finalLeft = MainStitcher().stitchImage(leftUnmaskArea, maskLeft)
finalRight = MainStitcher().stitchImage(maskRight, rightUnmaskArea)

MainStitcher().Display(finalLeft, finalRight)

ImageRW().writeFinalImage(finalLeft, "Masked_Left.jpg")
ImageRW().writeFinalImage(finalRight, "Masked_Right.jpg")