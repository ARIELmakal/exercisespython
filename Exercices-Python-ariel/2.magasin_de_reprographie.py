#Nombre de photocopie à faire
nbre_photocopie = int(input(">> Nombre de photocopies: "))

#Cas où le nombre de photocopie est inferieure ou égale à 20 alors nous restons dans le tarrif normal
if nbre_photocopie <= 20: 
    price = nbre_photocopie * 10 # tarif normal
    print(f">> {price }centimes")

#Cas où le nombre de photocopie est supérieure à 20 alors prendrons le 20 premiers impressions avec le tarrif normal et le reste sera pris dans le tarrif dégressif 
else:
    price1 = 20 * 10
    price = price1 + (nbre_photocopie - 20 ) * 8 #tarif normal + tarif dégressif (*8)
    print(f">> {price} centimes")

#Cette fonction renvoie le prix converti en euro
def prix_euro(nbre):
    a = nbre / 100
    return a
#Affichage du prix
print(f"{prix_euro(price)}£")