##Documentation for a module
#This whole module was created as the main class

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅

##importing of external and precreated libraries
import numpy as np
import cv2

## Documentation for main class MainStitcher
# The constructor, used to stitch together the divided parts of the original image, returns the final image at the end of the class
class MainStitcher:

## Documentation for the class stitchImage
# this class is to stitch together the left and right parts of the image after being divided, and form a final image
    def stitchImage(self, leftPart, rightPart):
        finalImage = np.hstack((leftPart[:,:], rightPart[:,:]))
        return finalImage

## Documentation for the class Display
# used to display the final image after being finished
    def Display(self, finalLeft, finalRight):
        cv2.imshow("Masked Left", finalLeft)
        cv2.imshow("Masked Right", finalRight)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
