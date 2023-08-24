#Demande à l'utlisateur d'entrer une chaine caractères
mots = input(">> Chaîne de caractère: ")
#Je sépare le mot entrer par l'utilisateur en leur plaçant dans une tuple en appliquant la methode str.split()
chaine = mots.split(" ")

#Verification de la chaine de caractère entrée par l'utilisateur si elle est supérieure ou egale à 2mots pour effectuer les changements.
if len(chaine) >= 2:
    #Echange de chaine de caractère entre le premier et le dernier mots
    chaine[0], chaine[-1] = chaine[-1], chaine[0]
    #Reconstitution de la nouvelle chaine créée dans une nouvelle phrase.
    new_chaine = ' '.join(chaine)
    print(f"{new_chaine}")
else:
    print("La chaine de caractère entrée doit comporter deux ou plusieurs mots pour effectuer les changements")