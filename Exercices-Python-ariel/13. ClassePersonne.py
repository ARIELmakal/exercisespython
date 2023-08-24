import math
class Personne:
    def __init__(self, nom:str, age:int, taille:float, poids:float):
        self.poids = poids
        self.taille = taille
        self.age = age
        self.nom = nom
    def IMC(self):
        Imc = self.poids / (math.pow(self.poids,2))
        return Imc
    def interpretation(self):
        imc = self.IMC()
        if imc <= 18:
            print(f"{self.nom} a {self.age}ans: Insuffisance pondérale")
        elif imc >= 30:
            print(f"{self.nom} a {self.age}ans: Oésité")
            


        
        

personne1 = Personne("Ariel",45,1.89,65)
personne1.interpretation()