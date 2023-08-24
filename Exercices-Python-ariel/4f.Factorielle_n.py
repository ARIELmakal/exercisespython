def factorielle(nbre):
    fact = 1
    for i in range(1, nbre+1):
        fact = fact *i
    print(f"{nbre}! = {fact}")

factorielle(100)