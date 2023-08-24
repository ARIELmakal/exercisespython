
def truc(x):
    print(x)
    return(2*x)
    print(3*x)
    return(4*x)

def bidule(x):
    print(x)
    print(2*x)
    return(3*x)
    print(4*x)
 
print(bidule(20))
print()
print(truc(10))

'''
La fonction truc() retourne tout les élement avant return et return lui meme. Tout ce quie est renvoyer après de pas pris en compte
La fonction bidule() retourne return et tous les elements avant avant car il est celui qui cloture l'affichage
'''