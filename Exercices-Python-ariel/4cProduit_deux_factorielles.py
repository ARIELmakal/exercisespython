first_number = int(input("Enter the first number: "))
second_number = int(input("Entrer the second number:  "))
f = 1
f1 = 1
for number1 in range (1, first_number+1):
    f = f * number1
for number2 in range (1, second_number+1):
    f1 = f1 * number2
sum = round (f / f1, 3)
print(f"{f}/{f1} = {sum}")