import matplotlib.pyplot as plt
import cv2 as cv

I1 = cv.imread("./images/lenna.bmp")
I2 = cv.imread("./images/DIPXE.jpg")

plt.subplot(221)
plt.axis("off")
plt.imshow(cv.cvtColor(I1,cv.COLOR_BGR2RGB))
plt.title("original image")

plt.subplot(222)
plt.axis("off")
F1 = I1[::-1,:]
plt.imshow(cv.cvtColor(F1,cv.COLOR_BGR2RGB))
plt.title("flipped image")

plt.subplot(223)
plt.axis("off")
F2 = I1[::4,::4]
plt.imshow(cv.cvtColor(F2,cv.COLOR_BGR2RGB))
plt.title("sampled image")

plt.tight_layout()
plt.show()


plt.subplot(221)
plt.axis("off")
plt.imshow(cv.cvtColor(I2,cv.COLOR_BGR2RGB))
plt.title("original image")

plt.subplot(222)
plt.axis("off")
Y = cv.add(I2[:,:256],I1[:138,:])
plt.imshow(cv.cvtColor(Y,cv.COLOR_BGR2RGB))
plt.title("original image")

plt.subplot(223)
plt.axis("off")
plt.imshow(cv.cvtColor(cv.bitwise_not(I2),cv.COLOR_BGR2RGB))
plt.title("complement image")

plt.tight_layout()
plt.show()


"""Y=imadd(im1(:,1:256),OrjI(1:138,:));
subplot(1,3,1),imshow(im1);title('original image');
subplot(1,3,2),imshow(Y);title('original image');
subplot(1,3,3),imshow(imcomplement(im1));title('complement image');"""