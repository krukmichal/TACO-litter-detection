import cv2
import os

def resize_image(filename):
    img = cv2.imread(filename)
    #scale = 1280/max(img.shape[0], img.shape[1])
    #width = int(img.shape[1]*scale)
    #height = int(img.shape[0]*scale)
    width = min(640,img.shape[1])
    height = min(640, img.shape[0])

    dim = (width,height)

    resized = cv2.resize(img,dim,interpolation = cv2.INTER_AREA)

    cv2.imwrite(filename, resized)

def change_size_all_images():
    images = os.listdir("output/images")
    for image in images:
        resize_image("output/images/" + image)
    
