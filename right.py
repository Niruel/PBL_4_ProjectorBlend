import numpy as np
import cv2

left = cv2.imread('/Users/reaper45/Downloads/ImageLeft0.png',3)
right = cv2.imread('/Users/reaper45/Downloads/ImageRight0.png',3)
print("hello world")
right1  = right[0:800, :270]
mask1 = np.repeat(np.tile(np.linspace(1, 0, 270), (800, 1))[:, :, np.newaxis], 3, axis=2)
mask2 = np.repeat(np.tile(np.linspace(0, 1, 270), (800, 1))[:, :, np.newaxis], 3, axis=2)

masked = np.uint8(right1*mask2)
masked2 = np.hstack((masked[:,:],right[:,270:1280]))

cv2.imshow("test", masked2)
cv2.imwrite("right.jpg", masked2)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
