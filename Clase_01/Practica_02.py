
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
Palabra = ("arroz")
Palabra1 = ("zorra")
if Palabra == ''.join(reversed(Palabra1)):
    print(Palabra, "es palindroma")
else:
    print(Palabra, "no es palindroma")