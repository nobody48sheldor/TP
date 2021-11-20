import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

# Nom complet du fichier contenant les données
nom_fichier = "exp1.txt"      # Ligne à compléter

#Lecture des données expérimentales
f = open(nom_fichier,"r")
tableau = f.readlines()
f.close()
T = []
S = []
variables = tableau.pop(0).split('\t')
unites = tableau.pop(0).split('\t')
for ligne in tableau:
	l = ligne.split('\t')
	T.append(float(l[0].replace(',','.')))
	S.append(float(l[1].replace(',','.').replace("\x00","")))
T = np.array(T)
S = np.array(S)

# On obtient deux tableaux Numpy :
# le tableau T qui contient les dates
# le tableau S qui contient les mesures

# Caractérisation de la réaction : valeur de la concntration initiale C0 en mol/L
C0 = 2.15*(10**(-3))       # Valeur à compléter

# Calcul de la concentration en produit (HCl)  P en mol/L
P =S/(380e3)       #Formule à compléter

# Calcul de la concentration en réactif (CH3)3CCl R en mol/L
R = C0 - P        # Formule à compléter

# Calcul de la vitesse de formation
V=[]
TV = T[1:-1] # On retire les indices extrêmes pour que les index des dates correspondent à ceux des vitesses

for i in range(1,len(R)-1):
	V.append(-(R[i+1] - R[i-1])/(T[i+1]-T[i-1]))     #Formule à compléter

#Modélisation


# Affichage des courbes demandées
plt.title("concentration en réactifs en fonction du temps")     # Ligne à compléter
plt.plot(T, R, color='red', label="concentration en réactifs en fonction du temps")        # Ligne à compléter
plt.xlabel("temps (s)")      # Ligne à compléter
plt.ylabel("concentration (mol/L)")   # Ligne à compléter
plt.legend()
plt.grid()
plt.show()

plt.title("vitesse d'évolution des concentration des réactifs en fonction du temps")     # Ligne à compléter
plt.plot(TV, V, color='blue', label="vitesse d'évolution des concentration des réactifs en fonction du temps")        # Ligne à compléter
plt.xlabel("temps (s)")      # Ligne à compléter
plt.ylabel("concentration (mol/L)")   # Ligne à compléter
plt.legend()
plt.grid()
plt.show()

plt.title("vitesse d'évolution des concentration des réactifs en fonction du temps")     # Ligne à compléter
plt.plot(R, V, color='green', label="vitesse d'évolution des concentration des réactifs en fonction du temps")        # Ligne à compléter
plt.xlabel("temps (s)")      # Ligne à compléter
plt.ylabel("concentration (mol/L)")   # Ligne à compléter
plt.legend()
plt.grid()
plt.show()
