
# Imgage Histogram - Find, Plot and Analyze
# It which gives you an overall idea about the intensity distribution of an image.
# It distribute data along x and y axis.
# x - axis contain range of color values.
# y - axis contain numbers of pixels in an image.
# With histogram to extract information about contrast, brightness and intensity etc.

# plot histogram using matplotlib

import numpy as np
import cv2
from matplotlib import pyplot as plt

# plotting with calhist method
img = np.zeros((200,200), np.uint8)

cv2.rectangle(img, (0, 100), (200, 200), (255), -1)
cv2.rectangle(img, (0, 50), (50, 100), (127), -1)

# It accept parameters like ([img],[channel],mask,[histsize],range[0-255])
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.plot(hist)
plt.show()

cv2.imshow("res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()