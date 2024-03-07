######################################
#                                    #
#        Onur Oduncu - 22253503      #
#                                    #
######################################


import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/peppers.png')
red = img[:,:,2] #1.band
green = img[:,:,1] #2.band
blue = img[:,:,0] #3.band

plt.subplot(2, 2, 1)
plt.imshow(cv.cvtColor(img,cv.COLOR_BGR2RGBA))
plt.title("Doğal renkli")
# cv.imwrite('images/peppers.png',img)

plt.subplot(2, 2, 2)
plt.imshow(red,cmap='gray')
plt.title("Kırmızı bandına gri-ton görüntü")

plt.subplot(2, 2, 3)
plt.imshow(green,cmap='gray')
plt.title("Yeşil bandına gri-ton görüntü")

plt.subplot(2, 2, 4)
plt.imshow(blue,cmap='gray')
plt.title("Mavi bandına gri-ton görüntü")

plt.suptitle("gray-scale, monochromatic")
plt.show()


plt.subplot(2, 2, 1)
plt.imshow(cv.cvtColor(img,cv.COLOR_BGR2RGBA))
plt.title("original")

GRB = img.copy()
GRB[:,:,2] = img[:,:,1] 
GRB[:,:,1] = img[:,:,2]
plt.subplot(2, 2, 2)
plt.imshow(cv.cvtColor(GRB,cv.COLOR_BGR2RGBA))
plt.title("GRB")

RBG = img.copy()
RBG[:,:,0] = img[:,:,1] 
RBG[:,:,1] = img[:,:,0]
plt.subplot(2, 2, 3)
plt.imshow(cv.cvtColor(RBG,cv.COLOR_BGR2RGBA))
plt.title("RBG")

GBR = img.copy()
GBR[:,:,2] = img[:,:,1] 
GBR[:,:,1] = img[:,:,0] 
GBR[:,:,0] = img[:,:,2]
plt.subplot(2, 2, 4)
plt.imshow(cv.cvtColor(GBR,cv.COLOR_BGR2RGBA))
plt.title("GBR")

plt.suptitle("Yapay renkli RGB görüntüler")
plt.show()

plt.subplot(2, 2, 1)
plt.imshow(cv.cvtColor(img,cv.COLOR_BGR2RGBA))
plt.title("original")

only_red = img.copy()
only_red[:,:,1] = 0
only_red[:,:,0] = 0
plt.subplot(2, 2, 2)
plt.imshow(cv.cvtColor(only_red,cv.COLOR_BGR2RGBA))
plt.title("sadece kırmızı")

only_green = img.copy()
only_green[:,:,2] = 0
only_green[:,:,0] = 0
plt.subplot(2, 2, 3)
plt.imshow(cv.cvtColor(only_green,cv.COLOR_BGR2RGBA))
plt.title("sadece yeşil")

only_blue = img.copy()
only_blue[:,:,2] = 0
only_blue[:,:,1] = 0
plt.subplot(2, 2, 4)
plt.imshow(cv.cvtColor(only_blue,cv.COLOR_BGR2RGBA))
plt.title("sadece mavi")


plt.suptitle("(Kırmızı-yeşil-mavi) yapay renklendirilmesi")
plt.show()