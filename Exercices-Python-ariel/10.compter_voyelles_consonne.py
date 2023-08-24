"""
Ce code prend prend en compte la chaine de caractère entrée par l'utilisateur et compare par chaque chaine de caractère se trouvant dans les tuples(vowels, consonants)
et apres être parcouru par for nous affichons le nombre de voyelle et consonne.
"""
mots = input(">> Mots: ")
voyelles = ["a","A", "E","e", "i","I", "o","O","U", "u"]
consonants = ["b","B", "c","C", "d","D", "f","F", "g","G", "h","H", "j","J", "k","K", "l","L", "m","M", "n","N", "p","P", "q","Q", "r","R", "s","S", "t","T", "v","V", "w","W", "x","X", "y","Y", "z","Z"]
nobre_voyelles = 0
nbre_consonne = 0
for string in mots:
  if string in voyelles:
    nobre_voyelles += 1
  elif string in consonants:
    nbre_consonne += 1
print(f">> La chaine de caractère {mots} a {nbre_consonne} consonne(s) et {nobre_voyelles} voyelle(s)")

