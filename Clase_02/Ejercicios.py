# Hacer un programa que introduzca el usuario dos palabras y detectar si es un anagrama.

Palabra1 = ("Sapo")
Palabra2 = ("Sopa")

Palabra1_list = list(Palabra1)
Palabra2_list = list(Palabra2)

Palabra1_list.sort()
Palabra2_list.sort()

Palabra1_list = "".join(Palabra1_list)
Palabra2_list = "".join(Palabra2_list)

if Palabra1_list == Palabra2_list:
    print(Palabra1, "y", Palabra2, "son un anagrama")
else:
    print(Palabra1, "y", Palabra2, "no son un anagrama")



# Realizar un programa para introducir un mail  y  verificar si esta correcto o no. 

mail = ("salvdor.mastandrea@comunidad.ub.edu.ar")

if "@" in mail:
    print("Este mail es correcto")
else: 
    print("Este mail es incorrecto")



# hacer un programa que el usurario escriba una frase y detectar si existe la palabra argentina.

Frase = ("frase Argentina")

if "Argentina" in Frase:
    print("Este frease contiene la palabra Argentina")
else: 
    print("Este frase no contiene la palabra Argentina")



# Realizar un programa que me devuelva el área de un rectángulo, introduciendo por teclado base y altura -🡪  area = base * altura

Base = 4
Altura = 5
Area = (Base * Altura)
print(Area)


# Realizar un programa que me devuelva la superficie del círculo, introduciendo por teclado radio. Definir la constante PI.

import math
Radio = 5
area = math.pi*Radio**2
print(area)