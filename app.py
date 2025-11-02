import cv2          #library for computer vision tasks
import imutils      #library for image processing tasks

img = cv2.imread("pandya.jpg") #read the image from file
resizeimg = imutils.resize(img, width=600, height=400)   #resize image to specified width and height
cv2.imwrite("resized_image.jpg", resizeimg)  #save the resized image to file
cv2.imshow("Resized Image", resizeimg)  #display the resized image in a window
cv2.waitKey(0)
cv2.destroyAllWindows()