import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "E:/Python Projects/8.Image to sketch/zuckerberg.jpg"

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989,.5870,.1140])
    # it is 2-dimensional array formula to convert image to gray scale
    
def dodge(front,back):
    final_sketch = front*255/(255-back)
    #if image is grater than 255 then it will convert it to 255
    final_sketch[final_sketch>255]=255
    final_sketch[back==255]=255
    #to convert any suitable existing column to categorical type we will use aspect function
    #and uint8 is for 8-bit signed integer
    return final_sketch.astype('uint8')

ss = imageio.imread(img)   # to read the given image
# first we will convert image to black and white (gray scale)
gray = rgb2gray(ss)  

i = 255-gray  
#0,0,0 is for darkest  color and 255,255,255 is for brigthest color which is probably white color

#to convert it into blur image
blur = scipy.ndimage.filters.gaussian_filter(i,sigma=15)
#sigma  is the intensity of blurness of image
r=dodge(blur,gray) #this function will convert our image to sketch by taking two parameter as blur and gray

cv2.imwrite('new_sketch.png',r)