import cv2
image = cv2.imread("111/1.png")

print(image)
cv2.namedWindow("the window")
cv2.imshow("the window", image)

cv2.waitKey(0)