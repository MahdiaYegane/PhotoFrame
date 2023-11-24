#create a border around the image like a photo frame

import cv2 as cv

image=cv.imread("E://openCV_images/3.png")
image=cv.copyMakeBorder(image,50,50,20,20,cv.BORDER_REFLECT,
                        None,value=10)

cv.imshow("image",image)
cv.waitKey(0)
cv.destroyAllWindows()