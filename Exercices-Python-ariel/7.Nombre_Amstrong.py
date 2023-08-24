
def somme_cubes():
    n = int(input(">> NOMBRE: "))
    
    somme = 0
    for chiffre in str(n):
    # on utilise le type (str) pour convertir le nombre entier en chaine de caractère car cela nous permettra de parcourir tout le chiffre
    # on réutilisera le type (int) pour reconvertir la chaine de caractère en type (int)
        somme = (int(chiffre) ** 3) + somme
    print(somme)
somme_cubes()