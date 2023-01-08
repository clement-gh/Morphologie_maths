

from listeFonction import *
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

struc = np.array([[0, 0, 0],
                  [2, 1, 2],
                  [1, 1, 1]])

chemin_img = "./lena.jpg"

img = mpimg.imread(chemin_img)


if img.ndim == 3:
    img = rgb2gray(img)

plt.figure(1)
#plt.imshow(img, cmap='gray')
plt.imshow(img, cmap=plt.cm.gray)
plt.title("Image to test seuil")


plt.figure(2)
img = thresholdingImage(img, 128)
#img= additionOfTwoImages(img, img2)
plt.imshow(img, cmap=plt.cm.gray)
plt.title("Image après seuil")


plt.figure(11)
img11 = skeleton_thinning_homotopic(img)
plt.imshow(img11, cmap=plt.cm.gray)
plt.title("Image amincie homotopique")


'''
plt.figure(3)
img3 = thickening(img)
plt.imshow(img3, cmap=plt.cm.gray)
plt.title("Image après 'épaississement")

plt.figure(4)
img4 = thinning(img,struc)
plt.imshow(img4, cmap=plt.cm.gray)
plt.title("Image après amincississement")

plt.figure(4)
img4 = slimming(img)
plt.imshow(img4, cmap=plt.cm.gray)
plt.title("Image après amincississement")




plt.figure(7)
img7= lantuejoulSkeleton(img,100) 
plt.imshow(img7, cmap=plt.cm.gray)
plt.title("Skeletonization")

plt.figure(5)
img1 = erodeBinaryImage(img,4)
plt.imshow(img1, cmap=plt.cm.gray)
plt.title("erode test")

plt.figure(6)
img2 = dilateBinaryImage(img,4)
plt.imshow(img2, cmap=plt.cm.gray)
plt.title("dilate test")



'''
plt.show()
    