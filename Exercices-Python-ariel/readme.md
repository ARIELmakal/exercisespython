# Exercices Python

## Consignes 
+ Pour chaque exercice, créer un fichier .py unique
+ Mettre des commentaires appropriés à chaque étape
+ Tu ne dois modifier que la branche `ariel`.
+ Les remarques et exercices supplémentaires seront ajoutés dans la branche `main`.
## Exercices

### Exercice 1
Transformer 42569 secondes en heures, minutes, secondes.

### Exercice 2
Un magasin de reprographie propose un tarif dégressif. Les 20 premières photographies sont facturées à 10
centimes et les suivantes à 8 centimes.
1. Calculer à la main le coût de 15 puis de 30 photocopies.
2. Écrire une fonction prix(n) qui renvoie le prix en euros pour n photocopies. La tester.

### Exercice 3
Voici deux fonctions nommées truc et bidule.
```python
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
```


On exécute truc(10).
1. Quelle(s) valeur(s) (est) sont affichée(s)? Quelle valeur est renvoyée?
2. Même question avec bidule(10).

### Exercice 4 (Diviseurs d’un nombre triangulaire)
Un nombre est dit triangulaire d’indice n s’il égal à 1+2+3+···+n.
Par exemple, le nombre triangulaire d’indice 5 vaut 15 car 1+2+3+4+5=15.
1. Écrire une fonction triangle qui renvoie la valeur du nombre triangulaire d’indice n.
Par exemple triangle(5) renverra 15.
2. Écrire une fonction nbre_diviseurs qui renvoie le nombre de diviseurs d’un entier n ∈ N∗.
Par exemple, les diviseurs de 6 sont 1, 2, 3, 6. Il y a donc 4 diviseurs, ainsi nbre_diviseurs(6) renverra
4
3. Écrire un script qui détermine le plus petit nombre triangulaire qui admette au moins 50 diviseurs.
Exercice 5 (Découverte des factorielles)
Soit n ∈N∗, on appelle «factorielle n» noté n!, l’entier n!=1×2×···×n avec la convention 0!=1.
Par exemple, 4!=1×2×3×4=24=4×3!.
1. Écrire le nombre 15×14×13×12×11 comme un quotient de deux factorielles.
2. Exprimer à l’aide de factorielles les deux produits suivants : 2×4×6×···×100 et 1×3×5×···×99.
3. Combien y-a-t-il d’anagrammes du mot fleur? Et du mot tennis?
4. Écrire un script qui calcule 64!
5. Écrire une fonction factorielle qui prend en argument un entier naturel n et renvoie n!

### Exercice 6 (Combien de truc et bidule?)
Pour les trois scripts suivants, dire ce qui est affiché et combien de fois.
for i in range(3):
 print(’bidule’)
print(’truc’)
for i in range(3):
 print(’bidule’)
for j in range(4):
 print(’truc’)
for i in range(3):
 print(’bidule’)
 for j in range(4):
 print(’truc’)

### Exercice 7 (Nombres d’Amstrong)
On souhaite déterminer les entiers naturels qui sont égaux à la somme des cubes de leurs chiffres. De tels
entiers seront appelés des nombres d’Armstrong.
Par exemple, l’entier 0 est un nombre d’Armstrong car 0&sup3; = 0
mais l’entier 59 n’en est pas un car
5&sup3; + 9&sup3; = 854
donc
5&sup3; + 9&sup3; &ne; 59.
1. Écrire une fonction somme_cubes_chiffres qui prend en argument un entier naturel et renvoie la
somme des cubes de ses chiffres.
Par exemple, somme_cubes_chiffres(256) devra renvoyer
2&sup3; + 5&sup3; + 6&sup3; = 349.
2. Écrire un script qui détermine les nombres d’Amstrong inférieurs à 10 000.

### Exercice 8
Ecrire un programme en langage Python qui demande à l’utilisateur de saisir un nombre entier
n et de lui afficher si ce nombre est carré parfait ou non.


### Exercice 9
Ecrire un programme en Python qui demande à l’utilisateur de saisir une chaine de caractère s
et de lui renvoyer un message indiquant si la chaine contient la lettre ‘a’ tout en indiquant sa
position sur la chaine. Exemple si l’utilisateur tape la chaine s = ‘langage’ le programme lui
renvoie :
```
La lettre ‘a’ se trouve à la position : 1 La lettre ‘a’ se trouve à la position : 4
```

### Exercice 10
Ecrire un programme en langage Python, qui permet de compter le nombre de voyelles et de consonnes dans
une chaine donnée. Exemple pour la chaine s= `‘anticonstitutionellement’` le programme doit
renvoyer le message suivant :
```
 La chaine anticonstitutionellement possède 10 voyelles.
```
### Exercice 11
Ecrire un programme Python qui permet d’échanger le premier et le dernier mot. Exemple si la chaîne est:
```
 “Python est un langage de programmation”.
```
, le programme renvoie la chaine :
```
 “programmation est un langage de Python”.
```
On suppose que le texte est bien formé ( un
espace après chaque ponctuation et aucun espace avant la ponctuation)

### Exercice 12
Soit la classe `Date` définie par le diagramme de classe UML suivant :

Date        |
------------
jour : int  |
mois : int  |
année : int |

+ Implémenter cette classe en Python.
Dans la méthode de construction de la classe, **prévoir** un dispositif pour éviter les dates impossibles (du genre 32/14/2020). Dans ce cas, la création doit provoquer une erreur, chose possible grâce à l'instruction `raise` (documentation à rechercher!)

+ Ajouter une méthode `__repr__` permettant d'afficher la date sous la forme "25 janvier 1989". Les noms des mois seront définis en tant qu'attribut de classe à l'aide d'une liste.

+ Ajouter une méthode `__lt__` qui permet de comparer deux dates. L'expression `d1 < d2` (`d1` et `d2` étant deux objets de type `Date`) doit grâce à cette méthode renvoyer `True` ou `False`

### Exercice 13
&Eacute;crire la définition de la classe `Personne` ayant trois attributs définissant certaines caractéristiques d'une personne réelle : `taille`,`poids` et `age`.
Cette classe aura : 
+ une méthode `imc()` qui détermine l'**IMC** de la personne,
+ une méthode `interpretation()` qui affiche "Insuffisance pondérale" si l'IMC est inférieur ou égale à 18,5 et qui affiche "obésité" si l'IMC est supérieur ou égale à 30.
Rappel : l'IMC(Indice de masse corporelle) est donné par la formule *poids/taille&sup2;* avec le poids en kg et la taille en m

### Exercice 14


### Exercice 15


### Exercice 16


### Exercice 17