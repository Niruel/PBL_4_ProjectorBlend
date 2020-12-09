import numpy as np
import cv2

left = cv2.imread('/Users/reaper45/Downloads/ImageLeft0.png',3)
right = cv2.imread('/Users/reaper45/Downloads/ImageRight0.png',3)
print("hello world")
left1  = left[0:800, 976:1280]
mask1 = np.repeat(np.tile(np.linspace(1, 0, 304), (800, 1))[:, :, np.newaxis], 3, axis=2)
mask2 = np.repeat(np.tile(np.linspace(0, 1, 270), (800, 1))[:, :, np.newaxis], 3, axis=2)

masked = np.uint8(left1*mask1)
masked1 = np.hstack((left[:,:976],masked[:,:]))

cv2.imshow("test", masked1)
cv2.imwrite("left.jpg", masked1)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
