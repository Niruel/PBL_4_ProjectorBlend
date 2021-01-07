##Documentation for a module
#This whole module was created as the main class
#!/usr/bin/env python
# -*- coding: utf-8 -*-

##importing external libraries
from image_rw import ImageRW
from main_stitcher import MainStitcher

## Documentation for definition class
#assigning values to the varaibles which will be used to represent the left and right part of the image
leftImage, rightImage = ImageRW().getLeftRightImage()

## Documentation for definition class
# assigning value to the variable leftUnmaskArea and leftMaskArea
# defining the function of 2 variables
# leftUnmaskArea creates an unmasked area based on the left part of the image, specifically after being divided
# leftMaskArea creates a masked area based on the left part of the iamge, specifically after being divided
leftUnmaskArea = ImageRW().writeLeftCropped(leftImage)
leftMaskArea = ImageRW().writeLeftMask(leftImage)

## Documentation for definition class
# assigning value to the variable rightUnmaskArea and rightMaskArea
# defining the function of 2 variables
# rightUnmaskArea creates an unmasked area based on the right part of the image, specifically after being divided
# rightMaskArea creates a masked area based on the right part of the image, specifically after being divided
rightUnmaskArea = ImageRW().writeRightCropped(rightImage)
rightMaskArea = ImageRW().writeRightMask(rightImage)

## Documentation for definition class
# assigning values to varialbes maskLeft and maskRight, which are used to correct the gamma values of the image
# the function of the 2 variables are for gamma correction after the image is divided
maskLeft = ImageRW().gammaCorrectLeft(leftMaskArea)
maskRight = ImageRW().gammaCorrectRight(rightMaskArea)

## Documentation for definition class
# assigning values to varialbes finalLeft and finalRight, which are used to stitch the 2 parts of the image ater being divided
# finalLeft is to process the left part of the image after it's gamma corrected, giving the final product image (works with the stitcher of the right part to connect smoothly on boundaries
# finalRight is to process the right part of the image after  it's gamma corrected, giving the final product image(works with the stitcher of the left part to connect smoothly on boundaries
finalLeft = MainStitcher().stitchImage(leftUnmaskArea, maskLeft)
finalRight = MainStitcher().stitchImage(maskRight, rightUnmaskArea)

## Documentation for definition class
# MainStitcher class stitch together the final parts of the image
# the class execute the function of the 2 previous classes
MainStitcher().Display(finalLeft, finalRight)

## Documentation for definition class
# assigning values to different variables used to update/write in the new values to the left and right parts of the divided image
ImageRW().writeFinalImage(finalLeft, "Masked_Left.jpg")
ImageRW().writeFinalImage(finalRight, "Masked_Right.jpg")
