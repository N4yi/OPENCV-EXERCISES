import cv2
import numpy as np

img=cv2.imread("klon.jpg")
color=img[150,200]
print(color)
cv2.imshow("Klon Asker",img)
cv2.waitKey(0)
cv2.destroyAllWindows()