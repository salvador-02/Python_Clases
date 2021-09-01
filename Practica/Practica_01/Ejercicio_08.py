# Ejercicio 8:
# Escribir un programa que permita ingresar las coordenadas (x,y) de un punto en el plano y
# verifique si el punto está dentro del círculo con centro en (0,0) y radio 10, o está fuera o en
# la circunferencia. Mostrar los mensajes adecuados.

CordenadaX = 10
CordenadaY = 1

if CordenadaX > 10 or CordenadaY > 10:
    print(CordenadaX, "y", CordenadaY, "Estan Fuera de la Circunferencia")
else:
    print(CordenadaX, "y", CordenadaY, "Estan Dentro de la Circunferencia")

