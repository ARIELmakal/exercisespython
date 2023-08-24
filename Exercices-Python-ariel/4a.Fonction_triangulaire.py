'''En utilisant la formule générale d'indice n = n * (n+1)/2'''
def nbre_triangulaire():
    nombre_triangulaire = int(input(">> Nombre triangulaire: "))
    reponse_trg = int((nombre_triangulaire*(nombre_triangulaire+1))/2)
    print(f"\n>> {reponse_trg}")

nbre_triangulaire()