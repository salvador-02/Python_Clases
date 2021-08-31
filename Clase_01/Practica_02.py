
#Ej.4 Area Rectangulo
Base = 4
Altura = 5
Area = (Base * Altura)
print(Area)


#Ej.5 Area Circulo 
import math
Radio = 5
area = math.pi*Radio**2
print(area)


#Ej.1 Palindromo 
Palabra = "neuquen"
if Palabra == ''.join(reversed(Palabra)):
    print("Es Palindroma")
else:
    print("No es Palindroma")