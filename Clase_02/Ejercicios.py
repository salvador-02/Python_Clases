#Ej.1
# Hacer un programa que introduzca el usuario dos palabras y detectar si es un anagrama.

Palabra1 = ("Sapo")
Palabra2 = ("Sopa")

Palabra1_list = list(Palabra1)
Palabra2_list = list(Palabra2)

Palabra1_list.sort()
Palabra2_list.sort()

if Palabra1_list == Palabra2_list:
    print(Palabra1, "y", Palabra2, "son un anagrama")
else:
    print(Palabra1, "y", Palabra2, "no son un anagrama")



#Ej.2
# Realizar un programa para introducir un mail  y  verificar si esta correcto o no. 

mail = ("salvdor.mastandrea@comunidad.ub.edu.ar")

if "@" in mail:
    print("Este mail es correcto")
else: 
    print("Este mail es incorrecto")



#Ej.3
# Hacer un programa que el usurario escriba una frase y detectar si existe la palabra argentina.

Frase = ("frase Argentina")

if "Argentina" in Frase:
    print("Este frease contiene la palabra Argentina")
else: 
    print("Este frase no contiene la palabra Argentina")



#Ej.4
# Realizar un programa que me devuelva el área de un rectángulo, introduciendo por teclado base y altura -🡪  area = base * altura

Base = 4
Altura = 5
Area = (Base * Altura)
print("El area del rectangulo es",Area)


#Ej.5
# Realizar un programa que me devuelva la superficie del círculo, introduciendo por teclado radio. Definir la constante PI.

import math
Radio = 5
area = math.pi*Radio**2
print("La superficie del circulo es", area)

