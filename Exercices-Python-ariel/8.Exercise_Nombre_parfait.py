'''Pour determiner si un nombre entier est un carré parfait il faut:
        Calculez la racine carrée du nombre. Si la racine carrée est un nombre entier, alors le nombre est un carré parfait
        Pour faire simple, si la racine carré d'un nombre est un nombre entier alors ce nombre est un carré parfait'''
import math

nombre = int(input("Enter the number: "))
racine_carre = math.sqrt(nombre)

if isinstance(racine_carre, int):
    print("Le nombre entrer est un carre parfait")
else:
    print("Le nombre entré n'est pas un carré parfait")