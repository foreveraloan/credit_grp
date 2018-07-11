"""
Placer ce fichier dans un dossier vide
et initialiser un repertoire git dedans

"""
'''git init'''

"""
commit this file in git
"""
'''git add kata4.py
commit -m "add kata4.py"'''


"""
Matrice de rotation

pour les matrices 2x2 les matrices de rotations sont
de la forme suivante et comme leur nom l'indique ont
pour fonction de faire tourner les vecteurs :

    cos theta -sin theta
    sin theta cos theta


coder la fonction build_rotation_matrix(theta)

qui retourne une matrice de rotation

"""
import numpy as np

def build_rotation_matrix(theta):
    theta = np.radians(30)
    c = np.cos(theta)
    s = np.sin(theta)
    R = np.matrix('{} {}; {} {}'.format(c, -s, s, c))
    #print(R)
    X = np.array((0,1))
    #print(X)
    return R.dot(X)

"""

commit le fichier à nouveau

"""
'''git commit -m "add kata_4.py update"'''
"""

Créer une branche "dev" avec la commande
git checkout -b dev

"""
'''git branch dev'''
'''git branch checkout dev'''
"""
Afficher la matrice de rotation pour theta = pi / 2
"""
pi = np.pi
rot_mat_pi = build_rotation_matrix((pi/2))

"""
Calculer la multiplication entre la matrice de rotation pi / 2 et le vecteur
[1 0] et le vecteur [0 1]

"""
def matrix_vector_multiplication(mat, vect):
    r = np.zeros(vect.shape)
    cols = []
    for i, v in enumerate(vect):

        r += mat[:, i] * v
    return r

v = np.array([1, 0])
print (rot_mat_pi)
matrix_vector_multiplication(v, rot_mat_pi)
"""
commit le fichier

"""


"""
retourner sur la branche master.
vérifier que le fichier ne comporte pas les
modifications effectuées sur la branche dev
"""

"""
fusionner les modifications de la branche dev
dans la branche master

"""
