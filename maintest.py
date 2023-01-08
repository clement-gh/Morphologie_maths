from functions import *
from listeFonction import *


struc = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

print(struc[1][1])

def rotate_matrixe_sens_negatif(element_structurant):
    element_structurant_rotated = np.array(element_structurant, dtype=int)
    '''
    Par exemple [[2, 0, 2],
                [1, 1, 0],
                [1, 1, 2]]
    devient [[1, 2, 0],
            [1, 1, 2],
            [1, 2, 0]]
    '''
    #copier les éléments de la matrice (le centre non compris) dans un tableau 1d
    #en gardant l'ordre
    elements_matrice_1d_sans_centre = np.zeros(8, dtype=int)

    elements_matrice_1d_sans_centre[0] = element_structurant[0][0]
    elements_matrice_1d_sans_centre[1] = element_structurant[0][1]
    elements_matrice_1d_sans_centre[2] = element_structurant[0][2]
    elements_matrice_1d_sans_centre[3] = element_structurant[1][2]
    elements_matrice_1d_sans_centre[4] = element_structurant[2][2]
    elements_matrice_1d_sans_centre[5] = element_structurant[2][1]
    elements_matrice_1d_sans_centre[6] = element_structurant[2][0]
    elements_matrice_1d_sans_centre[7] = element_structurant[1][0]

    #appliquer la rotation
    element_structurant_rotated[0][1] = elements_matrice_1d_sans_centre[0]
    element_structurant_rotated[0][2] = elements_matrice_1d_sans_centre[1]
    element_structurant_rotated[1][2] = elements_matrice_1d_sans_centre[2]
    element_structurant_rotated[2][2] = elements_matrice_1d_sans_centre[3]
    element_structurant_rotated[2][1] = elements_matrice_1d_sans_centre[4]
    element_structurant_rotated[2][0] = elements_matrice_1d_sans_centre[5]
    element_structurant_rotated[1][0] = elements_matrice_1d_sans_centre[6]
    element_structurant_rotated[0][0] = elements_matrice_1d_sans_centre[7]

    print("element structurant: ")
    print(element_structurant)
    print("element structurant rotated")
    print(element_structurant_rotated)

    return element_structurant_rotated