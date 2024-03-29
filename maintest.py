
from listeFonction import *
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def  testSeuillage(seuil):
        chemin_img = "./lena.jpg"
        img = mpimg.imread(chemin_img)
        
        
        plt.figure(1).show()
        plt.imshow(img, cmap=plt.cm.gray)
        plt.title("Image to test seuillage")
        plt.figure(2).show()
        img = thresholdingImage(img, seuil)
        plt.imshow(img, cmap=plt.cm.gray)
        plt.title("Image après seuillage")
        wait()
        
        
        

def testAddition():
        chemin_img2 = "./cercle.jpg"
        chemin_img = "./rectangle.jpg"
        img = mpimg.imread(chemin_img)
        img2 = mpimg.imread(chemin_img2)
        
        img = thresholdingImage(img, 128)
        img2 = thresholdingImage(img2, 128)
        
        plt.figure(1).show()
        plt.imshow(img, cmap=plt.cm.gray)
        plt.title("Image to test addition")
        plt.figure(2).show()
        img = additionOfTwoImages(img, img2)
        plt.imshow(img, cmap=plt.cm.gray)
        plt.title("Image après addition")
        wait()
        

def testSoustraction():
        chemin_img2 = "./cercle.jpg"
        chemin_img = "./rectangle.jpg"
        img = mpimg.imread(chemin_img)
        img2 = mpimg.imread(chemin_img2)
        
        img = thresholdingImage(img, 128)
        img2 = thresholdingImage(img2, 128)
        
        plt.figure(1).show()
        plt.imshow(img, cmap=plt.cm.gray)
        plt.title("Image to test addition")
        plt.figure(2).show()
        img = subtractionOfTwoImages(img, img2)
        plt.imshow(img, cmap=plt.cm.gray)
        plt.title("Image après soustraction")
        wait()

def testErosion():
        chemin_img = "./cercle.jpg"
        img = mpimg.imread(chemin_img)
        img = thresholdingImage(img, 128)
        plt.figure(1).show()
        plt.imshow(img, cmap=plt.cm.gray)
        plt.title("Image to test erosion")
        plt.figure(2).show()
        img = erodeBinaryImage(img,20)
        plt.imshow(img, cmap=plt.cm.gray)
        plt.title("Image après erosion")
        wait()

def testDilatation():
        chemin_img = "./cercle.jpg"
        img = mpimg.imread(chemin_img)
        img = thresholdingImage(img, 128)
        plt.figure(1).show()
        plt.imshow(img, cmap=plt.cm.gray)
        plt.title("Image to test dilatation")
        plt.figure(2).show()
        img = dilateBinaryImage(img,20)
        plt.imshow(img, cmap=plt.cm.gray)
        plt.title("Image après dilatation")
        wait()

def testSqueletteLantuejoul():
        chemin_img = "./lena.jpg"
        img = mpimg.imread(chemin_img)
        img = thresholdingImage(img, 128)
        plt.figure(1).show()
        plt.imshow(img, cmap=plt.cm.gray)
        plt.title("Image to test squelette")
        plt.figure(2).show()
        img = lantuejoulSkeleton(img)
        plt.imshow(img, cmap=plt.cm.gray)
        plt.title("Image après squelettion")
        wait()

np1 = np.array([[2, 0,0],
                [1, 1, 0],
                [2, 1, 2]]) #meilleur

np2 = np.array([[2, 1,0],
                [1, 1, 0],
                [2, 1, 2]]) #fractal

np3 = np.array([[2, 0,2],[1, 1, 1],[1, 1, 2]])

np4 = np.array([[0, 0,0],[2, 1, 2],[1, 1, 1]])

def testAmincissementHomotopique(neighbourhood_pattern):
                   
        chemin_img = "./lena.jpg"
        img = mpimg.imread(chemin_img)
        img = thresholdingImage(img, 128)
        plt.figure(1).show()
        plt.imshow(img, cmap=plt.cm.gray)
        plt.title("Image to test amincissment")
        plt.figure(2).show()
        img = skeletonThinningHomotopic(img, neighbourhood_pattern)
        plt.imshow(img, cmap=plt.cm.gray)
        plt.title("Image après amincissment homotopique")
        plt.show()
        wait()

def wait():
    input("Press Enter to continue...")
    plt.close("all")

testAmincissementHomotopique(np2)