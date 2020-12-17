import numpy as np
import cv2

originalImage = cv2.imread('Whole.jpg')
leftImage = originalImage[0:800, 0:1280] #image to be displayed using the left projector
rightImage = originalImage[0:800, 976:2256] #image to be displayed using the right projector

leftUnmaskArea = leftImage[0:800, :975] #unmasked part
leftMaskArea = leftImage[0:800, 976:1280] #masked part

rightMaskArea = rightImage[0:800, :304] #masked part
rightUnmaskArea = rightImage[0:800, 305:1280] #unmasked part

invGamma = 1 / 2.2 #the inverse gamma rate, usually 0.4

maskLeft = np.tile(np.linspace(1, 0, 304), (800, 1)) #array for the left mask, full color to black
maskLeft = maskLeft ** (invGamma) #gamma correction for the mask
maskLeft = cv2.merge([maskLeft, maskLeft, maskLeft]) #merging the gamma-corrected RGB channel

maskedLeft = np.uint8(leftMaskArea * maskLeft) #applying the mask on the designated area
maskedLeft = np.clip((maskedLeft), 0, 255) #limitting the value for the channel from 0 to 255 (RGB channel)
finalLeft = np.hstack((leftUnmaskArea[:,:], maskedLeft[:,:])) #combining the masked part of the image with the unamsked one

cv2.imwrite("maskedLeft.jpg", finalLeft)

maskRight = np.tile(np.linspace(0, 1, 304), (800, 1)) #array for the right mask, black to full color
maskRight = maskRight ** (invGamma) #gamma correction for the mask
maskRight = cv2.merge([maskRight, maskRight, maskRight]) #merging the gamma-corrected RGB channel

maskedRight = np.uint8(rightMaskArea * maskRight) #applying the mask on the designated area
maskedRight = np.clip((maskedRight), 0, 255) #limitting the value for the channel from 0 to 255 (RGB channel)
finalRight = np.hstack((maskedRight[:,:],rightUnmaskArea[:,:])) #combining the masked part of the image with the unamsked one

cv2.imwrite("maskedRight.jpg", finalRight)

# cv2.imshow("Left", finalLeft)
# cv2.imshow("Right", finalRight)
cv2.imshow("Right", originalImage)

cv2.waitKey(0)
cv2.destroyAllWindows()