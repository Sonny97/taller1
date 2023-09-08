print(""" Holii UwU
    Vamos a capturar tu (IMC)
Osea tu indice de masa corporal. ;)
""")

peso = int(input("Hazme el favor de digitar tu peso en Kg: "))
altura = float(input("Hazme el favor de digitar tu altura en metros: "))

imc = peso / altura**2

print("Tu Indice de Masa Corporal (IMC) es de: ", imc)