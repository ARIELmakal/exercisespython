#Nous convertir temps = 42569s en heures minutes secondes:
temps = 42569

''' 
a)      Nous savons que 1h équivaut 3600sec et c'est exactement ce par quoi nous allons commencer, 
en divisant (temps) par 3600 et ainsi convertir le quotient en int() et nous ainsi la valeur de l'heure que nous allons stocker dans la variable (heure)
'''
heure = int(temps / 3600)


#Ensuite nous allons récuperer le reste de la division en utilisant le signe %(modulo) dans la variable min1
min1 = temps % 3600


#la valeur de la minutes que nous allons stocker dans la variable minute une fois divisé puis converti en int()
minute = int(min1 / 60)

#Et les restes des secondes étant inférieurs à 60 sont gardées telles quelles.
sec = min1 % 60

#On affichera ainsi le resultat suivant et voila !
print(f"{heure}h {minute}min {sec}sec")