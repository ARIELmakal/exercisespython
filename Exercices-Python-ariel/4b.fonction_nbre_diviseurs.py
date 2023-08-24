def nbre_diviseur():
  n = int(input(">> nombre: "))
  nbre_div = 0
  for i in range(1, n+1):
    if n % i == 0:
      nbre_div = nbre_div + 1
  print(nbre_div)


nbre_diviseur()



