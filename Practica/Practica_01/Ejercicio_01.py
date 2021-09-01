# Ejercicio 1:
# Diseña un programa que lea la edad de dos personas y diga quién es más joven, la
# primera o la segunda. Ten en cuenta que ambas pueden tener la misma edad. En tal caso,
# hazlo saber con un mensaje adecuado.

Persona1 = {"Nombre" : "Angel" , "Edad" : "35"}
Persona2 = {"Nombre" : "Luis" , "Edad" : "27"}

if Persona1.get("Edad") == Persona2.get("Edad"):
    print(Persona1.get("Nombre"),"tiene la misma edad que", Persona2.get("Nombre"))

if Persona1.get("Edad") < Persona2.get("Edad"):
    print(Persona1.get("Nombre"),"es mas joven", "que", Persona2.get("Nombre"))
else:
    print(Persona2.get("Nombre"), "es mas joven que", Persona1.get("Nombre"))