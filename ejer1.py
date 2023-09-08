print(""" Bienvenido al ejercicio que realiza calculos con fracciones.
Acontinuacion vamos a digitar numeritos...

diviertete!!    :D

""")
numerador = int(input("Porfavor digita el valor del numerador de la fraccion 1: "))
denominador = int(input("Porfavor digita el valor del denominador de la fraccion 1: "))
if denominador == 0:
    print("El denominador no puede ser 0. >:( ")
    exit()
fraction1 = numerador / denominador
numerador = int(input("Porfavor digita el valor del numerador de la fraccion 2: "))
denominador = int(input("Porfavor digita el valor del denominador de la fraccion 2: "))
if denominador == 0:
    print("El denominador no puede ser 0, vuelve cuando aprendas a digitar. >:( ")
    exit()
fraction2 = numerador / denominador

operator = input("""Digite el tipo de operador entre
'+' para Sumar
'-' para Sumar
'*' para Sumar
'/' para Sumar
""")

result = 0

if fraction2 == 0 and operator == '/':
    print("No es posible realizar division entre '0'.")
elif operator == '+':
    result = fraction1 + fraction2
elif operator == '-':
    result = fraction1 - fraction2
elif operator == '*':
    result = fraction1 * fraction2
elif operator == '/':
    result = fraction1 / fraction2

print('Y eso dio como resultado: ', result)
