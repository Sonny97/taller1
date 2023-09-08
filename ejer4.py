print(""" Holii UwU
Vamos a encontrar un numero magico.
""")

userNumber = int(input("Porfavor digita un numero cualquiera: "))

if (userNumber % 5 == 0) and (userNumber % 3 != 0) and (userNumber % 2 != 0):
    print("Es un numerito especial el tuyo")
else: print("Esa monda no es especial.")