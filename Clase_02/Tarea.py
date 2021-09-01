#dado dos datos de alturas de dos diferentes personas, decir cual es la mayor, devolver el nombre y la altura de las dos

Persona1 = {"Nombre" : "Angel" , "Altura" : "1.85"}
Persona2 = {"Nombre" : "Luis" , "Altura" : "1.78"}

if Persona1.get("Altura") == Persona2.get("Altura"):
    print(Persona1.get("Nombre"),"mide", Persona1.get("Altura"), "y", Persona2.get("Nombre")
    , "mide", Persona2.get("Altura"), "por ende, miden lo mismo")

if Persona1.get("Altura") > Persona2.get("Altura"):
    print(Persona1.get("Nombre"),"es mas alto porque mide", Persona1.get("Altura"), "encambio", Persona2.get("Nombre")
    , "mide", Persona2.get("Altura"))
else:
    print(Persona2.get("Nombre"), "es mas alto porque mide", Persona2.get("Altura"), "minetras que", Persona1.get("Nombre"), "mide"
    , Persona1.get("Altura"))



#determinar si una persona es mayor de edad para conducir, utilizando una variable booleana

Limite = 18
Edad = 16
if Edad >= Limite:
    print("Puede Conducir")
else:
    print("No puede conducir")
