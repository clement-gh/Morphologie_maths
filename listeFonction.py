import numpy as np 

#import pathlib


def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray

# Seuillage d'une image
def thresholdingImage(img,threshold):

    new_img = np.zeros(img.shape)
    new_img[img <= threshold] = 0
    new_img[img > threshold] = 1
    return new_img
    

def additionOfTwoImages(img1, img2):
   # assert img1.shape == img2.shape, "Les deux images doivent avoir les mêmes dimensions"
    img = (img1 + img2)
    img[img > 255] = 255
    
    return img

def subtractionOfTwoImages(img1, img2):
    img = img1 - img2
    img[img < 0] = 0
    return img


def erodeBinaryImage(img, structuring_element_size =3):
    assert img.shape[0] >= structuring_element_size  and img.shape[1] >= structuring_element_size 

  # Créez un noyau de convolution rempli de 1 avec la taille souhaitée
  # Créez une image de sortie remplie de zéros avec les mêmes dimensions que l'image d'entrée
    eroded_img = np.zeros_like(img)

  # Itérez sur chaque pixel de l'image d'entrée
    for i in range(structuring_element_size //2, img.shape[0]-structuring_element_size //2):
        for j in range(structuring_element_size //2, img.shape[1]-structuring_element_size //2):
      # on decoupe un sous tableau de taille structuring_element_size dna l'image d'origine centré sur le pixel courant
            sub_array = img[i-structuring_element_size //2:i+structuring_element_size //2+1,
             j-structuring_element_size //2:j+structuring_element_size //2+1]

      # Appliquer l'opération d'érosion en prenant le minimum de tous les éléments du sous-tableau
            eroded_img[i, j] = np.min(sub_array)
        
    return eroded_img



    

def dilateBinaryImage(img, structuring_element_size =3):

    # Vérifiez que la taille du noyau de convolution est inférieure ou égale à la taille de l'image
    assert img.shape[0] >= structuring_element_size  and img.shape[1] >= structuring_element_size 

  # Créez une image de sortie remplie de zéros avec les mêmes dimensions que l'image d'entrée
    dilated_img = np.zeros_like(img)

  # Itérez sur chaque pixel de l'image d'entrée
    for i in range(structuring_element_size //2, img.shape[0]-structuring_element_size //2):
        for j in range(structuring_element_size //2, img.shape[1]-structuring_element_size //2):
      # on decoupe un sous tableau de taille structuring_element_size dans l'image d'origine centré sur le pixel courant
            sub_array = img[i-structuring_element_size //2:i+structuring_element_size //2+1,
             j-structuring_element_size //2:j+structuring_element_size //2+1]

      # Appliquer l'opération d'érosion en prenant le minimum de tous les éléments du sous-tableau
            dilated_img[i, j] = np.max(sub_array)
        
    return dilated_img
 
 
def closing(img):
    closed_img =  erodeBinaryImage(dilateBinaryImage(img))
   
    return closed_img
                
def opening(img):
    open_img =    dilateBinaryImage(erodeBinaryImage(img))
    return open_img


def lantuejoulSkeleton(img,iteration=40):
    #TODO: tester sans la première itération

    # on crée une image remplie de 0
    img_full = np.zeros((len(img),len(img[0]) ),dtype=int)
    img_skeleton = np.zeros((len(img),len(img[0]) ),dtype=int)
    n = 0
    imgErodedSize_n = erodeBinaryImage(img,n)
    imgOpen = opening(imgErodedSize_n)
    imgSub = subtractionOfTwoImages(imgErodedSize_n,imgOpen)
    img_skeleton =  additionOfTwoImages(imgSub,img_skeleton)
    print("Lantuejoul: " ,n+1)

    # boucle sur les itérations
    for n in range(1, iteration -1  ):
     
        imgErodedSize_n = erodeBinaryImage(img,n)

        # si l'image erodé est égale à une image remplie de 0 on sort de la boucle car on a atteint l'idempotence
        if np.array_equal(imgErodedSize_n,img_full):
            break
        # sinon on continue

        # on applique l'opération d'ouverture
        imgOpen = opening(imgErodedSize_n)

        # on soustrait l'image erodé de l'image ouverte
        imgSub = subtractionOfTwoImages(imgErodedSize_n,imgOpen)

        # on ajoute le résultat à l'image squelette
        img_skeleton =  additionOfTwoImages(imgSub,img_skeleton)
      
        print("Lantuejoul: " ,n+1)
        n+=1
  
    return img_skeleton



#Amincissement 
def thinning(img, neighbourhood_pattern):
    thinned = np.array(img, dtype=int)

    # parcourir l'image en prenant en compte la taille de la configuration de voisinnage
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):

            # on ne fait pas les calculs pour les pixels de valeur 0
            if img[i][j] == 1:
                identical_pixel_number = 0

                # parcourir la configuration de voisinnage
                for rows in range(-1, 2):
                    for columns in range(-1, 2):

                        # si la valeur du pixel est 2 on ne fait pas de comparaison et on incrémente le compteur
                        if neighbourhood_pattern[rows + 1][columns + 1] == 2:
                            identical_pixel_number += 1
                        
                        #sinon on compare la valeur du pixel avec la valeur de la configuration de voisinnage
                        else:
                            compare = img[i + rows][j + columns] - neighbourhood_pattern[rows + 1][columns + 1]
                            # si les valeurs sont identiques on incrémente le compteur
                            if  compare == 0:
                                identical_pixel_number += 1
                # si tous les pixels sont identiques on amincit le pixel
                if identical_pixel_number == 9:
                    thinned[i][j] = 0

    return thinned


#Epaississement
def thickening(img, neighbourhood_pattern):
    thickened = np.array(img, dtype=int)

    # parcourir l'image en prenant en compte la taille de la configuration de voisinnage
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):

           # on ne fait pas les calculs pour les pixels de valeur 1
            if img[i][j] == 0:
                identical_pixel_number = 0

                # parcourir la configuration de voisinnage
                for rows in range(-1, 2):
                    for columns in range(-1, 2):

                        # si la valeur du pixel est 2 on ne fait pas de comparaison et on incrémente le compteur
                        if neighbourhood_pattern[rows + 1][columns + 1] == 2:
                            identical_pixel_number += 1
                        
                        #sinon on compare la valeur du pixel avec la valeur de la configuration de voisinnage
                        else:
                            compare = img[i + rows][j + columns] - neighbourhood_pattern[rows + 1][columns + 1]
                            if  compare == 0:
                                identical_pixel_number += 1
                                
                # si tous les pixels sont identiques on épaissit le pixel
                if identical_pixel_number == 9:
                    thickened[i][j] = 1

    return thickened

#Amincissement homotopique
def skeleton_thinning_homotopic(img):

    # copier l'image dans des variables locales
    # pour éviter de modifier l'image originale lors des opérations de amincissement on utilise squeletteN
    squeletteN = np.array(img, dtype=int)

    # pour vérifier l'idempotance on utilise squelette qui sera une copie de squeletteN
    squelette = np.array(img, dtype=int)
    
    neighbourhood_pattern = [[0, 0, 0],
                           [2, 1, 2],
                           [1, 1, 1]]


    counter = 0
    counter_similarity = 0
    while True:
        squeletteN = thinning(squeletteN,neighbourhood_pattern)

        counter += 1
        print(f'Amincissement homotopique - boucle: {counter}')

        # vérification de l'idempotance
        if (squelette == squeletteN).all():
            counter_similarity += 1
        else:
            counter_similarity = 0
        # au bout de 2 itérations consécutives, on arrête la boucle
        if counter_similarity > 2 or counter > 500:
            break

        # copie par valeur de squeletteN dans squelette
        squelette = np.copy(squeletteN)
        #rotation de la matrice de l'élémet structurant
        neighbourhood_pattern = neighbourhoodRotate(neighbourhood_pattern)

    return squeletteN

#Rotation de la configuration de voisinnage
def neighbourhoodRotate(neighbourhood_pattern):
    rotated = np.array(neighbourhood_pattern, dtype=int)
    
    # rotation de 45°
    rotated[0][1] = neighbourhood_pattern[0][0]
    rotated[0][2] = neighbourhood_pattern[0][1]
    rotated[1][2] = neighbourhood_pattern[0][2]
    rotated[2][2] = neighbourhood_pattern[1][2]
    rotated[2][1] = neighbourhood_pattern[2][2]
    rotated[2][0] = neighbourhood_pattern[2][1]
    rotated[1][0] = neighbourhood_pattern[2][0]
    rotated[0][0] = neighbourhood_pattern[1][0]
    # rotated[1][1] = neighbourhood_pattern[1][1] 
    # pas besoin de le changer la valeur du centre 
 
    return rotated