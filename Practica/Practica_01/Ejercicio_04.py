# Ejercicio 4:
# Diseña un programa que, dado un número entero, determine si éste es el doble de un
# número impar. (Ejemplo: 14 es el doble de 7, que es impar.)

Numero = 14
Doble = Numero/2

if (Doble % 2 == 0):
    print (Numero, "Es el Doble de", Doble, ",", "Que es Par")
else:
    print (Numero, "Es el Doble de", Doble, ",", "Que es Impar")